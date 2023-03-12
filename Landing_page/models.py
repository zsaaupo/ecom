from django.db import models
from Customer.models import Customer
class Product(models.Model):

    product_name = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to="product/image")
    product_price = models.CharField(max_length=5)
    delivery_charge = models.PositiveIntegerField()
    product_description = models.CharField(max_length=500)

    def __str__(self):
        return self.product_name

class Order(models.Model):

    order_number = models.CharField(max_length=6)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    kg = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()

    def __str__(self):
        return self.order_number