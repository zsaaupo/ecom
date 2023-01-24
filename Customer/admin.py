from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):

    list_display = [
        "full_name",
        "phone_number"
    ]

admin.site.register(Customer, CustomerAdmin)