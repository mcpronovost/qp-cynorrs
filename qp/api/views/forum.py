from django.core.exceptions import BadRequest

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST

from qp.forum.models import (
    qpForum,
    qpForumZone,
    qpForumTerritory,
    qpForumSector,
    qpForumChapter,
    qpForumMessage,
    qpForumTrack
)

from qp.api.serializers.forum import (
    qpForumSerializer,
    qpForumZoneSerializer,
    qpForumTerritorySerializer,
    qpForumSectorSerializer,
    qpForumChapterSerializer,
    qpForumMessageSerializer,
    qpForumMessageEditSerializer,
    qpForumChapterCreateSerializer
)

class qpForumRetrieveView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = qpForumSerializer
    queryset = qpForum.objects.all()
    lookup_field = "pk"

class qpForumZoneRetrieveView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = qpForumZoneSerializer
    queryset = qpForumZone.objects.all()
    lookup_field = "pk"

class qpForumTerritoryRetrieveView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = qpForumTerritorySerializer
    queryset = qpForumTerritory.objects.all()
    lookup_field = "pk"

class qpForumSectorRetrieveView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = qpForumSectorSerializer
    queryset = qpForumSector.objects.all()
    lookup_field = "pk"

class qpForumChapterRetrieveView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = qpForumChapterSerializer
    queryset = qpForumChapter.objects.all()
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            instance = self.get_object()
            track, created = qpForumTrack.objects.get_or_create(
                player=request.user.player,
                chapter=instance
            )
            track.save()
        return self.retrieve(request, *args, **kwargs)

class qpForumChapterMessagesListView(ListAPIView):
    model = qpForumMessage
    permission_classes = [AllowAny]
    serializer_class = qpForumMessageSerializer
    pagination_limit = "settings_perpage_messages"

    def get_queryset(self):
        pk = self.kwargs["pk"]
        queryset = self.model.objects.filter(
            chapter=pk
        )
        return queryset

class qpForumChapterCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpForumChapterCreateSerializer

class qpForumChapterMessageCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpForumMessageEditSerializer

class qpForumChapterMessageEditView(RetrieveUpdateDestroyAPIView):
    model = qpForumMessage
    permission_classes = [IsAuthenticated]
    serializer_class = qpForumMessageEditSerializer

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
            author = instance.author.player
            if player == author or player == instance.world.creator or player in instance.world.administrators.all() or player in instance.world.moderators.all():
                serializer = self.get_serializer(instance, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                if getattr(instance, "_prefetched_objects_cache", None):
                    instance._prefetched_objects_cache = {}
                return Response(serializer.data)
        except Exception as e:
            print("Error on qpForumChapterMessageEditView > patch : ", e)
        return Response(status=HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            player = request.user.player
            author = instance.author.player
            if player == author or player == instance.world.creator or player in instance.world.administrators.all():
                self.perform_destroy(instance)
                return Response(status=HTTP_204_NO_CONTENT)
        except Exception as e:
            print("Error on qpForumChapterMessageEditView > delete : ", e)
        return Response(status=HTTP_400_BAD_REQUEST)
