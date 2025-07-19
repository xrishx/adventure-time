from datetime import timedelta

from django.contrib.auth import authenticate, get_user_model

from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from users.models import PasswordResetOTP

from users.serializers.serializers import LoginSerializer, ForgotPasswordSerializer, ResetPasswordSerializer

from django.utils import timezone
 
User = get_user_model()
 
class LoginView(APIView):

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():

            return Response(serializer.errors, status=400)
 
        email = serializer.validated_data['email']

        password = serializer.validated_data['password']

        remember_me = serializer.validated_data['remember_me']
 
        user = authenticate(request, email=email, password=password)

        if not user:

            return Response({"detail": "Invalid credentials"}, status=401)
 
        refresh = RefreshToken.for_user(user)

        if not remember_me:

            # Shorten token lifetime if not remember me (1 hour)

            refresh.set_exp(lifetime=timedelta(hours=1))
 
        return Response({

            'refresh': str(refresh),

            'access': str(refresh.access_token),

        })
 
 
class LogoutView(APIView):

    permission_classes = [IsAuthenticated]
 
    def post(self, request):

        refresh_token = request.data.get('refresh')

        if not refresh_token:

            return Response({"detail": "Refresh token required"}, status=400)
 
        try:

            token = RefreshToken(refresh_token)

            token.blacklist()

            return Response({"detail": "Successfully logged out"}, status=205)

        except Exception:

            return Response({"detail": "Invalid refresh token"}, status=400)
 
 
class ForgotPasswordView(APIView):

    def post(self, request):

        serializer = ForgotPasswordSerializer(data=request.data)

        if not serializer.is_valid():

            return Response(serializer.errors, status=400)
 
        email = serializer.validated_data['email']

        if not User.objects.filter(email=email).exists():

            # Don't reveal user existence, respond success anyway for security

            return Response({"detail": "If that email exists, an OTP was sent."}, status=200)
 
        otp_obj = PasswordResetOTP.objects.create(email=email)

        # For now, print OTP to console (replace with email logic later)

        print(f"OTP for {email}: {otp_obj.otp}")
 
        return Response({"detail": "If that email exists, an OTP was sent."}, status=200)
 
 
class ResetPasswordView(APIView):

    def post(self, request):

        serializer = ResetPasswordSerializer(data=request.data)

        if not serializer.is_valid():

            return Response(serializer.errors, status=400)

        email = serializer.validated_data['email']

        otp = serializer.validated_data['otp']

        new_password = serializer.validated_data['new_password']

        try:

            otp_obj = PasswordResetOTP.objects.filter(email=email, otp=otp).latest('created_at')

        except PasswordResetOTP.DoesNotExist:

            return Response({"detail": "Invalid OTP"}, status=400)

        if otp_obj.is_expired():

            return Response({"detail": "OTP expired"}, status=400)

        try:

            user = User.objects.get(email=email)

            user.set_password(new_password)

            user.save()

            # Delete all OTPs for this email (cleanup)

            PasswordResetOTP.objects.filter(email=email).delete()

            return Response({"detail": "Password reset successful"}, status=200)

        except User.DoesNotExist:

            return Response({"detail": "User not found"}, status=404)

