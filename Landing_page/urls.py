from django.urls import path
from .views import landin_page

urlpatterns = [
    path('', landin_page),
]