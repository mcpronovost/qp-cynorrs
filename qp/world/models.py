import math
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField

from qp.world.utils import (
    get_perpage
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
    stylesheet = models.TextField(
        verbose_name=_("Custom Stylesheet"),
        default="",
        blank=True,
        null=True
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

    def get_absolute_url(self):
        return "/worlds/%s/" % (
            str(self.slug)
        )
    
    @property
    def count_chapters(self):
        result = 0
        try:
            for zone in self.zones.all():
                result += zone.count_chapters
        except Exception:
            pass
        return result
    
    @property
    def count_messages(self):
        result = 0
        try:
            for zone in self.zones.all():
                result += zone.count_messages
        except Exception:
            pass
        return result


class qpWorldZone(models.Model):
    world = models.ForeignKey(
        qpWorld,
        on_delete=models.CASCADE,
        related_name="zones",
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
        verbose_name = _("Zone")
        verbose_name_plural = _("Zones")
        ordering = ["world", "ordering", "name"]
    
    class Qapi:
        admin_order = 2
    
    def __str__(self):
        return "%s" % (
            str(self.name)
        )

    def save(self, *args, **kwargs):
        if self.ordering == 0:
            lastorder = qpWorldZone.objects.filter(
                world=self.world
            ).last().ordering if qpWorldZone.objects.filter(
                world=self.world
            ).last() is not None else 0
            self.ordering = (lastorder + 1)
        return super().save(*args, **kwargs)
    
    @property
    def count_chapters(self):
        result = 0
        try:
            for territory in self.territories.all():
                result += territory.count_chapters
        except Exception:
            pass
        return result
    
    @property
    def count_messages(self):
        result = 0
        try:
            for territory in self.territories.all():
                result += territory.count_messages
        except Exception:
            pass
        return result


class qpWorldTerritory(models.Model):
    zone = models.ForeignKey(
        qpWorldZone,
        on_delete=models.CASCADE,
        related_name="territories",
        verbose_name=_("Zone"),
        blank=False,
        null=False
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=32,
        blank=False,
        null=False
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        null=True
    )
    colour = ColorField(
        verbose_name=_("Colour"),
        blank=True,
        null=True
    )
    flexbasis = models.CharField(
        verbose_name=_("Flex Basis"),
        max_length=9,
        default="100%",
        blank=False,
        null=False
    )
    ordering = models.PositiveSmallIntegerField(
        verbose_name=_("Ordering"),
        default=0,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _("Territory")
        verbose_name_plural = _("Territories")
        ordering = ["zone", "ordering", "name"]
    
    class Qapi:
        admin_order = 3
    
    def __str__(self):
        return "%s" % (
            str(self.name)
        )

    def save(self, *args, **kwargs):
        if self.ordering == 0:
            lastorder = qpWorldTerritory.objects.filter(
                zone=self.zone
            ).last().ordering if qpWorldTerritory.objects.filter(
                zone=self.zone
            ).last() is not None else 0
            self.ordering = (lastorder + 1)
        return super().save(*args, **kwargs)
    
    @property
    def world(self):
        if self.zone is not None:
            return self.zone.world
        return None
    
    @property
    def count_chapters(self):
        result = 0
        try:
            result = self.chapters.filter(
                sector=None
            ).count()
        except Exception:
            pass
        return result
    
    @property
    def count_chapters_all(self):
        result = 0
        try:
            result = self.chapters.count()
        except Exception:
            pass
        return result
    
    @property
    def count_messages(self):
        result = 0
        try:
            for chapter in self.chapters.all():
                result += chapter.count_messages
        except Exception:
            pass
        return result
    
    @property
    def last_message(self):
        result = None
        try:
            if self.count_messages:
                result = qpWorldMessage.objects.filter(
                    chapter__territory=self
                ).last()
        except Exception:
            pass
        return result


class qpWorldSector(models.Model):
    territory = models.ForeignKey(
        qpWorldTerritory,
        on_delete=models.CASCADE,
        related_name="sectors",
        verbose_name=_("Territory"),
        blank=False,
        null=False
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=32,
        blank=False,
        null=False
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        null=True
    )
    colour = ColorField(
        verbose_name=_("Colour"),
        blank=True,
        null=True
    )
    flexbasis = models.CharField(
        verbose_name=_("Flex Basis"),
        max_length=9,
        default="100%",
        blank=False,
        null=False
    )
    ordering = models.PositiveSmallIntegerField(
        verbose_name=_("Ordering"),
        default=0,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _("Sector")
        verbose_name_plural = _("Sectors")
        ordering = ["territory", "ordering", "name"]
    
    class Qapi:
        admin_order = 4
    
    def __str__(self):
        return "%s" % (
            str(self.name)
        )

    def save(self, *args, **kwargs):
        if self.ordering == 0:
            lastorder = qpWorldSector.objects.filter(
                territory=self.territory
            ).last().ordering if qpWorldSector.objects.filter(
                territory=self.territory
            ).last() is not None else 0
            self.ordering = (lastorder + 1)
        return super().save(*args, **kwargs)
    
    @property
    def count_chapters(self):
        result = 0
        try:
            result = self.chapters.count()
        except Exception:
            pass
        return result
    
    @property
    def count_messages(self):
        result = 0
        try:
            for chapter in self.chapters.all():
                result += chapter.count_messages
        except Exception:
            pass
        return result
    
    @property
    def last_message(self):
        result = None
        try:
            if self.count_messages:
                result = qpWorldMessage.objects.filter(
                    chapter__sector=self
                ).last()
        except Exception:
            pass
        return result


class qpWorldChapter(models.Model):
    territory = models.ForeignKey(
        qpWorldTerritory,
        on_delete=models.SET_NULL,
        related_name="chapters",
        verbose_name=_("Territory"),
        blank=True,
        null=True
    )
    sector = models.ForeignKey(
        qpWorldSector,
        on_delete=models.SET_NULL,
        related_name="chapters",
        verbose_name=_("Sector"),
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        "player.qpPlayerHero",
        on_delete=models.SET_NULL,
        related_name="chapters",
        verbose_name=_("Author"),
        blank=True,
        null=True
    )
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=90,
        blank=False,
        null=False
    )
    description = models.CharField(
        verbose_name=_("Description"),
        max_length=200,
        blank=True,
        null=True
    )
    last_message = models.OneToOneField(
        "world.qpWorldMessage",
        on_delete=models.SET_NULL,
        related_name="lastmessage_chapter",
        verbose_name=_("Last Message"),
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated"),
        auto_now=True
    )

    class Meta:
        verbose_name = _("Chapter")
        verbose_name_plural = _("Chapters")
        ordering = ["-last_message__created_at", "-updated_at", "-created_at"]
    
    class Qapi:
        admin_order = 5
    
    def __str__(self):
        return "%s" % (
            str(self.title)
        )

    def save(self, *args, **kwargs):
        try:
            self.last_message = self.messages.last()
        except IndexError:
            pass
        return super().save(*args, **kwargs)
    
    @property
    def count_messages(self):
        result = 0
        try:
            result = self.messages.count()
        except Exception:
            pass
        return result
    
    def get_route(self):
        result = {"name": "WorldChapter", "params": {
            "world_pk": self.territory.world.id,
            "slug": self.territory.world.slug,
            "zone_pk": self.territory.zone.id,
            "zone_slug": slugify(self.territory.zone.name),
            "territory_pk": self.territory.id,
            "territory_slug": slugify(self.territory.name),
            "chapter_pk": self.id,
            "chapter_slug": slugify(self.title)
        }, "hash": "#c%s" % (self.id)}
        if self.sector is not None:
            result["params"]["sector_pk"] = self.sector.pk
            result["params"]["sector_slug"] = slugify(self.sector.name)
        return result

    def update_last_message(self):
        try:
            self.last_message = self.messages.last()
            self.save()
        except IndexError:
            pass


class qpWorldMessage(models.Model):
    chapter = models.ForeignKey(
        qpWorldChapter,
        on_delete=models.CASCADE,
        related_name="messages",
        verbose_name=_("Chapter"),
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        "player.qpPlayerHero",
        on_delete=models.SET_NULL,
        related_name="messages",
        verbose_name=_("Author"),
        blank=True,
        null=True
    )
    text = models.TextField(
        verbose_name=_("Text"),
        blank=False,
        null=False
    )
    count_updates = models.PositiveSmallIntegerField(
        verbose_name=_("Updates"),
        default=0
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated"),
        auto_now=True
    )

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")
        ordering = ["created_at"]
    
    class Qapi:
        admin_order = 6
    
    def __str__(self):
        return _("Message #%(pk)s") % {
            "pk": str(self.pk)
        }

    def save(self, *args, **kwargs):
        if self.pk is not None:
            self.count_updates += 1
        super().save(*args, **kwargs)
        self.chapter.update_last_message()
        return

    def delete(self):
        super().delete()
        self.chapter.update_last_message()
        return
    
    def get_route(self, request, last = False):
        result = {"name": "WorldChapter", "params": {
            "world_pk": self.chapter.territory.world.id,
            "slug": self.chapter.territory.world.slug,
            "zone_pk": self.chapter.territory.zone.id,
            "zone_slug": slugify(self.chapter.territory.zone.name),
            "territory_pk": self.chapter.territory.id,
            "territory_slug": slugify(self.chapter.territory.name),
            "chapter_pk": self.chapter.id,
            "chapter_slug": slugify(self.chapter.title)
        }, "hash": "#m%s" % (self.id)}
        if self.chapter.sector is not None:
            result["params"]["sector_pk"] = self.chapter.sector.pk
            result["params"]["sector_slug"] = slugify(self.chapter.sector.name)
        if last:
            perpage = get_perpage(request, "messages")
            result["query"] = {
                "page": math.ceil(self.chapter.messages.count() / perpage)
            }
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
    slug = models.SlugField(
        verbose_name=_("Slug"),
        unique=True,
        blank=True,
        null=True
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
    slug = models.SlugField(
        verbose_name=_("Slug"),
        unique=True,
        blank=True,
        null=True
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
    slug = models.SlugField(
        verbose_name=_("Slug"),
        unique=True,
        blank=True,
        null=True
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
