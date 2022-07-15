from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from qp.world.models import (
    qpWorld,
    qpWorldZone,
    qpWorldTerritoty,
    qpWorldSector
)


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

    def get_world(request, pk):
        # ===---
        try:
            world = qpWorld.objects.get(
                pk=pk
            )
        except Exception as e:
            print("Error on qpWorldView > get_world : ", e)
            return Response({"valid": False}, status=status.HTTP_400_BAD_REQUEST)
        # ===---
        world_data = {
            "id": int(world.pk),
            "name": str(world.name),
            "slug": str(world.slug),
            "stylesheet": world.stylesheet,
            "zones": []
        }
        # ===--- zones
        for zone in world.zones.all():
            zone_data = qpWorldView.get_zone(request, zone.pk)
            world_data["zones"].append(zone_data)
        # ===---
        return world_data

    def get_zone(request, pk):
        # ===---
        try:
            zone = qpWorldZone.objects.get(
                pk=pk
            )
        except Exception as e:
            print("Error on qpWorldView > get_zone : ", e)
            return Response({"valid": False}, status=status.HTTP_400_BAD_REQUEST)
        # ===---
        zone_data = {
            "id": zone.pk,
            "name": str(zone.name),
            "description": zone.description,
            "world": zone.world.pk,
            "territories": []
        }
        # ===--- territories
        for territory in zone.territories.all():
            territory_data = qpWorldView.get_territory(request, territory.pk)
            zone_data["territories"].append(territory_data)
        # ===---
        return zone_data

    def get_territory(request, pk):
        # ===---
        try:
            territory = qpWorldTerritoty.objects.get(
                pk=pk
            )
        except Exception as e:
            print("Error on qpWorldView > get_territory : ", e)
            return Response({"valid": False}, status=status.HTTP_400_BAD_REQUEST)
        # ===---
        territory_data = {
            "id": territory.pk,
            "name": str(territory.name),
            "description": territory.description,
            "world": territory.zone.world.pk,
            "zone": territory.zone.pk,
            "flexbasis": str(territory.flexbasis),
            "sectors": []
        }
        # ===--- sectors
        for sector in territory.sectors.all():
            sector_data = qpWorldView.get_sector(request, sector.pk)
            territory_data["sectors"].append(sector_data)
        # ===---
        return territory_data

    def get_sector(request, pk):
        # ===---
        try:
            sector = qpWorldSector.objects.get(
                pk=pk
            )
        except Exception as e:
            print("Error on qpWorldView > get_sector : ", e)
            return Response({"valid": False}, status=status.HTTP_400_BAD_REQUEST)
        # ===---
        sector_data = {
            "id": sector.pk,
            "name": str(sector.name),
            "description": sector.description,
            "world": sector.territory.zone.world.pk,
            "zone": sector.territory.zone.pk,
            "territory": sector.territory.pk,
            "flexbasis": str(sector.flexbasis)
        }
        # ===---
        return sector_data

    def get(self, request, pk):
        # ===---
        world_data = qpWorldView.get_world(request, pk)
        # ===---
        return Response({
            "world": world_data,
            "valid": True
        })


class qpWorldZoneView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        # ===---
        zone_data = qpWorldView.get_zone(request, pk)
        world_data = qpWorldView.get_world(request, zone_data["world"])
        # ===---
        return Response({
            "world": world_data,
            "zone": zone_data,
            "valid": True
        })


class qpWorldTerritoryView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        # ===---
        territory_data = qpWorldView.get_territory(request, pk)
        zone_data = qpWorldView.get_zone(request, territory_data["zone"])
        world_data = qpWorldView.get_world(request, zone_data["world"])
        # ===---
        return Response({
            "world": world_data,
            "zone": zone_data,
            "territory": territory_data,
            "valid": True
        })
