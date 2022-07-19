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

from qp.forum.models import (
    qpForumTerritory,
    qpForumSector
)


class qpGameActionTravelView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        player = request.user.player
        # ===---
        travellers = request.POST.get("travellers", None)
        territory = request.POST.get("territory", None)
        sector = request.POST.get("sector", None)
        # ===---
        if travellers is None or territory is None:
            return Response({"valid": False}, status=status.HTTP_400_BAD_REQUEST)
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
                territoire = qpForumTerritory.objects.get(
                    pk=int(territory)
                )
                if sector is not None:
                    secteur = qpForumSector.objects.get(
                        pk=int(sector)
                    )
            except ObjectDoesNotExist:
                return Response({"valid": False}, status=status.HTTP_400_BAD_REQUEST)
            # ===---
            cooldown_time = timedelta(hours=1)
            if hero.geo and hero.geo != "":
                hero_geo = json.loads(hero.geo)
                if hero_geo["territory"] == territoire.pk:
                    cooldown_time = timedelta(hours=1)
                elif hero_geo["zone"] == territoire.zone.pk:
                    cooldown_time = timedelta(hours=2)
                else:
                    cooldown_time = timedelta(hours=3)
            # ===---
            hero.geo = json.dumps({
                "world": territoire.zone.world.pk,
                "zone": territoire.zone.pk,
                "territory": territoire.pk,
                "section": secteur.pk if sector is not None and secteur is not None else None,
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
