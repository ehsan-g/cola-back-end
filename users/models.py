from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as __


class MyUserManager(BaseUserManager):
    # super user
    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        return self.create_user(email, user_name, first_name, password, **other_fields)

    # normal user
    def create_user(self, email, user_name, first_name, password, **other_fields):
        if not email:
            # _ if translation needed later
            raise ValueError(__("You must provide an email address"))

        email = self.normalize_email(email)
        user = self.model(
            email=email, user_name=user_name, first_name=first_name, **other_fields
        )
        user.set_password(password)
        user.save()
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    NONE = "0"
    PEPSI = "1"
    COKE = "2"

    TYPES = (
        (NONE, "-"),
        (PEPSI, "Pepsi"),
        (COKE, "Coke"),
    )
    company = models.CharField(max_length=20, choices=TYPES, default="0")
    email = models.EmailField(
        verbose_name="email_address", max_length=255, unique=True, blank=False
    )
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    employee_number = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    profile_picture = models.ImageField(upload_to="", blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    wallet_address = models.CharField(max_length=250, null=True, blank=True)
    nft_address = models.CharField(max_length=250, blank=True)
    level = models.IntegerField(default=0)
    objects = MyUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["company", "first_name", "user_name"]
    # Email & Password are required by default

    def __str__(self):
        return self.email
