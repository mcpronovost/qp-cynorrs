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
    route = serializers.SerializerMethodField(source="get_route")

    class Meta:
        model = qpForumMessage
        fields = ["id", "author", "chapter", "text", "route", "created_at", "updated_at"]
        depth = 2
    
    def get_route(self, obj):
        return obj.get_route(self.context["request"])


class qpForumChapterSerializer(serializers.ModelSerializer):
    messages = qpForumMessageSerializer(many=True)
    count_messages = serializers.ReadOnlyField(default=0)
    route = serializers.ReadOnlyField(source="get_route")

    class Meta:
        model = qpForumChapter
        fields = "__all__"
        depth = 1


class qpForumChapterListSerializer(serializers.ModelSerializer):
    count_messages = serializers.ReadOnlyField(default=0)
    last_message = qpForumMessageSerializer()
    route = serializers.ReadOnlyField(source="get_route")

    class Meta:
        model = qpForumChapter
        fields = "__all__"
        depth = 2


class qpForumTerritorySerializer(serializers.ModelSerializer):
    count_sectors = serializers.ReadOnlyField(default=0)
    count_chapters = serializers.ReadOnlyField(default=0)
    count_messages = serializers.ReadOnlyField(default=0)
    chapters = qpForumChapterListSerializer(many=True)
    last_chapter = qpForumChapterListSerializer()
    
    class Meta:
        model = qpForumTerritory
        fields = ["id", "name", "description", "flexbasis", "colour", "ordering", "count_sectors", "count_chapters", "count_messages", "chapters", "zone", "last_chapter"]
        depth = 1


class qpForumTerritoryListSerializer(serializers.ModelSerializer):
    count_sectors = serializers.ReadOnlyField(default=0)
    count_chapters = serializers.ReadOnlyField(default=0)
    count_messages = serializers.ReadOnlyField(default=0)
    last_chapter = qpForumChapterListSerializer()
    
    class Meta:
        model = qpForumTerritory
        fields = ["id", "name", "description", "flexbasis", "colour", "ordering", "count_sectors", "count_chapters", "count_messages", "last_chapter", "zone"]
        depth = 1


class qpForumZoneSerializer(serializers.ModelSerializer):
    territories = qpForumTerritoryListSerializer(many=True, read_only=True)

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
        ret = super().to_representation(instance)
        forum = qpForum.objects.get(pk=ret.get("id"))
        forum_is_visible = forum.get_is_visible(self.context["request"])
        world_is_visible = forum.world.get_is_visible(self.context["request"])
        if world_is_visible and forum_is_visible:
            return ret
        raise PermissionDenied()
