from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from qp.world.models import (
    qpWorld,
    qpWorldZone,
    qpWorldTerritoty,
    qpWorldSector,
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

@admin.register(qpWorldTerritoty)
class qpWorldTerritotyAdmin(admin.ModelAdmin):
    pass

@admin.register(qpWorldSector)
class qpWorldSectorAdmin(admin.ModelAdmin):
    pass

@admin.register(qpWorldRace)
class qpWorldRaceAdmin(admin.ModelAdmin):
    pass

@admin.register(qpWorldEthnicity)
class qpWorldEthnicityAdmin(admin.ModelAdmin):
    pass

@admin.register(qpWorldNationality)
class qpWorldNationalityAdmin(admin.ModelAdmin):
    pass
