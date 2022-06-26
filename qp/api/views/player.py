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
        user = serializer.save()
        return Response({
            "user": qpPlayerSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class qpLoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = qpPlayerLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": qpPlayerSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
