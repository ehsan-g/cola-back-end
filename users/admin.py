from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from buildings.models import Building, BuildingImage, Address

from .models import (
    MyUser,
)


class UserAdminConfig(UserAdmin):
    model = MyUser
    search_fields = ("email", "user_name", "first_name", "last_name", "profile_picture")
    list_filter = (
        "company",
        "email",
        "user_name",
        "first_name",
        "level",
    )
    ordering = ("-start_date",)
    list_display = (
        "email",
        "user_name",
        "first_name",
        "last_name",
        "profile_picture",
        "company",
        "level",
        "is_active",
        "is_admin",
        "is_staff",
        "is_superuser",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "company",
                    "email",
                    "user_name",
                    "first_name",
                    "last_name",
                    "profile_picture",
                    "nft_address",
                    "wallet_address",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_admin",
                    "level",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "company",
                    "employee_number",
                    "email",
                    "user_name",
                    "first_name",
                    "last_name",
                    "profile_picture",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_admin",
                ),
            },
        ),
    )


class BuildingAdminConfig(admin.ModelAdmin):
    model = Building
    list_display = ["building_name", "company", "is_active", "slug", "created_at"]
    list_filter = ["building_name", "company"]
    list_editable = ["is_active"]

    prepopulated_fields = {"slug": ("building_name",)}


class AddressAdminConfig(admin.ModelAdmin):
    model = Address


class BuildingImageAdminConfig(admin.ModelAdmin):
    model = BuildingImage


admin.site.register(MyUser, UserAdminConfig)
admin.site.register(Building, BuildingAdminConfig)
admin.site.register(BuildingImage, BuildingImageAdminConfig)
admin.site.register(Address, AddressAdminConfig)
