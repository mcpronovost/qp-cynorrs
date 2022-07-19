from django.utils.translation import gettext_lazy as _

CHOIX_VISIBILITY = [
    (0, _("Everyone")),
    (1, _("Creator Only")),
    (2, _("Administrators")),
    (3, _("Moderators")),
    (4, _("Validated Players")),
    (5, _("Players"))
]

def get_perpage(request, view):
    result = 1
    # ===---
    if request.user.is_authenticated and request.user.player:
        if view == "chapters":
            result = request.user.player.settings_perpage_chapters
        elif view == "messages":
            result = request.user.player.settings_perpage_messages
    else:
        perpage_defaults = {
            "chapters": 12,
            "messages": 20
        }
        result = perpage_defaults[view]
    # ===---
    return result
