from django.urls import path
from .views import landin_page, ProductApi

urlpatterns = [
    path('', landin_page),

    # APIs
    path('product_api', ProductApi.as_view()),
]