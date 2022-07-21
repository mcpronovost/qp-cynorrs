from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.world.models import (
    qpWorld
)


class qpWorldSerializer(serializers.ModelSerializer):
    count_players = serializers.ReadOnlyField(default=0)
    count_heros = serializers.ReadOnlyField(default=0)
    count_chapters = serializers.ReadOnlyField(default=0, allow_null=False)
    count_messages = serializers.ReadOnlyField(default=0)

    class Meta:
        model = qpWorld
        fields = [
            "id", "name", "description",
            "creator", "administrators", "moderators",
            "count_players", "count_heros",
            "count_chapters",  "count_messages",
            "is_active"
        ]
