import json

from datetime import timedelta

from django.contrib.auth.signals import user_logged_in
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from knox.models import AuthToken
from knox.settings import knox_settings

from qp.api.serializers.player import (
    qpPlayerSerializer,
    qpPlayerCreateSerializer,
    qpPlayerLoginSerializer
)

from qp.player.models import (
    qpPlayer
)


class qpPlayerView(APIView):

    def get_player(self, player):
        result = {
            "id": player.pk,
            "name": player.name,
            "avatar": "https://i.servimg.com/u/f80/11/34/44/55/pachua10.jpg",
            "banner": "https://i.servimg.com/u/f80/11/34/44/55/banner14.jpg"
        }
        return result

    def get_heros(self, player):
        result = []
        for hero in player.heros.filter(
            is_active=True
        ):
            # =-
            hero_geo = None
            is_can_travel = True
            if hero.geo and hero.geo != "":
                hero_geo = json.loads(hero.geo)
                is_can_travel = True if (hero_geo["cooldown"] - timezone.now().timestamp()) <= 0 else False
            # =-
            avatar = None
            if hero.avatar is not None:
                try:
                    avatar = hero.avatar.url
                except Exception:
                    avatar = None
            # =-
            result.append({
                "id": hero.pk,
                "name": hero.name,
                "initials": hero.initials,
                "world": hero.world.pk,
                "geo": hero_geo,
                "is_can_travel": is_can_travel,
                "avatar": avatar
            })
        return result

    def get(self, request):
        if not request.user.is_authenticated:
            return Response({"valid": False}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            player = request.user.player
        except ObjectDoesNotExist:
            player = qpPlayer.objects.create(
                user=request.user
            )
        # ===---
        player_data = self.get_player(player)
        heros_data = self.get_heros(player)
        # ===---
        return Response({
            "player": player_data,
            "heros": heros_data,
            "valid": True
        })


class qpPlayerHerosView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            player = request.user.player
        except ObjectDoesNotExist:
            return Response({"valid": False}, status=status.HTTP_400_BAD_REQUEST)
        # ===---
        heros_data = qpPlayerView.get_heros(None, player)
        # ===---
        return Response({
            "heros": heros_data,
            "valid": True
        })


class qpPlayerHeroView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        player = request.user.player
        # ===---
        try:
            hero = player.heros.get(pk=pk, is_active=True)
        except ObjectDoesNotExist:
            return Response({"valid": False}, status=status.HTTP_400_BAD_REQUEST)
        # ===---
        print("hero : ", hero)
        print("post : ", request.POST)
        # ===---
        heros_data = qpPlayerView.get_heros(None, player)
        # ===---
        return Response({
            "heros": heros_data,
            "valid": True
        })


class qpRegisterView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = qpPlayerCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            "valid": True
        })


class qpLoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
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
