from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class GameConfig(AppConfig):
    name = "qp.game"
    verbose_name = _("Game")

    class Qapi:
        admin_order = 4
