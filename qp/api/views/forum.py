
from django.db.models import Q

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from qp.forum.models import (
    qpForum,
    qpForumZone,
    qpForumTerritory
)

from qp.api.serializers.forum import (
    qpForumSerializer,
    qpForumZoneSerializer,
    qpForumTerritorySerializer
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
