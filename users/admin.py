from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

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
        "permission_level",
    )
    ordering = ("-start_date",)
    list_display = (
        "email",
        "user_name",
        "first_name",
        "last_name",
        "profile_picture",
        "company",
        "permission_level",
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
                    "permission_level",
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



admin.site.register(MyUser, UserAdminConfig)
