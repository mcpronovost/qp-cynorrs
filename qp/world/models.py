from django.db import models
from django.utils.translation import gettext_lazy as _

from qp.utils import (
    CHOIX_VISIBILITY
)


class qpWorld(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=32,
        blank=False,
        null=False
    )
    slug = models.SlugField(
        verbose_name=_("Slug"),
        unique=True,
        blank=True,
        null=True
    )
    description = models.CharField(
        verbose_name=_("Description"),
        max_length=250,
        blank=True,
        null=True
    )
    creator = models.ForeignKey(
        "player.qpPlayer",
        on_delete=models.SET_NULL,
        related_name="creator_worlds",
        verbose_name=_("Creator"),
        blank=True,
        null=True
    )
    administrators = models.ManyToManyField(
        "player.qpPlayer",
        related_name="admin_worlds",
        verbose_name=_("Administrators"),
        blank=True
    )
    moderators = models.ManyToManyField(
        "player.qpPlayer",
        related_name="modo_worlds",
        verbose_name=_("Moderators"),
        blank=True
    )
    visibility = models.PositiveSmallIntegerField(
        verbose_name=_("Visibility"),
        choices=CHOIX_VISIBILITY,
        default=1,
        blank=False,
        null=False
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
        verbose_name = _("World")
        verbose_name_plural = _("Worlds")
        ordering = ["name"]
    
    class Qapi:
        admin_order = 1
    
    def __str__(self):
        return "%s" % (
            str(self.name)
        )
    
    @property
    def count_players(self):
        result = 0
        try:
            result = self.heros.filter(is_active=True).values_list("player").distinct().count()
        except Exception:
            pass
        return result
    
    @property
    def count_heros(self):
        return self.heros.filter(is_active=True).count()
    
    @property
    def count_chapters(self):
        result = 0
        try:
            result = self.forum.count_chapters
        except Exception:
            pass
        return result
    
    @property
    def count_messages(self):
        result = 0
        try:
            result = self.forum.count_messages
        except Exception:
            pass
        return result


class qpWorldRace(models.Model):
    world = models.ForeignKey(
        qpWorld,
        on_delete=models.CASCADE,
        related_name="races",
        verbose_name=_("World"),
        blank=False,
        null=False
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=32,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _("Race")
        verbose_name_plural = _("Races")
        ordering = ["name"]
    
    class Qapi:
        admin_order = 20
    
    def __str__(self):
        return "%s" % (
            str(self.name)
        )


class qpWorldEthnicity(models.Model):
    world = models.ForeignKey(
        qpWorld,
        on_delete=models.CASCADE,
        related_name="ethnicities",
        verbose_name=_("World"),
        blank=False,
        null=False
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=32,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _("Ethnicity")
        verbose_name_plural = _("Ethnicities")
        ordering = ["name"]
    
    class Qapi:
        admin_order = 30
    
    def __str__(self):
        return "%s" % (
            str(self.name)
        )


class qpWorldNationality(models.Model):
    world = models.ForeignKey(
        qpWorld,
        on_delete=models.CASCADE,
        related_name="nationalities",
        verbose_name=_("World"),
        blank=False,
        null=False
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=32,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _("Nationality")
        verbose_name_plural = _("Nationalities")
        ordering = ["name"]
    
    class Qapi:
        admin_order = 40
    
    def __str__(self):
        return "%s" % (
            str(self.name)
        )
