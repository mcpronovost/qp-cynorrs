from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class WorldConfig(AppConfig):
    name = "qp.world"
    verbose_name = _("World")

    class Qapi:
        admin_order = 4
