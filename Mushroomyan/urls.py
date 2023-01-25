from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("Landing_page.urls")),
    path('user/', include("Customer.urls")),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
