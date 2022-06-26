from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from qp.player.models import qpPlayer


class qpPingView(APIView):

    def get(self, request, format=None):
        if not request.user.is_authenticated:
            return Response({"valid": True})
        try:
            player = request.user.player
        except ObjectDoesNotExist:
            player = qpPlayer.objects.create(
                user=request.user
            )
        # ===---
        player_data = {
            "name": player.name
        }
        # ===---
        return Response({
            "player": player_data,
            "valid": True
        })

