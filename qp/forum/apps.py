from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ForumConfig(AppConfig):
    name = "qp.forum"
    verbose_name = _("Forum")

    class Qapi:
        admin_order = 5
