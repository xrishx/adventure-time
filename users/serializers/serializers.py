from rest_framework import serializers
from django.contrib.auth import authenticate
from users.models import User, OTP
from django.core.mail import send_mail

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    remember_me = serializers.BooleanField(default=False)

class SendOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email doesn't exist.")
        return value

    def save(self):
        email = self.validated_data['email']
        otp_obj = OTP.objects.create(email=email)
        send_mail(
            'Your OTP Code',
            f'Your OTP is {otp_obj.code}',
            'noreply@example.com',
            [email],
        )

class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=5)

    def validate(self, data):
        if not OTP.objects.filter(email=data['email'], code=data['code']).exists():
            raise serializers.ValidationError("Invalid OTP")
        return data

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def save(self):
        user = User.objects.get(email=self.validated_data['email'])
        user.set_password(self.validated_data['new_password'])
        user.save()