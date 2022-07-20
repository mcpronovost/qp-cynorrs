import hashlib
from zoneinfo import ZoneInfo
from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.formats import date_format
from django.utils.translation import gettext_lazy as _
from qp.settings import TIME_ZONE

from qp.world.models import qpWorld


CHOIX_GENDER = [
    ("m", _("Male")),
    ("f", _("Female")),
    ("o", _("Other"))
]


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
    slug = models.SlugField(
        verbose_name=_("Slug"),
        unique=True,
        blank=True,
        null=True
    )
    affinity = models.PositiveIntegerField(
        verbose_name=_("Affinity"),
        default=0,
        blank=False,
        null=False
    )
    avatar = models.ImageField(
        verbose_name=_("Avatar"),
        upload_to="players/avatars",
        blank=True,
        null=True
    )
    limits_create_worlds = models.PositiveSmallIntegerField(
        verbose_name=_("World Creation Limit"),
        default=2,
        blank=False,
        null=False
    )
    limits_create_heros = models.PositiveSmallIntegerField(
        verbose_name=_("Hero Creation Limit"),
        default=10,
        blank=False,
        null=False
    )
    settings_perpage_chapters = models.PositiveSmallIntegerField(
        verbose_name=_("Chapitres per page"),
        default=12,
        blank=False,
        null=False
    )
    settings_perpage_messages = models.PositiveSmallIntegerField(
        verbose_name=_("Messages per page"),
        default=20,
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
    
    class Qapi:
        admin_order = 1
    
    def __str__(self):
        return "%s (%s)" % (
            str(self.playername),
            str(self.user.username) if self.user else "-"
        )

    def get_absolute_url(self):
        return "/players/%s/" % (
            str(self.slug)
        )

    def save(self, *args, **kwargs):
        self.slug = slugify(
            str(self.playername)
        )
        return super().save(*args, **kwargs)
    
    @property
    def name(self):
        return "%s" % (
            str(self.playername)
        )
    
    @property
    def last_login(self):
        if self.user is not None and self.user.last_login is not None:
            return "%s" % (
                date_format(
                    self.user.last_login.astimezone(ZoneInfo(TIME_ZONE)),
                    format="SHORT_DATETIME_FORMAT"
                )
            )
        return "-"
    
    def can_create_worlds(self):
        if self.creator_worlds.count() < self.limits_create_worlds:
            return True
        return False
    
    def can_create_heros(self):
        if self.heros.count() < self.limits_create_heros:
            return True
        return False


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
    gender = models.CharField(
        verbose_name=_("Gender"),
        max_length=2,
        choices=CHOIX_GENDER,
        default="o",
        blank=False,
        null=False
    )
    geo = models.TextField(
        verbose_name=_("Geolocalisation"),
        blank=True,
        null=True
    )
    avatar = models.ImageField(
        verbose_name=_("Avatar"),
        upload_to="characters/avatars",
        blank=True,
        null=True
    )
    resistance_physical = models.PositiveSmallIntegerField(
        verbose_name=_("Physical Resistance"),
        default=0,
        blank=False,
        null=False
    )
    resistance_mental = models.PositiveSmallIntegerField(
        verbose_name=_("Mental Resistance"),
        default=0,
        blank=False,
        null=False
    )
    resistance_spiritual = models.PositiveSmallIntegerField(
        verbose_name=_("Spiritual Resistance"),
        default=0,
        blank=False,
        null=False
    )
    attribute_strength = models.PositiveIntegerField(
        verbose_name=_("Strength"),
        default=0,
        blank=False,
        null=False
    )
    attribute_constitution = models.PositiveIntegerField(
        verbose_name=_("Constitution"),
        default=0,
        blank=False,
        null=False
    )
    attribute_dexterity = models.PositiveIntegerField(
        verbose_name=_("Dexterity"),
        default=0,
        blank=False,
        null=False
    )
    attribute_perception = models.PositiveIntegerField(
        verbose_name=_("Perception"),
        default=0,
        blank=False,
        null=False
    )
    attribute_intelligence = models.PositiveIntegerField(
        verbose_name=_("Intelligence"),
        default=0,
        blank=False,
        null=False
    )
    attribute_composure = models.PositiveIntegerField(
        verbose_name=_("Composure"),
        default=0,
        blank=False,
        null=False
    )
    is_valid = models.BooleanField(
        verbose_name=_("Valid"),
        default=False
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

    def __str__(self):
        return self.name
    
    @property
    def name(self):
        """
        Name merge the first_name, the middle_name and the last_name into a single string.

        :return: a STRING.
        """
        names = []
        if self.first_name and self.first_name != "":
            names.append(self.first_name)
        if self.middle_name and self.middle_name != "":
            names.append(self.middle_name)
        if self.last_name and self.last_name != "":
            names.append(self.last_name)
        return "%s" % (
            " ".join(names)
        )
    
    @property
    def initials(self):
        initials = []
        if self.first_name and self.first_name != "":
            initials.append(self.first_name[0])
        if self.middle_name and self.middle_name != "":
            initials.append(self.middle_name[0])
        if self.last_name and self.last_name != "":
            initials.append(self.last_name[0])
        return "%s" % (
            "".join(initials)
        )
    
    @property
    def karma(self):
        """
        Karma is used to determine the luck of a character and is based on character informations to get a payload. The payload is converted in bytes, then hashed with sha224 to get a hexadecimal digest that will be used to find an INTEGER.

        :return: an INTEGER between 1 et 12.
        """
        payload = "%s-%s-%s-%s-%s" % (
            str(self.name),
            str(self.gender),
            str(self.resistance_physical),
            str(self.resistance_mental),
            str(self.resistance_spiritual)
        )
        return ((int(hashlib.sha224(
            bytes(payload)
        ).hexdigest(), base=16)) % 12) + 1


class qpPlayerHero(qpPlayerCharacter):
    player = models.ForeignKey(
        qpPlayer,
        on_delete=models.CASCADE,
        related_name="heros",
        verbose_name=_("Player"),
        blank=False,
        null=False
    )
    world = models.ForeignKey(
        qpWorld,
        on_delete=models.SET_NULL,
        related_name="heros",
        verbose_name=_("World"),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Hero")
        verbose_name_plural = _("Heros")
    
    class Qapi:
        admin_order = 2


class qpPlayerCompanion(qpPlayerCharacter):
    player = models.ForeignKey(
        qpPlayer,
        on_delete=models.SET_NULL,
        related_name="companions",
        verbose_name=_("Player"),
        blank=True,
        null=True
    )
    world = models.ForeignKey(
        qpWorld,
        on_delete=models.SET_NULL,
        related_name="companions",
        verbose_name=_("World"),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Companion")
        verbose_name_plural = _("Companions")
    
    class Qapi:
        admin_order = 3

