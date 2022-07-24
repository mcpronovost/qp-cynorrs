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
    qpForumMessage
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

class qpForumRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = qpForumSerializer
    queryset = qpForum.objects.all()
    lookup_field = "pk"

class qpForumZoneRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = qpForumZoneSerializer
    queryset = qpForumZone.objects.all()
    lookup_field = "pk"

class qpForumTerritoryRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = qpForumTerritorySerializer
    queryset = qpForumTerritory.objects.all()
    lookup_field = "pk"

class qpForumSectorRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = qpForumSectorSerializer
    queryset = qpForumSector.objects.all()
    lookup_field = "pk"

class qpForumChapterRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = qpForumChapterSerializer
    queryset = qpForumChapter.objects.all()
    lookup_field = "pk"

class qpForumChapterMessagesListAPIView(ListAPIView):
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

class qpForumChapterCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpForumChapterCreateSerializer

class qpForumChapterMessageCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpForumMessageEditSerializer

class qpForumChapterMessageEditAPIView(RetrieveUpdateDestroyAPIView):
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
            print("Error on qpForumChapterMessageEditAPIView > patch : ", e)
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
            print("Error on qpForumChapterMessageEditAPIView > delete : ", e)
        return Response(status=HTTP_400_BAD_REQUEST)
