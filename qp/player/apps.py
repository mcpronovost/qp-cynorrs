from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class PlayerConfig(AppConfig):
    name = "qp.player"
    verbose_name = _("Player")

    class Qapi:
        admin_order = 3
