from zoneinfo import ZoneInfo

from django.template.defaultfilters import date as _date

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from qp.world.models import (
    qpWorld,
    qpWorldZone,
    qpWorldTerritory,
    qpWorldSector,
    qpWorldChapter,
    qpWorldMessage
)

from qp.world.utils import (
    get_perpage
)


class qpWorldsView(APIView):

    def get(self, request):
        # ===---
        try:
            worlds = qpWorld.objects.all()
        except Exception as e:
            print("Error on qpWorldsView > get : ", e)
            return Response({"valid": False}, status=status.HTTP_400_BAD_REQUEST)
        # ===---
        worlds_data = []
        for world in worlds:
            world_data = qpWorldView.get_world(request, world.pk)
            worlds_data.append(world_data)
        # ===---
        return Response({
            "worlds": worlds_data,
            "valid": True
        })


class qpWorldView(APIView):
    permission_classes = [AllowAny]

    def get_world(request, pk, singleton):
        """
        Returns data of a given world.
        Uses the singleton's keyword to determine if zones should be added.
        
        :param request: (any) django request.
        :param pk: (int) primary key of qpWorld.
        :param singleton: (str) keyword where the data is showed ("index", "zone", etc.)

        :return: (object) data of world with zones if applicable.
        """
        # ===---
        try:
            world = qpWorld.objects.get(
                pk=pk
            )
        except Exception as e:
            print("Error on qpWorldView > get_world : ", e)
            return
        # ===---
        world_data = {
            "id": int(world.pk),
            "name": str(world.name),
            "slug": str(world.slug),
            "stylesheet": world.stylesheet,
            "count_chapters": world.count_chapters,
            "count_messages": world.count_messages,
            "copyright": {
                "year": "%s-%s" % (world.created_at.year, world.updated_at.year) if world.created_at.year != world.updated_at.year else str(world.updated_at.year)
            }
        }
        if singleton in ["index"]:
            world_data["zones"] = []
            # ===--- zones
            for zone in world.zones.all():
                zone_data = qpWorldView.get_zone(request, zone.pk, singleton)
                world_data["zones"].append(zone_data)
        # ===---
        return world_data

    def get_zone(request, pk, singleton):
        """
        Returns data of a given zone.
        Uses the singleton's keyword to determine if territories should be added.
        
        :param request: (any) django request.
        :param pk: (int) primary key of qpWorldZone.
        :param singleton: (str) keyword where the data is showed ("index", "zone", etc.)

        :return: (object) data of zone with territories if applicable.
        """
        # ===---
        try:
            zone = qpWorldZone.objects.get(
                pk=pk
            )
        except Exception as e:
            print("Error on qpWorldView > get_zone : ", e)
            return
        # ===---
        zone_data = {
            "id": zone.pk,
            "name": str(zone.name),
            "description": zone.description,
            "world": zone.world.pk,
            "count_chapters": zone.count_chapters,
            "count_messages": zone.count_messages
        }
        if singleton in ["index", "zone"]:
            zone_data["territories"] = []
            # ===--- territories
            for territory in zone.territories.all():
                territory_data = qpWorldView.get_territory(request, territory.pk, singleton)
                zone_data["territories"].append(territory_data)
        # ===---
        return zone_data

    def get_territory(request, pk, singleton):
        """
        Returns data of a given territory.
        Uses the singleton's keyword to determine if sectors and chapters should be added.
        
        :param request: (any) django request.
        :param pk: (int) primary key of qpWorldTerritory.
        :param singleton: (str) keyword where the data is showed ("index", "zone", etc.)

        :return: (object) data of territory with sectors and chapters if applicable.
        """
        # ===---
        try:
            territory = qpWorldTerritory.objects.get(
                pk=pk
            )
        except Exception as e:
            print("Error on qpWorldView > get_territory : ", e)
            return
        # ===---
        territory_data = {
            "id": territory.pk,
            "name": str(territory.name),
            "description": territory.description,
            "world": territory.zone.world.pk,
            "zone": territory.zone.pk,
            "count_chapters": territory.count_chapters,
            "count_messages": territory.count_messages,
            "colour": territory.colour,
            "flexbasis": str(territory.flexbasis),
            "last_message": {
                "title": territory.last_message.chapter.title,
                "author": {
                    "initials": territory.last_message.author.initials,
                    "avatar": territory.last_message.author.avatar.url if territory.last_message.author.avatar else None
                } if territory.last_message.author else None,
                "date": _date(territory.last_message.updated_at.astimezone(ZoneInfo("America/Toronto")), "d F Y H:i"),
                "routes": {
                    "chapter": territory.last_message.chapter.get_route(),
                    "message": territory.last_message.get_route(request, True)
                }
            } if territory.last_message else None
        }
        if singleton in ["territory"]:
            # ===--- sectors
            territory_data["sectors"] = []
            for sector in territory.sectors.all():
                sector_data = qpWorldView.get_sector(request, sector.pk, singleton)
                territory_data["sectors"].append(sector_data)
        if singleton in ["territory"]:
            # ===--- chapters
            perpage = get_perpage(request, "chapters")
            territory_data["chapters"] = []
            territory_data["perpage_chapters"] = perpage
            page = request.GET.get("page", 1)
            offset = (int(page) * perpage) - perpage
            chapters = territory.chapters.filter(
                sector=None
            )[offset:(offset+perpage)]
            for chapter in chapters:
                chapter_data = qpWorldView.get_chapter(request, chapter.pk, singleton)
                territory_data["chapters"].append(chapter_data)
        # ===---
        return territory_data

    def get_sector(request, pk, singleton):
        """
        Returns data of a given sector.
        Uses the singleton's keyword to determine if chapters should be added.
        
        :param request: (any) django request.
        :param pk: (int) primary key of qpWorldSector.
        :param singleton: (str) keyword where the data is showed ("index", "zone", etc.)

        :return: (object) data of sector with chapters if applicable.
        """
        # ===---
        try:
            sector = qpWorldSector.objects.get(
                pk=pk
            )
        except Exception as e:
            print("Error on qpWorldView > get_sector : ", e)
            return
        # ===---
        sector_data = {
            "id": sector.pk,
            "name": str(sector.name),
            "description": sector.description,
            "world": sector.territory.zone.world.pk,
            "zone": sector.territory.zone.pk,
            "territory": sector.territory.pk,
            "count_chapters": sector.count_chapters,
            "count_messages": sector.count_messages,
            "colour": sector.colour,
            "flexbasis": str(sector.flexbasis)
        }
        if singleton in ["sector"]:
            perpage = get_perpage(request, "chapters")
            sector_data["chapters"] = []
            sector_data["perpage_chapters"] = perpage
            page = request.GET.get("page", 1)
            offset = (int(page) * perpage) - perpage
            chapters = sector.chapters.all()[offset:(offset+perpage)]
            # ===--- chapters
            for chapter in chapters:
                chapter_data = qpWorldView.get_chapter(request, chapter.pk, singleton)
                sector_data["chapters"].append(chapter_data)
        # ===---
        return sector_data

    def get_chapter(request, pk, singleton):
        """
        Returns data of a given chapter.
        Uses the singleton's keyword to determine if messages should be added.
        
        :param request: (any) django request.
        :param pk: (int) primary key of qpWorldChapter.
        :param singleton: (str) keyword where the data is showed ("index", "zone", etc.)

        :return: (object) data of chapters with messages if applicable.
        """
        # ===---
        try:
            chapter = qpWorldChapter.objects.get(
                pk=pk
            )
        except Exception as e:
            print("Error on qpWorldView > get_chapter : ", e)
            return
        # ===---
        chapter_data = {
            "id": chapter.pk,
            "title": str(chapter.title),
            "world": chapter.territory.zone.world.pk,
            "zone": chapter.territory.zone.pk,
            "territory": chapter.territory.pk,
            "sector": chapter.sector.pk if chapter.sector else None,
            "count_messages": chapter.count_messages,
            "author": {
                "avatar": chapter.author.avatar.url if chapter.author.avatar else None
            } if chapter.author else None,
            "last_message": {
                "author": {
                    "initials": chapter.last_message.author.initials,
                    "avatar": chapter.last_message.author.avatar.url if chapter.last_message.author.avatar else None
                } if chapter.last_message.author else None,
                "date": _date(chapter.last_message.updated_at.astimezone(ZoneInfo("America/Toronto")), "d F Y H:i")
            } if chapter.last_message else None
        }
        if singleton in ["chapter"]:
            perpage = get_perpage(request, "messages")
            chapter_data["messages"] = []
            chapter_data["perpage_messages"] = perpage
            page = request.GET.get("page", 1)
            offset = (int(page) * perpage) - perpage
            messages = chapter.messages.all()[offset:(offset+perpage)]
            # ===--- messages
            for message in messages:
                message_data = qpWorldView.get_message(request, message.pk, singleton)
                chapter_data["messages"].append(message_data)
        # ===---
        return chapter_data

    def get_message(request, pk, singleton):
        """
        Returns data of a given message.
        
        :param request: (any) django request.
        :param pk: (int) primary key of qpWorldMessage.
        :param singleton: (str) keyword where the data is showed ("index", "zone", etc.)

        :return: (object) data of chapters.
        """
        # ===---
        try:
            message = qpWorldMessage.objects.get(pk=pk)
        except Exception as e:
            print("Error on qpWorldView > get_message : ", e)
            return
        # ===---
        message_data = {
            "id": message.pk,
            "world": message.chapter.territory.zone.world.pk,
            "zone": message.chapter.territory.zone.pk,
            "territory": message.chapter.territory.pk,
            "sector": message.chapter.sector.pk if message.chapter.sector else None,
            "author": {
                "id": message.author.pk,
                "name": message.author.name
            } if message.author is not None else None,
            "text": message.text
        }
        # ===---
        return message_data

    def get(self, request, pk):
        # ===---
        world_data = qpWorldView.get_world(request, pk, "index")
        # ===---
        return Response({
            "world": world_data,
            "valid": True
        })


