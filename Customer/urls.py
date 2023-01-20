from django.urls import path
from .views import sing_up

urlpatterns = [
    path('join', sing_up),
]