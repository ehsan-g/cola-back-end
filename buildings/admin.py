from django.contrib import admin
from buildings.models import Building, BuildingImage, Address


class BuildingImageInline(admin.StackedInline):
    model = BuildingImage


class AddressInline(admin.StackedInline):
    model = Address


class BuildingAdminConfig(admin.ModelAdmin):
    model = Building
    inlines = [BuildingImageInline, AddressInline]
    list_display = ["building_name", "company", "is_active", "slug", "created_at"]
    list_filter = ["building_name", "company"]
    list_editable = ["is_active"]

    prepopulated_fields = {"slug": ("building_name",)}


admin.site.register(Building, BuildingAdminConfig)