class qpWorldZoneView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        # ===---
        zone_data = qpWorldView.get_zone(request, pk, "zone")
        world_data = qpWorldView.get_world(request, zone_data["world"], "zone")
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
        territory_data = qpWorldView.get_territory(request, pk, "territory")
        zone_data = qpWorldView.get_zone(request, territory_data["zone"], "territory")
        world_data = qpWorldView.get_world(request, zone_data["world"], "territory")
        # ===---
        return Response({
            "world": world_data,
            "zone": zone_data,
            "territory": territory_data,
            "valid": True
        })


class qpWorldSectorView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        # ===---
        sector_data = qpWorldView.get_sector(request, pk, "sector")
        territory_data = qpWorldView.get_territory(request, sector_data["territory"], "sector")
        zone_data = qpWorldView.get_zone(request, sector_data["zone"], "sector")
        world_data = qpWorldView.get_world(request, sector_data["world"], "sector")
        # ===---
        return Response({
            "world": world_data,
            "zone": zone_data,
            "territory": territory_data,
            "sector": sector_data,
            "valid": True
        })


class qpWorldChapterView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        # ===---
        chapter_data = qpWorldView.get_chapter(request, pk, "chapter")
        sector_data = qpWorldView.get_sector(request, chapter_data["sector"], "chapter")
        territory_data = qpWorldView.get_territory(request, chapter_data["territory"], "chapter")
        zone_data = qpWorldView.get_zone(request, chapter_data["zone"], "chapter")
        world_data = qpWorldView.get_world(request, chapter_data["world"], "chapter")
        # ===---
        return Response({
            "world": world_data,
            "zone": zone_data,
            "territory": territory_data,
            "sector": sector_data,
            "chapter": chapter_data,
            "valid": True
        })
