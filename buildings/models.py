from django.db import models
from django.urls import reverse
from users.models import MyUser
from django.utils.translation import gettext_lazy as _

#  Building.objects.get_queryset() / to return only active ones
class BuildingManager(models.Manager):
    def get_queryset(self):
        return super(BuildingManager, self).get_queryset().filter(is_active=True)


class Address(models.Model):
    """
    The Address table.
    """

    country = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Addresses"
        ordering = ("-created_at",)

    # e.g in django template,get URL links for all buildings by calling this
    def __str__(self):
        return str(self.address)


class Building(models.Model):
    """
    The Building table.
    """

    NONE = "0"
    PEPSI = "1"
    COKE = "2"

    TYPES = (
        (NONE, "-"),
        (PEPSI, "Pepsi"),
        (COKE, "Coke"),
    )
    company = models.CharField(max_length=20, choices=TYPES, default="0")
    building_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    objects = BuildingManager()
    created_by = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name="building_creator",
        default=MyUser,
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name="building_address",
        default=Address,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

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

    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, related_name="building_image"
    )
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a building image"),
        upload_to="images/",
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
