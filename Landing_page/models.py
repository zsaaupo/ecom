from django.db import models

class Product(models.Model):

    product_name = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to="product/image")
    product_price = models.CharField(max_length=5)
    product_description = models.CharField(max_length=500)

    def __str__(self):
        return self.product_name
