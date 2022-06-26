from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.player.models import qpPlayer


User = get_user_model()


class qpPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class qpPlayerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {
            "email": {"write_only": True},
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"]
        )
        qpPlayer.objects.create(
            user=user
        )
        return user


class qpPlayerLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError(_("Invalid details."))
