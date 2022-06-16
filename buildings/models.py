from django.db import models
from django.urls import reverse
from users.models import MyUser
from django.utils.translation import gettext_lazy as _

#  for django panel / ex: to return only active ones get_queryset().is_active()
class BuildingManager(models.Manager):
    def get_queryset(self):
        return super(BuildingManager, self).get_queryset()


class Building(models.Model):
    """
    The Building table.
    """

    NONE = 0
    PEPSI = 1
    COKE = 2

    TYPES = (
        (NONE, "-"),
        (PEPSI, "Pepsi"),
        (COKE, "Coke"),
    )
    company = models.IntegerField(choices=TYPES, default=0)
    building_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = BuildingManager()
    created_by = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name="building_creator",
        default=MyUser,
    )

    class Meta:
        verbose_name_plural = "Buildings"
        ordering = ("-created_at",)

    # e.g in django template,get URL links for all buildings by calling this
    def get_absolute_url(self):
        return reverse("buildings: building_detail", args=[self.slug])

    def __str__(self):
        return self.building_name


class BuildingImage(models.Model):
    """
    The Building Image table.
    """

    building = models.OneToOneField(
        Building, on_delete=models.CASCADE, related_name="building_image"
    )
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a building image"),
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("Alternative"),
        help_text=_("Please add alternative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Building Image")
        verbose_name_plural = _("Building Images")


class Address(models.Model):
    """
    The Address table.
    """

    building = models.OneToOneField(
        Building, on_delete=models.CASCADE, related_name="building_address"
    )
    country = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Addresses"
        ordering = ("-created_at",)

    def __str__(self):
        return str(self.address)


class Floor(models.Model):
    """
    The Floor table.
    """

    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, related_name="building_floor"
    )
    title = models.CharField(max_length=200, null=True, blank=True)
    level = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Floors"
        ordering = ("-created_at",)

    def __str__(self):
        return str(self.title)


class Room(models.Model):
    """
    The Room table.
    """

    floor = models.ForeignKey(
        Floor, on_delete=models.CASCADE, related_name="floor_rooms"
    )
    title = models.CharField(max_length=200, null=True, blank=True)
    capacity = models.IntegerField(default=0)
    permission_level = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Rooms"
        ordering = ("-created_at",)

    def __str__(self):
        return str(self.title)
