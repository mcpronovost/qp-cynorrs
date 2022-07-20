import math
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField

from qp.utils import (
    CHOIX_VISIBILITY
)

from qp.forum.utils import (
    get_perpage
)


class qpForum(models.Model):
    world = models.OneToOneField(
        "world.qpWorld",
        on_delete=models.SET_NULL,
        related_name="forum",
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
        verbose_name = _("Forum")
        verbose_name_plural = _("Forums")
        ordering = ["name"]
    
    class Qapi:
        admin_order = 1
    
    def __str__(self):
        return "%s" % (
            str(self.name)
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


class qpForumZone(models.Model):
    forum = models.ForeignKey(
        qpForum,
        on_delete=models.CASCADE,
        related_name="zones",
        verbose_name=_("Forum"),
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
        ordering = ["forum", "ordering", "name"]
    
    class Qapi:
        admin_order = 2
    
    def __str__(self):
        return "%s" % (
            str(self.name)
        )

    def save(self, *args, **kwargs):
        if self.ordering == 0:
            lastorder = qpForumZone.objects.filter(
                forum=self.forum
            ).last().ordering if qpForumZone.objects.filter(
                forum=self.forum
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


class qpForumTerritory(models.Model):
    zone = models.ForeignKey(
        qpForumZone,
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
            lastorder = qpForumTerritory.objects.filter(
                zone=self.zone
            ).last().ordering if qpForumTerritory.objects.filter(
                zone=self.zone
            ).last() is not None else 0
            self.ordering = (lastorder + 1)
        return super().save(*args, **kwargs)
    
    @property
    def forum(self):
        if self.zone is not None:
            return self.zone.forum
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
                result = qpForumMessage.objects.filter(
                    chapter__territory=self
                ).last()
        except Exception:
            pass
        return result


class qpForumSector(models.Model):
    territory = models.ForeignKey(
        qpForumTerritory,
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
            lastorder = qpForumSector.objects.filter(
                territory=self.territory
            ).last().ordering if qpForumSector.objects.filter(
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
                result = qpForumMessage.objects.filter(
                    chapter__sector=self
                ).last()
        except Exception:
            pass
        return result


class qpForumChapter(models.Model):
    territory = models.ForeignKey(
        qpForumTerritory,
        on_delete=models.SET_NULL,
        related_name="chapters",
        verbose_name=_("Territory"),
        blank=True,
        null=True
    )
    sector = models.ForeignKey(
        qpForumSector,
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
        "forum.qpForumMessage",
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
        result = {"name": "ForumChapter", "params": {
            "forum_pk": self.territory.forum.id,
            "slug": self.territory.forum.slug,
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


class qpForumMessage(models.Model):
    chapter = models.ForeignKey(
        qpForumChapter,
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
        result = {"name": "ForumChapter", "params": {
            "forum_pk": self.chapter.territory.forum.id,
            "slug": self.chapter.territory.forum.slug,
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