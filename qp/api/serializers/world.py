from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from qp.world.models import (
    qpWorld,
    qpWorldStyle
)

from qp.api.serializers.forum import (
    qpForumSerializer
)


class qpWorldStyleSerializer(serializers.ModelSerializer):

    class Meta:
        model = qpWorldStyle
        fields = "__all__"


class qpWorldSerializer(serializers.ModelSerializer):
    count_players = serializers.ReadOnlyField(default=0)
    count_heros = serializers.ReadOnlyField(default=0)
    count_chapters = serializers.ReadOnlyField(default=0, allow_null=False)
    count_messages = serializers.ReadOnlyField(default=0)
    copyright = serializers.ReadOnlyField()
    style = serializers.SerializerMethodField(source="get_style")

    class Meta:
        model = qpWorld
        fields = [
            "id",
            "name",
            "description",
            "slug",
            "creator",
            "administrators",
            "moderators",
            "count_players",
            "count_heros",
            "count_chapters",
            "count_messages",
            "forum",
            "visibility",
            "is_active",
            "copyright",
            "style"
        ]
        depth = 1

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        world = qpWorld.objects.get(pk=ret.get("id"))
        world_is_visible = world.get_is_visible(self.context["request"])
        if world_is_visible:
            return ret
        raise PermissionDenied()
    
    def get_style(self, obj):
        result = None
        style = obj.style
        if style is not None:
            result = qpWorldStyleSerializer(style).data
        return result


class qpWorldNavSerializer(serializers.ModelSerializer):

    class Meta:
        model = qpWorld
        fields = ["id", "slug", "name"]
        depth = 1
