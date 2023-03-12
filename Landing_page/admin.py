from django.contrib import admin
from .models import Product, Order

class ProductAdmin(admin.ModelAdmin):

    list_display = [
        "product_name",
        "product_image",
        "product_price",
        "delivery_charge",
        "product_description"
    ]

admin.site.register(Product,ProductAdmin)


class OrderAdmit(admin.ModelAdmin):

    list_display = [
        "order_number",
        "customer",
        "kg",
        "total_price"
    ]

admin.site.register(Order,OrderAdmit)