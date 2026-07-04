from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_company_owner",
        "is_staff",
        "is_active",
    )

    list_filter = (
        "role",
        "is_company_owner",
        "is_staff",
        "is_active",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "ERP Information",
            {
                "fields": (
                    "phone",
                    "avatar",
                    "role",
                    "is_company_owner",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "ERP Information",
            {
                "fields": (
                    "phone",
                    "role",
                    "is_company_owner",
                )
            },
        ),
    )
