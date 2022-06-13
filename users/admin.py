from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea, TextInput

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
    )
    ordering = ("-start_date",)
    list_display = (
        "email",
        "user_name",
        "first_name",
        "last_name",
        "profile_picture",
        "company",
        "is_admin",
        "is_superuser",
        "is_active",
        "is_staff",
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
        ("Permissions", {"fields": ("is_staff", "is_active")}),
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
                ),
            },
        ),
    )


admin.site.register(MyUser, UserAdminConfig)
