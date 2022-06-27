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
        return "%s (%s)" % (
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


class qpWorldRace(models.Model):
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
        admin_order = 2


class qpWorldEthnicity(models.Model):
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
        admin_order = 3


class qpWorldNationality(models.Model):
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
        admin_order = 4
