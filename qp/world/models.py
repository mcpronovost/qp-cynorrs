from django.db import models
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField

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
    
    def get_is_visible(self, request):
        try:
            player = request.user.player or request.user.is_authenticated
            if player is None:
                return self.visibility == 0 and self.is_active
            else:
                return self.creator == player or (
                    (self.is_active and (
                        self.visibility == 0 or self.visibility == 6 or (
                            self.visibility == 2 and player in self.administrators.all()
                        ) or (
                            self.visibility == 3 and (player in self.administrators.all() or player in self.moderators.all())
                        ) or (
                            self.visibility == 4 and (
                                player in self.administrators.all() or 
                                player in self.moderators.all() or 
                                player.heros.filter(world=self, is_valid=True, is_active=True).count()
                            )
                        ) or (
                            self.visibility == 5 and (
                                player in self.administrators.all() or 
                                player in self.moderators.all() or 
                                player.heros.filter(world=self, is_active=True).count()
                            )
                        )
                    ))
                )
        except:
            pass
        return False
    
    @property
    def style(self):
        return self.styles.filter(is_active=True).last()
    
    @property
    def copyright(self):
        year = self.created_at.year
        if year != self.updated_at.year:
            year = "%s-%s" % (
                str(year),
                str(self.updated_at.year)
            )
        if self.creator:
            return "%s %s" % (
                str(year),
                str(self.creator.playername)
            )
        return "%s" % (str(year))
    
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


class qpWorldStyle(models.Model):
    world = models.ForeignKey(
        qpWorld,
        on_delete=models.CASCADE,
        related_name="styles",
        verbose_name=_("World"),
        blank=True,
        null=True
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=32,
        blank=False,
        null=False
    )
    app_body_bg = ColorField(
        verbose_name=_("App Background Colour"),
        default="#c9cfd1"
    )
    app_body_txt = ColorField(
        verbose_name=_("App Text Colour"),
        default="#435259"
    )
    app_header_bg = ColorField(
        verbose_name=_("App Header Background Colour"),
        default="#435259"
    )
    app_header_txt = ColorField(
        verbose_name=_("App Header Text Colour"),
        default="#c9cfd1"
    )
    app_header_txt_hov = ColorField(
        verbose_name=_("App Header Text Hover Colour"),
        default="#dbe0e2"
    )
    app_sidebar_bg = ColorField(
        verbose_name=_("App Sidebar Background Colour"),
        default="#dbe0e2"
    )
    app_smallbar_bg = ColorField(
        verbose_name=_("App Smallbar Background Colour"),
        default="#dbe0e2"
    )
    stylesheet = models.TextField(
        verbose_name=_("Custom Stylesheet"),
        default="",
        blank=True,
        null=False
    )
    is_active = models.BooleanField(
        verbose_name=_("Active"),
        default=False
    )

    class Meta:
        verbose_name = _("Style")
        verbose_name_plural = _("Styles")
        ordering = ["name"]
    
    class Qapi:
        admin_order = 1000
    
    def __str__(self):
        return "%s" % (
            str(self.name)
        )
