from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST

from qp.player.models import (
    qpPlayer,
    qpPlayerHero
)

from qp.world.models import (
    qpWorld
)

from qp.forum.models import (
    qpForum,
    qpForumZone,
    qpForumTerritory,
    qpForumSector
)

from qp.api.serializers.player import (
    qpPlayerMeSerializer,
    qpPlayerMeHeroSerializer,
    qpPlayerMeCharactersHerosListSerializer,
    qpPlayerMeCharactersHeroSerializer,
    qpPlayerMeWorldListSerializer,
    qpPlayerMeWorldSerializer,
    qpPlayerMeWorldForumSerializer,
    qpPlayerMeWorldForumZoneEditSerializer,
    qpPlayerMeWorldForumTerritoryEditSerializer,
    qpPlayerMeWorldForumSectorEditSerializer
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


class qpPlayerMeCharactersHerosListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpPlayerMeCharactersHerosListSerializer
    queryset = qpPlayerHero.objects.all()

    def get_queryset(self):
        try:
            return self.request.user.player.heros.all()
        except Exception as e:
            print("Error on qpPlayerMeCharactersHerosListView : ", e)
        return None


class qpPlayerMeCharactersRetrieveView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpPlayerMeCharactersHeroSerializer
    queryset = qpPlayerHero.objects.all()
    lookup_field = "pk"

    def get_queryset(self):
        try:
            return self.request.user.player.heros.filter(
                pk=int(self.kwargs.get("pk"))
            )
        except Exception as e:
            print("Error on qpPlayerMeCharactersRetrieveView : ", e)
        return None


class qpPlayerMeWorldsListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpPlayerMeWorldListSerializer
    queryset = qpWorld.objects.all()

    def get_queryset(self):
        queryset = self.request.user.player.creator_worlds.all()
        return queryset


class qpPlayerMeWorldRetrieveView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpPlayerMeWorldSerializer
    queryset = qpWorld.objects.all()
    lookup_field = "pk"

    def get_queryset(self):
        try:
            return self.request.user.player.creator_worlds.filter(
                pk=int(self.kwargs.get("pk"))
            )
        except Exception as e:
            print("Error on qpPlayerMeWorldRetrieveView : ", e)
        return None


class qpPlayerMeWorldForumRetrieveView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpPlayerMeWorldForumSerializer
    queryset = qpForum.objects.all()
    lookup_field = "pk"

    def get_queryset(self):
        try:
            return qpForum.objects.filter(
                pk=int(self.kwargs.get("pk")),
                world__creator=self.request.user.player
            )
        except Exception as e:
            print("Error on qpPlayerMeWorldForumRetrieveView : ", e)
        return None


class qpPlayerMeWorldForumZoneCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpPlayerMeWorldForumZoneEditSerializer


class qpPlayerMeWorldForumZoneEditView(RetrieveUpdateDestroyAPIView):
    model = qpForumZone
    permission_classes = [IsAuthenticated]
    serializer_class = qpPlayerMeWorldForumZoneEditSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        queryset = self.model.objects.filter(
            pk=pk
        )
        return queryset

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            player = request.user.player
            if player == instance.forum.world.creator or player in instance.forum.world.administrators.all():
                serializer = self.get_serializer(instance, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                if getattr(instance, "_prefetched_objects_cache", None):
                    instance._prefetched_objects_cache = {}
                return Response(serializer.data)
        except Exception as e:
            print("Error on qpPlayerMeWorldForumZoneEditView > patch : ", e)
        return Response(status=HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            player = request.user.player
            if player == instance.forum.world.creator or player in instance.forum.world.administrators.all():
                self.perform_destroy(instance)
                return Response(status=HTTP_204_NO_CONTENT)
        except Exception as e:
            print("Error on qpPlayerMeWorldForumZoneEditView > delete : ", e)
        return Response(status=HTTP_400_BAD_REQUEST)


class qpPlayerMeWorldForumTerritoryCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpPlayerMeWorldForumTerritoryEditSerializer


class qpPlayerMeWorldForumTerritoryEditView(RetrieveUpdateDestroyAPIView):
    model = qpForumTerritory
    permission_classes = [IsAuthenticated]
    serializer_class = qpPlayerMeWorldForumTerritoryEditSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        queryset = self.model.objects.filter(
            pk=pk
        )
        return queryset

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            player = request.user.player
            if player == instance.zone.forum.world.creator or player in instance.zone.forum.world.administrators.all():
                serializer = self.get_serializer(instance, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                if getattr(instance, "_prefetched_objects_cache", None):
                    instance._prefetched_objects_cache = {}
                return Response(serializer.data)
        except Exception as e:
            print("Error on qpPlayerMeWorldForumTerritoryEditView > patch : ", e)
        return Response(status=HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            player = request.user.player
            if player == instance.zone.forum.world.creator or player in instance.zone.forum.world.administrators.all():
                self.perform_destroy(instance)
                return Response(status=HTTP_204_NO_CONTENT)
        except Exception as e:
            print("Error on qpPlayerMeWorldForumTerritoryEditView > delete : ", e)
        return Response(status=HTTP_400_BAD_REQUEST)


class qpPlayerMeWorldForumSectorCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpPlayerMeWorldForumSectorEditSerializer


class qpPlayerMeWorldForumSectorEditView(RetrieveUpdateDestroyAPIView):
    model = qpForumSector
    permission_classes = [IsAuthenticated]
    serializer_class = qpPlayerMeWorldForumSectorEditSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        queryset = self.model.objects.filter(
            pk=pk
        )
        return queryset

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            player = request.user.player
            if player == instance.territory.zone.forum.world.creator or player in instance.territory.zone.world.administrators.all():
                serializer = self.get_serializer(instance, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                if getattr(instance, "_prefetched_objects_cache", None):
                    instance._prefetched_objects_cache = {}
                return Response(serializer.data)
        except Exception as e:
            print("Error on qpPlayerMeWorldForumSectorEditView > patch : ", e)
        return Response(status=HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            player = request.user.player
            if player == instance.territory.zone.world.creator or player in instance.territory.zone.world.administrators.all():
                self.perform_destroy(instance)
                return Response(status=HTTP_204_NO_CONTENT)
        except Exception as e:
            print("Error on qpPlayerMeWorldForumSectorEditView > delete : ", e)
        return Response(status=HTTP_400_BAD_REQUEST)
