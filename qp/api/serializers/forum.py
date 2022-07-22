from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from qp.forum.models import (
    qpForum,
    qpForumZone,
    qpForumTerritory,
    qpForumChapter,
    qpForumMessage
)


class qpForumMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = qpForumMessage
        fields = ["id", "author", "chapter", "text", "created_at", "updated_at"]
        depth = 1


class qpForumChapterSerializer(serializers.ModelSerializer):
    count_chapters = serializers.ReadOnlyField(default=0, allow_null=False)
    count_messages = serializers.ReadOnlyField(default=0)
    last_message = qpForumMessageSerializer()
    class Meta:
        model = qpForumChapter
        fields = "__all__"
        depth = 1


class qpForumTerritorySerializer(serializers.ModelSerializer):
    count_chapters = serializers.ReadOnlyField(default=0, allow_null=False)
    count_messages = serializers.ReadOnlyField(default=0)
    chapters = qpForumChapterSerializer(many=True)
    last_message = qpForumMessageSerializer()
    class Meta:
        model = qpForumTerritory
        fields = ["id", "name", "description", "flexbasis", "colour", "ordering", "count_chapters", "count_messages", "chapters", "zone", "last_message"]
        depth = 1


class qpForumZoneSerializer(serializers.ModelSerializer):
    territories = qpForumTerritorySerializer(many=True, read_only=True)
    class Meta:
        model = qpForumZone
        fields = ["id", "name", "description", "ordering", "territories"]
        depth = 1


class qpForumSerializer(serializers.ModelSerializer):
    zones = qpForumZoneSerializer(many=True, read_only=True)
    class Meta:
        model = qpForum
        fields = ["id", "name", "visibility", "is_active", "zones"]
        depth = 1

    def to_representation(self, instance):
        ret = super(qpForumSerializer, self).to_representation(instance)
        forum = qpForum.objects.get(pk=ret.get("id"))
        forum_is_visible = forum.get_is_visible(self.context["request"])
        world_is_visible = forum.world.get_is_visible(self.context["request"])
        if world_is_visible and forum_is_visible:
            return ret
        raise PermissionDenied()
