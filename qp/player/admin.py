from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from qp.player.models import (
    qpPlayer,
    qpPlayerHero,
    qpPlayerCompanion
)

class qpPlayerHeroInline(admin.StackedInline):
    model = qpPlayerHero
    extra = 0

class qpPlayerCompanionInline(admin.StackedInline):
    model = qpPlayerCompanion
    extra = 0


@admin.register(qpPlayer)
class qpPlayerAdmin(admin.ModelAdmin):
    list_display = [
        "playername",
        "user",
        "slug",
        "last_login",
        "updated_at"
    ]
    search_fields = [
        "playername",
        "user__username"
    ]
    raw_id_fields = ["user"]
    readonly_fields = ["slug"]
    fieldsets = [
        (_("Informations"), {
            "fields": [
                "user",
                ("playername", "slug"),
                "affinity"
            ]
        })
    ]
    inlines = [
        qpPlayerHeroInline,
        qpPlayerCompanionInline
    ]


class qpPlayerCharacterAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "player",
        "world"
    ]
    list_filter = [
        "world"
    ]
    search_fields = [
        "first_name",
        "middle_name",
        "last_name",
        "player__playername"
    ]
    raw_id_fields = ["player", "world"]
    fieldsets = [
        (" ", {
            "fields": [
                "player",
                "world",
                "geo",
                "is_active"
            ]
        }),
        (_("Informations"), {
            "fields": [
                "first_name",
                "middle_name",
                "last_name"
            ]
        }),
        (_("Resistances"), {
            "fields": [
                "resistance_physical",
                "resistance_mental",
                "resistance_spiritual"
            ]
        }),
        (_("Attributes"), {
            "fields": [
                ("attribute_strength", "attribute_constitution"),
                ("attribute_dexterity", "attribute_perception"),
                ("attribute_intelligence", "attribute_composure")
            ]
        })
    ]


@admin.register(qpPlayerHero)
class qpPlayerHeroAdmin(qpPlayerCharacterAdmin):
    pass

@admin.register(qpPlayerCompanion)
class qpPlayerCompanionAdmin(qpPlayerCharacterAdmin):
    pass