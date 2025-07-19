from django.urls import path
from users.viewsets.viewsets import (
    LoginView, LogoutView,
    SendOTPView, VerifyOTPView, ResetPasswordView
)
from django.http import JsonResponse

def users_root(request):
    return JsonResponse({'status': 'ok'})

urlpatterns = [
    path('', users_root),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('forgot-password/', SendOTPView.as_view(), name='forgot_password'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
]