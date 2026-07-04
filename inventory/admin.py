from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sku",
        "selling_price",
        "stock_quantity",
        "low_stock_alert",
        "is_active",
        "created_at",
    )
    search_fields = ("name", "sku", "barcode")
    list_filter = ("is_active", "created_at")
