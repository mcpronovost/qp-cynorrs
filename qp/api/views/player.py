from django.core.exceptions import BadRequest

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from qp.player.models import (
    qpPlayer,
    qpPlayerHero
)

from qp.world.models import (
    qpWorld
)

from qp.api.serializers.player import (
    qpPlayerMeSerializer,
    qpPlayerMeHeroSerializer,
    qpPlayerMeWorldSerializer
)

from qp.api.serializers.world import (
    qpWorldNavSerializer
)


class qpPlayerMeRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpPlayerMeSerializer
    queryset = qpPlayer.objects.all()
    lookup_field = "pk"

    def get_object(self):
        try:
            return self.request.user.player
        except Exception as e:
            print("Error on qpPlayerRetrieveView : ", e)
        return None


class qpPlayerMeHerosListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpPlayerMeHeroSerializer
    queryset = qpPlayerHero.objects.all()
    pagination_class = None

    def get_queryset(self):
        queryset = self.request.user.player.heros.filter(
            is_active=True
        )
        return queryset


class qpPlayerMeWorldsListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpPlayerMeWorldSerializer
    queryset = qpWorld.objects.all()

    def get_queryset(self):
        queryset = self.request.user.player.creator_worlds.filter(
            is_active=True
        )
        return queryset
