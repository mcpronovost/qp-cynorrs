from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class qpPlayer(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name="player",
        verbose_name=_("User"),
        blank=True,
        null=True
    )
    playername = models.CharField(
        verbose_name=_("Playername"),
        max_length=32,
        blank=False,
        null=False
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = _("Player")
        verbose_name_plural = _("Players")
        ordering = ["-user__last_login"]
    
    @property
    def name(self):
        if self.playername is not None and self.playername != "":
            return "%s" % (
                self.playername
            )
        return "%s" % (
            str(_("Traveler"))
        )


class qpPlayerCharacter(models.Model):
    first_name = models.CharField(
        verbose_name=_("First Name"),
        max_length=32,
        blank=True,
        null=True
    )
    middle_name = models.CharField(
        verbose_name=_("Middle Name"),
        max_length=32,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        verbose_name=_("Last Name"),
        max_length=32,
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        verbose_name=_("Active"),
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True
        ordering = ["last_name", "middle_name", "first_name"]


class qpPlayerHero(qpPlayerCharacter):
    player = models.ForeignKey(
        qpPlayer,
        on_delete=models.CASCADE,
        related_name="heros",
        verbose_name=_("Player"),
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _("Hero")
        verbose_name_plural = _("Heros")


class qpPlayerCompanion(qpPlayerCharacter):
    player = models.ForeignKey(
        qpPlayer,
        on_delete=models.CASCADE,
        related_name="companions",
        verbose_name=_("Player"),
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _("Companion")
        verbose_name_plural = _("Companions")

