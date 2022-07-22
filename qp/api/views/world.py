from zoneinfo import ZoneInfo

from django.db.models import Q
from django.template.defaultfilters import date as _date

from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from qp.world.models import (
    qpWorld
)

from qp.api.serializers.world import (
    qpWorldSerializer
)


class qpWorldsListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = qpWorldSerializer
    # pagination_limit = "settings_perpage_chapters"


class qpWorldsCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpWorldSerializer


class qpWorldsRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = qpWorldSerializer
    queryset = qpWorld.objects.all()
    lookup_field = "slug"
