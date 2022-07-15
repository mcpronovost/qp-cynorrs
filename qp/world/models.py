from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


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

    class Meta:
        verbose_name = _("Zone")
        verbose_name_plural = _("Zones")
        ordering = ["world", "name"]
    
    class Qapi:
        admin_order = 2
    
    def __str__(self):
        return "%s" % (
            str(self.name)
        )
    
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
    flexbasis = models.CharField(
        verbose_name=_("Flex Basis"),
        max_length=9,
        default="100%",
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _("Territory")
        verbose_name_plural = _("Territories")
        ordering = ["zone", "name"]
    
    class Qapi:
        admin_order = 3
    
    def __str__(self):
        return "%s" % (
            str(self.name)
        )
    
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
    flexbasis = models.CharField(
        verbose_name=_("Flex Basis"),
        max_length=9,
        default="100%",
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _("Sector")
        verbose_name_plural = _("Sectors")
        ordering = ["territory", "name"]
    
    class Qapi:
        admin_order = 4
    
    def __str__(self):
        return "%s" % (
            str(self.name)
        )
    
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
        ordering = ["-updated_at", "-created_at"]
    
    class Qapi:
        admin_order = 5
    
    def __str__(self):
        return "%s" % (
            str(self.title)
        )
    
    @property
    def count_messages(self):
        result = 0
        try:
            result = self.messages.count()
        except Exception:
            pass
        return result


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
        return super().save(*args, **kwargs)


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
