from django.urls import path
from users.viewsets.viewsets import (
    LoginView,
    LogoutView,
    ForgotPasswordView,
    ResetPasswordView
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
]