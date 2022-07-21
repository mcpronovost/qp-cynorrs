from collections import OrderedDict
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.forum.models import (
    qpForum,
    qpForumZone
)


class qpForumZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = qpForumZone
        fields = [
            "id",
            "name",
            "description"
        ]


class qpForumSerializer(serializers.ModelSerializer):
    zones = qpForumZoneSerializer(many=True, read_only=True)
    class Meta:
        model = qpForum
        fields = [
            "id",
            "name",
            "zones",
            "visibility",
            "is_active"
        ]

    def to_representation(self, instance):
        ret = super(qpForumSerializer, self).to_representation(instance)
        try:
            visibility = ret.get("visibility")
            is_active = ret.get("is_active", False)
            if not self.context["request"].user.is_authenticated:
                if is_active and visibility == 0:
                    return ret
            else:
                forum = qpForum.objects.get(pk=ret.get("id"))
                player = self.context["request"].user.player
                if forum.world.creator == player or (
                    (is_active and (
                        visibility == 0 or visibility == 6 or (
                            visibility == 2 and player in forum.world.administrators.all()
                        ) or (
                            visibility == 3 and (player in forum.world.administrators.all() or player in forum.world.moderators.all())
                        ) or (
                            visibility == 4 and (
                                player in forum.world.administrators.all() or 
                                player in forum.world.moderators.all() or 
                                player.heros.filter(world=forum.world, is_valid=True, is_active=True).count()
                            )
                        ) or (
                            visibility == 5 and (
                                player in forum.world.administrators.all() or 
                                player in forum.world.moderators.all() or 
                                player.heros.filter(world=forum.world, is_active=True).count()
                            )
                        )
                    ))
                ):
                    return ret
        except:
            pass
        return OrderedDict()
