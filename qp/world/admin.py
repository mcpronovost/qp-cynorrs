from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from qp.world.models import (
    qpWorld,
    qpWorldZone,
    qpWorldTerritory,
    qpWorldSector,
    qpWorldChapter,
    qpWorldMessage,
    qpWorldRace,
    qpWorldEthnicity,
    qpWorldNationality
)


@admin.register(qpWorld)
class qpWorldAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "creator"
    ]
    filter_horizontal = [
        "administrators",
        "moderators"
    ]

@admin.register(qpWorldZone)
class qpWorldZoneAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "ordering",
        "world"
    ]
    list_filter = [
        ("world", admin.RelatedOnlyFieldListFilter)
    ]

@admin.register(qpWorldTerritory)
class qpWorldTerritoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "ordering",
        "zone",
        "get_world"
    ]
    list_filter = [
        ("zone__world", admin.RelatedOnlyFieldListFilter),
        ("zone", admin.RelatedOnlyFieldListFilter)
    ]

    def get_world(self, obj):
        if obj.zone:
            return obj.zone.world
        return None
    get_world.short_description = str(_("World"))

@admin.register(qpWorldSector)
class qpWorldSectorAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "ordering",
        "territory",
        "get_zone",
        "get_world"
    ]
    list_filter = [
        ("territory__zone__world", admin.RelatedOnlyFieldListFilter),
        ("territory__zone", admin.RelatedOnlyFieldListFilter),
        ("territory", admin.RelatedOnlyFieldListFilter)
    ]

    def get_world(self, obj):
        if obj.territory and obj.territory.zone:
            return obj.territory.zone.world
        return None
    get_world.short_description = str(_("World"))

    def get_zone(self, obj):
        if obj.territory:
            return obj.territory.zone
        return None
    get_zone.short_description = str(_("Zone"))

@admin.register(qpWorldChapter)
class qpWorldChapterAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "get_author",
        "get_messages",
        "sector",
        "territory",
        "get_zone",
        "get_world"
    ]
    list_filter = [
        ("territory__zone__world", admin.RelatedOnlyFieldListFilter),
        ("territory__zone", admin.RelatedOnlyFieldListFilter),
        ("territory", admin.RelatedOnlyFieldListFilter),
        ("sector", admin.RelatedOnlyFieldListFilter),
        ("author__player", admin.RelatedOnlyFieldListFilter),
        ("author", admin.RelatedOnlyFieldListFilter)
    ]

    def get_author(self, obj):
        if obj.author is not None and obj.author.player is not None:
            return "%s (%s)" % (
                str(obj.author),
                str(obj.author.player)
            )
        return str(obj.author)
    get_author.short_description = str(_("Author"))

    def get_messages(self, obj):
        return "%s" % (
            obj.count_messages
        )
    get_messages.short_description = str(_("Messages"))

    def get_world(self, obj):
        if obj.territory and obj.territory.zone:
            return obj.territory.zone.world
        return None
    get_world.short_description = str(_("World"))

    def get_zone(self, obj):
        if obj.territory:
            return obj.territory.zone
        return None
    get_zone.short_description = str(_("Zone"))

@admin.register(qpWorldMessage)
class qpWorldMessageAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "chapter",
        "get_author",
        "created_at",
        "get_sector",
        "get_territory",
        "get_zone",
        "get_world"
    ]
    list_filter = [
        ("chapter__territory__zone__world", admin.RelatedOnlyFieldListFilter),
        ("chapter__territory__zone", admin.RelatedOnlyFieldListFilter),
        ("chapter__territory", admin.RelatedOnlyFieldListFilter),
        ("chapter__sector", admin.RelatedOnlyFieldListFilter),
        ("author__player", admin.RelatedOnlyFieldListFilter),
        ("author", admin.RelatedOnlyFieldListFilter)
    ]

    def get_author(self, obj):
        if obj.author is not None and obj.author.player is not None:
            return "%s (%s)" % (
                str(obj.author),
                str(obj.author.player)
            )
        return str(obj.author)
    get_author.short_description = str(_("Author"))

    def get_world(self, obj):
        if obj.chapter and obj.chapter.territory and obj.chapter.territory.zone:
            return obj.chapter.territory.zone.world
        return None
    get_world.short_description = str(_("World"))

    def get_zone(self, obj):
        if obj.chapter.territory:
            return obj.chapter.territory.zone
        return None
    get_zone.short_description = str(_("Zone"))

    def get_territory(self, obj):
        if obj.chapter.territory:
            return obj.chapter.territory.zone
        return None
    get_territory.short_description = str(_("Territory"))

    def get_sector(self, obj):
        if obj.chapter.sector:
            return obj.chapter.sector
        return None
    get_sector.short_description = str(_("Sector"))

@admin.register(qpWorldRace)
class qpWorldRaceAdmin(admin.ModelAdmin):
    pass

@admin.register(qpWorldEthnicity)
class qpWorldEthnicityAdmin(admin.ModelAdmin):
    pass

@admin.register(qpWorldNationality)
class qpWorldNationalityAdmin(admin.ModelAdmin):
    pass
