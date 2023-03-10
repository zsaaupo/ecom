from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = ["product_name", "product_image", "product_price", "product_description"]