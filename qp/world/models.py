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

    def save(self, *args, **kwargs):
        self.slug = slugify(
            str(self.name)
        )
        return super().save(*args, **kwargs)


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
    slug = models.SlugField(
        verbose_name=_("Slug"),
        unique=True,
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


class qpWorldTerritoty(models.Model):
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
    slug = models.SlugField(
        verbose_name=_("Slug"),
        unique=True,
        blank=True,
        null=True
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


class qpWorldSector(models.Model):
    territory = models.ForeignKey(
        qpWorldTerritoty,
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
    slug = models.SlugField(
        verbose_name=_("Slug"),
        unique=True,
        blank=True,
        null=True
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
