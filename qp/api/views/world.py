from zoneinfo import ZoneInfo

from django.db.models import Q
from django.template.defaultfilters import date as _date

from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
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

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            queryset = qpWorld.objects.filter(
                Q(visibility=0),
                is_active=True
            )
        else:
            player = self.request.user.player
            queryset = qpWorld.objects.filter(
                Q(creator=player) | (Q(visibility=0) | Q(visibility=6) | (
                    Q(visibility=2) & Q(administrators__in=[player])
                ) | (
                    Q(visibility=3) & (Q(administrators__in=[player]) | Q(moderators__in=[player]))
                ) | (
                    Q(visibility=4) & (Q(administrators__in=[player]) | Q(moderators__in=[player]) | (
                        Q(heros__in=player.heros.filter(is_active=True, is_valid=True))
                    ))
                ) | (
                    Q(visibility=5) & (Q(administrators__in=[player]) | Q(moderators__in=[player]) | (
                        Q(heros__in=player.heros.filter(is_active=True, is_valid=True))
                    ) | (
                        Q(heros__in=player.heros.filter(is_active=True))
                    ))
                ) & Q(is_active=True))
            )
        return queryset.distinct()


class qpWorldsCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = qpWorldSerializer

    def get_queryset(self):
        player = self.request.user.player
        queryset = qpWorld.objects.filter(
            Q(creator=player) | (Q(visibility=0) | Q(visibility=6) | (
                Q(visibility=2) & Q(administrators__in=[player])
            ) | (
                Q(visibility=3) & (Q(administrators__in=[player]) | Q(moderators__in=[player]))
            ) | (
                Q(visibility=4) & (Q(administrators__in=[player]) | Q(moderators__in=[player]) | (
                    Q(heros__in=player.heros.filter(is_active=True, is_valid=True))
                ))
            ) | (
                Q(visibility=5) & (Q(administrators__in=[player]) | Q(moderators__in=[player]) | (
                    Q(heros__in=player.heros.filter(is_active=True, is_valid=True))
                ) | (
                    Q(heros__in=player.heros.filter(is_active=True))
                ))
            ) & Q(is_active=True))
        )
        return queryset
