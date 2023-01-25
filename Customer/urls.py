from django.urls import path
from .views import sing_up, ApiSingUp

urlpatterns = [
    path('join', sing_up),

    #API
    path('sign_up_api/', ApiSingUp.as_view()),
]