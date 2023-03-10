from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):

    list_display = [
        "product_name",
        "product_image",
        "product_description"
    ]

admin.site.register(Product,ProductAdmin)