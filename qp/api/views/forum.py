from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

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
    qpForumChapterSerializer
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

class qpForumChapterRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = qpForumChapterSerializer
    queryset = qpForumChapter.objects.all()
    lookup_field = "pk"
