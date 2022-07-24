from django.core.exceptions import BadRequest

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

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
    qpForumMessageCreateSerializer
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

class qpForumChapterMessageCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpForumMessageCreateSerializer
