from django.contrib.auth.signals import user_logged_in
from django.utils import timezone
from rest_framework import permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from knox.settings import knox_settings

from qp.api.serializers.player import (
    qpPlayerSerializer,
    qpPlayerCreateSerializer,
    qpPlayerLoginSerializer
)


class qpRegisterView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = qpPlayerCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            "valid": True
        })


class qpLoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = qpPlayerLoginSerializer

    def get_token_limit_per_user(self):
        return knox_settings.TOKEN_LIMIT_PER_USER
    
    def clean_expired_tokens(self, user):
        now = timezone.now()
        tokens = user.auth_token_set.filter(expiry__lt=now)
        tokens.delete()
    
    def clean_exceeded_tokens(self, user):
        limit = self.get_token_limit_per_user()
        if limit is None:
            return
        limit -= 1
        tokens = user.auth_token_set.order_by("-created")[limit:]
        for t in tokens:
            t.delete()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        user_logged_in.send(
            sender=user.__class__,
            request=request,
            user=user
        )
        self.clean_expired_tokens(user)
        self.clean_exceeded_tokens(user)
        return Response({
            "valid": True,
            "user": qpPlayerSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
