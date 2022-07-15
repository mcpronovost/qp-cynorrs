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
    pass

@admin.register(qpWorldZone)
class qpWorldZoneAdmin(admin.ModelAdmin):
    pass

@admin.register(qpWorldTerritory)
class qpWorldTerritoryAdmin(admin.ModelAdmin):
    pass

@admin.register(qpWorldSector)
class qpWorldSectorAdmin(admin.ModelAdmin):
    pass

@admin.register(qpWorldChapter)
class qpWorldChapterAdmin(admin.ModelAdmin):
    pass

@admin.register(qpWorldMessage)
class qpWorldMessageAdmin(admin.ModelAdmin):
    list_display = ["__str__", "author", "created_at", "updated_at"]

@admin.register(qpWorldRace)
class qpWorldRaceAdmin(admin.ModelAdmin):
    pass

@admin.register(qpWorldEthnicity)
class qpWorldEthnicityAdmin(admin.ModelAdmin):
    pass

@admin.register(qpWorldNationality)
class qpWorldNationalityAdmin(admin.ModelAdmin):
    pass
