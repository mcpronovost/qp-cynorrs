from django.utils.translation import gettext_lazy as _

CHOIX_GENDER = [
    ("m", _("Male")),
    ("f", _("Female")),
    ("o", _("Other"))
]

CHOIX_VISIBILITY = [
    (0, _("Everyone")),
    (1, _("Creator Only")),
    (2, _("Administrators")),
    (3, _("Moderators")),
    (4, _("Validated Players")),
    (5, _("Registered Players")),
    (6, _("Players"))
]