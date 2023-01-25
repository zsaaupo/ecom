from django.urls import path
from .views import sing_up, ApiSingUp, ApiOTPCheck

urlpatterns = [
    path('join', sing_up),

    #API
    path('sign_up_api/', ApiSingUp.as_view()),
    path('OTP_check_api/', ApiOTPCheck.as_view()),
]