from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from qp.forum.models import (
    qpForum,
    qpForumZone,
    qpForumTerritory,
    qpForumSector,
    qpForumChapter,
    qpForumMessage,
)


@admin.register(qpForum)
class qpForumAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "creator",
        "world"
    ]
    filter_horizontal = [
        "administrators",
        "moderators"
    ]

@admin.register(qpForumZone)
class qpForumZoneAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "ordering",
        "forum"
    ]
    list_filter = [
        ("forum", admin.RelatedOnlyFieldListFilter)
    ]

@admin.register(qpForumTerritory)
class qpForumTerritoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "ordering",
        "zone",
        "get_forum"
    ]
    list_filter = [
        ("zone__forum", admin.RelatedOnlyFieldListFilter),
        ("zone", admin.RelatedOnlyFieldListFilter)
    ]

    def get_forum(self, obj):
        if obj.zone:
            return obj.zone.forum
        return None
    get_forum.short_description = str(_("Forum"))

@admin.register(qpForumSector)
class qpForumSectorAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "ordering",
        "territory",
        "get_zone",
        "get_forum"
    ]
    list_filter = [
        ("territory__zone__forum", admin.RelatedOnlyFieldListFilter),
        ("territory__zone", admin.RelatedOnlyFieldListFilter),
        ("territory", admin.RelatedOnlyFieldListFilter)
    ]

    def get_forum(self, obj):
        if obj.territory and obj.territory.zone:
            return obj.territory.zone.forum
        return None
    get_forum.short_description = str(_("Forum"))

    def get_zone(self, obj):
        if obj.territory:
            return obj.territory.zone
        return None
    get_zone.short_description = str(_("Zone"))

@admin.register(qpForumChapter)
class qpForumChapterAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "get_author",
        "get_messages",
        "sector",
        "territory",
        "get_zone",
        "get_forum"
    ]
    list_filter = [
        ("territory__zone__forum", admin.RelatedOnlyFieldListFilter),
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

    def get_forum(self, obj):
        if obj.territory and obj.territory.zone:
            return obj.territory.zone.forum
        return None
    get_forum.short_description = str(_("Forum"))

    def get_zone(self, obj):
        if obj.territory:
            return obj.territory.zone
        return None
    get_zone.short_description = str(_("Zone"))

@admin.register(qpForumMessage)
class qpForumMessageAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "chapter",
        "get_author",
        "created_at",
        "get_sector",
        "get_territory",
        "get_zone",
        "get_forum"
    ]
    list_filter = [
        ("chapter__territory__zone__forum", admin.RelatedOnlyFieldListFilter),
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

    def get_forum(self, obj):
        if obj.chapter and obj.chapter.territory and obj.chapter.territory.zone:
            return obj.chapter.territory.zone.forum
        return None
    get_forum.short_description = str(_("Forum"))

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
