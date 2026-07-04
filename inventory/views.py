from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def inventory_view(request):
    products = [
        {
            "name": "Paracetamol 500mg",
            "sku": "MED-001",
            "category": "Medicine",
            "stock": 120,
            "price": 2.50,
            "status": "In Stock",
        },
        {
            "name": "Napa Extra",
            "sku": "MED-002",
            "category": "Medicine",
            "stock": 8,
            "price": 3.00,
            "status": "Low Stock",
        },
        {
            "name": "Hand Sanitizer",
            "sku": "GEN-001",
            "category": "General",
            "stock": 0,
            "price": 80.00,
            "status": "Out of Stock",
        },
    ]

    context = {
        "products": products,
        "total_products": len(products),
        "in_stock": 1,
        "low_stock": 1,
        "out_of_stock": 1,
    }

    return render(request, "index.html", context)
