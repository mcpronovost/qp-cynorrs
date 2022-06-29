from django.db import models
from django.utils.translation import gettext_lazy as _

from qp.world.models import (
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

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ["ordering"]
    
    def __str__(self):
        return "%s" % (
            self.titre
        )


class qpGameEventAction(models.Model):
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
    