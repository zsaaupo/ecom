from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("Landing_page.urls")),
    path('admin/', admin.site.urls),
]
