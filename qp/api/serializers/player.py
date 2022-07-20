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
        if User.objects.filter(username=validated_data["username"]).count():
            raise serializers.ValidationError({"username": "A user with that username already exists."})
        if User.objects.filter(email=validated_data["email"]).count():
            raise serializers.ValidationError({"email": "A user with that email already exists."})
        if qpPlayer.objects.filter(playername=validated_data["playername"]).count():
            raise serializers.ValidationError({"playername": "A player with that playername already exists."})
        if len(validated_data["password"]) < 6:
            raise serializers.ValidationError({"password": "That password is too short."})
        user = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"]
        )
        qpPlayer.objects.create(
            user=user,
            playername=validated_data["playername"]
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
