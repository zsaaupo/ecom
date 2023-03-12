from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product


def landin_page(request):
    return render(request, "index.html")


def order(request):
    return render(request, "order.html")


class ProductApi(ListAPIView):

    permission_classes = []

    def get(self, request):

        product_data = Product.objects.filter().all()
        product_data = ProductSerializer(product_data, many=True).data

        return Response(product_data)