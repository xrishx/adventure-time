from rest_framework import serializers
from reviews.models import Review

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user','name', 'rating', 'review', 'image']
        read_only_fields = ['user', 'created_at']

class ReviewReadSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Review
        fields = ['id','user', 'created_at', 'name', 'rating', 'review', 'image', 'show']
        

