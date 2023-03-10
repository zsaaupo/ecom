from django.contrib import admin
from django.urls import path, include
from .settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include("Landing_page.urls")),
    path('user/', include("Customer.urls")),
    path('api-auth/', include('rest_framework.urls')),

]+static(MEDIA_URL, document_root=MEDIA_ROOT)
