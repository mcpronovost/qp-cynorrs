import base64
import json
from datetime import timedelta

from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from qp.api.views.player import (
    qpPlayerView
)

from qp.world.models import (
    qpWorldSector
)


class qpGameActionTravelView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        player = request.user.player
        # ===---
        travellers = request.POST.get("travellers", None)
        sector = request.POST.get("sector", None)
        # ===---
        if travellers is not None and sector is not None:
            try:
                all_travellers = json.loads(base64.b64decode(travellers).decode("utf-8"))
            except Exception:
                return Response({"valid": False}, status=status.HTTP_400_BAD_REQUEST)
            for traveller in all_travellers:
                try:
                    hero = player.heros.get(
                        pk=int(traveller["id"]),
                        player=player,
                        world=int(traveller["world"]),
                        is_active=True
                    )
                    secteur = qpWorldSector.objects.get(
                        pk=int(sector)
                    )
                except ObjectDoesNotExist:
                    return Response({"valid": False}, status=status.HTTP_400_BAD_REQUEST)
                # ===---
                cooldown_time = timedelta(hours=1)
                if hero.geo and hero.geo != "":
                    hero_geo = json.loads(hero.geo)
                    if hero_geo["territory"] == secteur.territory.pk:
                        cooldown_time = timedelta(hours=1)
                    elif hero_geo["zone"] == secteur.territory.zone.pk:
                        cooldown_time = timedelta(hours=2)
                    else:
                        cooldown_time = timedelta(hours=3)
                # ===---
                hero.geo = json.dumps({
                    "world": secteur.territory.zone.world.pk,
                    "zone": secteur.territory.zone.pk,
                    "territory": secteur.territory.pk,
                    "section": secteur.pk,
                    "cooldown": (timezone.now() + cooldown_time).timestamp()
                })
                hero.save()
        # ===---
        heros_data = qpPlayerView.get_heros(None, player)
        # ===---
        return Response({
            "heros": heros_data,
            "valid": True
        })
