from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from qp.world.models import qpWorld


class qpWorldsView(APIView):

    def get(self, request):
        worlds_data = [
            {
                "id": 0,
                "name": "Sagars",
                "zones": [
                    {
                        "id": 1,
                        "name": "Zone A",
                        "territories": [
                            {
                                "id": 2,
                                "name": "Territoire A-1",
                                "sectors": [
                                    {
                                        "id": 4,
                                        "name": "Secteur A-1-A"
                                    },
                                    {
                                        "id": 5,
                                        "name": "Secteur A-1-B"
                                    }
                                ]
                            },
                            {
                                "id": 3,
                                "name": "Territoire A-2",
                                "sectors": [
                                    {
                                        "id": 6,
                                        "name": "Secteur A-2-A"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
        # ===---
        return Response({
            "worlds": worlds_data,
            "valid": True
        })


class qpWorldView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        # ===---
        try:
            world = qpWorld.objects.get(
                pk=pk
            )
        except Exception as e:
            print("Error on qpWorldView > get : ", e)
            return Response({"valid": False}, status=status.HTTP_400_BAD_REQUEST)
        # ===---
        world_data = {
            "name": str(world.name),
            "stylesheet": world.stylesheet,
            "zones": []
        }
        # ===--- zones
        for zone in world.zones.all():
            zone_data = {
                "id": zone.pk,
                "name": str(zone.name),
                "territories": []
            }
            # ===--- territories
            for territory in zone.territories.all():
                territory_data = {
                    "id": territory.pk,
                    "name": str(territory.name),
                    "flexbasis": str(territory.flexbasis),
                    "sectors": []
                }
                # ===--- sectors
                for sector in territory.sectors.all():
                    sector_data = {
                        "id": sector.pk,
                        "name": str(sector.name),
                        "flexbasis": str(sector.flexbasis)
                    }
                    territory_data["sectors"].append(sector_data)
                # ===---
                zone_data["territories"].append(territory_data)
            # ===---
            world_data["zones"].append(zone_data)
        # ===---
        return Response({
            "world": world_data,
            "valid": True
        })

