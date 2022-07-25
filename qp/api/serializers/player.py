from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.player.models import (
    qpPlayer,
    qpPlayerHero
)

from qp.world.models import (
    qpWorld
)

from qp.api.serializers.world import (
    qpWorldNavSerializer
)


class qpPlayerMeSerializer(serializers.ModelSerializer):
    worldnavs = serializers.SerializerMethodField(source="get_worldnavs")

    class Meta:
        model = qpPlayer
        fields = ["id", "playername", "avatar", "banner", "worldnavs"]
        depth = 1

    def get_worldnavs(self, obj):
        queryset = obj.creator_worlds.filter(
            is_active=True
        )
        queryset |= obj.admin_worlds.filter(
            is_active=True
        )
        queryset |= obj.modo_worlds.filter(
            is_active=True
        )
        for h in obj.heros.filter(is_active=True):
            if h.world:
                queryset |= qpWorld.objects.filter(pk=h.world.pk)
        # ===---
        result = []
        for q in queryset.distinct():
            result.append(qpWorldNavSerializer(q).data)
        return result


class qpPlayerMeHeroSerializer(serializers.ModelSerializer):
    world = serializers.SerializerMethodField(source="get_world")

    class Meta:
        model = qpPlayerHero
        fields = ["id", "name", "avatar", "world", "is_valid", "geo"]
        depth = 1
    
    def get_world(self, obj):
        result = None
        try:
            world = obj.world
            result = {
                "id": world.pk,
                "name": str(world.name),
                "slug": str(world.slug)
            }
        except:
            pass
        return result
