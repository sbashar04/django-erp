from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to="users/avatars/", blank=True, null=True)
    is_company_owner = models.BooleanField(default=False)

    class Role(models.TextChoices):
        SUPER_ADMIN = "SUPER_ADMIN", "Super Admin"
        ADMIN = "ADMIN", "Admin"
        MANAGER = "MANAGER", "Manager"
        ACCOUNTANT = "ACCOUNTANT", "Accountant"
        SALES_PERSON = "SALES_PERSON", "Sales Person"
        STAFF = "STAFF", "Staff"

    role = models.CharField(
        max_length=30,
        choices=Role.choices,
        default=Role.STAFF,
    )

    def __str__(self):
        return self.get_full_name() or self.username
