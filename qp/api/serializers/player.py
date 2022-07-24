from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.player.models import qpPlayer


class qpPlayerMeSerializer(serializers.ModelSerializer):

    class Meta:
        model = qpPlayer
        fields = ["id", "playername", "avatar", "banner"]
        depth = 2