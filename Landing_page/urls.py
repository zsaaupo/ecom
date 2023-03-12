from django.urls import path
from .views import landin_page, ProductApi, order

urlpatterns = [
    path('', landin_page),
    path('order/', order),

    # APIs
    path('product_api', ProductApi.as_view()),
]