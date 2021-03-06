from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from qp.world.models import (
    qpWorld,
    qpWorldRace,
    qpWorldEthnicity,
    qpWorldNationality,
    qpWorldStyle
)


class qpWorldStyleInline(admin.StackedInline):
    model = qpWorldStyle
    extra = 0


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
    inlines = [qpWorldStyleInline]

@admin.register(qpWorldRace)
class qpWorldRaceAdmin(admin.ModelAdmin):
    pass

@admin.register(qpWorldEthnicity)
class qpWorldEthnicityAdmin(admin.ModelAdmin):
    pass

@admin.register(qpWorldNationality)
class qpWorldNationalityAdmin(admin.ModelAdmin):
    pass
