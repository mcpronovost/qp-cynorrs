from django.db import models
from django.utils.translation import gettext_lazy as _

from qp.world.models import (
    qpWorld,
    qpWorldSector
)


class qpGameEvent(models.Model):
    CHOIX_TYPE = [
        ("travel", _("Travel")),
        ("ressource", _("Ressource"))
    ]
    sector = models.ForeignKey(
        qpWorldSector,
        on_delete=models.CASCADE,
        related_name="game_events",
        verbose_name=_("Sector"),
        blank=False,
        null=False
    )
    type = models.CharField(
        verbose_name=_("Type"),
        max_length=32,
        choices=CHOIX_TYPE,
        blank=False,
        null=False
    )
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=120,
        blank=False,
        null=False
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        null=True
    )
    ordering = models.PositiveSmallIntegerField(
        verbose_name=_("Ordering"),
        default=0,
        blank=False,
        null=False
    )
    counter = models.PositiveSmallIntegerField(
        verbose_name=_("Counter"),
        default=None,
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        verbose_name=_("Active"),
        default=True
    )
    is_luckyroll = models.BooleanField(
        verbose_name=_("Lucky Roll"),
        default=False
    )

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ["ordering"]
    
    class Qapi:
        admin_order = 1
    
    def __str__(self):
        return "%s" % (
            self.titre
        )


class qpGameEventLuckyRollEntry(models.Model):
    event = models.ForeignKey(
        qpGameEvent,
        on_delete=models.CASCADE,
        related_name="luckyrolls",
        verbose_name=_("Event"),
        blank=False,
        null=False
    )
    success_roll = models.PositiveSmallIntegerField(
        verbose_name=_("Success Roll"),
        default=6,
        blank=False,
        null=False
    )
    success_message = models.TextField(
        verbose_name=_("Success Message"),
        blank=True,
        null=True
    )
    failure_message = models.TextField(
        verbose_name=_("Failure Message"),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Lucky Roll Entry")
        verbose_name_plural = _("Lucky Roll Entries")
    
    def __str__(self):
        return "#%s" % (
            self.pk
        )


class qpGameAction(models.Model):
    event = models.ForeignKey(
        qpGameEvent,
        on_delete=models.CASCADE,
        related_name="actions",
        verbose_name=_("Event"),
        blank=False,
        null=False
    )
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=120,
        blank=False,
        null=False
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        null=True
    )
    ordering = models.PositiveSmallIntegerField(
        verbose_name=_("Ordering"),
        default=0,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _("Action")
        verbose_name_plural = _("Actions")
        ordering = ["ordering"]
    
    def __str__(self):
        return "%s" % (
            self.titre
        )


class qpGameBonusMalus(models.Model):
    CHOIX_TYPE = [
        ("bonus", _("Bonus")),
        ("malus", _("Malus"))
    ]
    world = models.ForeignKey(
        qpWorld,
        on_delete=models.CASCADE,
        related_name="bonus",
        verbose_name=_("World"),
        blank=False,
        null=False
    )
    type = models.CharField(
        verbose_name=_("Type"),
        max_length=6,
        choices=CHOIX_TYPE,
        blank=False,
        null=False
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=120,
        blank=False,
        null=False
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Bonus / Malus")
        verbose_name_plural = _("Bonus / Malus")
        ordering = ["name"]
    
    def __str__(self):
        return "%s" % (
            self.name
        )
    