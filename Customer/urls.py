from django.urls import path
from .views import sign_up, sign_in, ApiSignUp, ApiOTPCheck, ApiLogIn

urlpatterns = [
    path('join', sign_up),
    path('log_in', sign_in),

    #API
    path('sign_up_api/', ApiSignUp.as_view()),
    path('OTP_check_api/', ApiOTPCheck.as_view()),
    path('login_api/', ApiLogIn.as_view()),
]