from django.contrib import admin

from qp.player.models import qpPlayer


@admin.register(qpPlayer)
class qpPlayerAdmin(admin.ModelAdmin):
    pass