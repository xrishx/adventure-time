from rest_framework import serializers
from reviews.models import Review

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'review', 'image']

class ReviewReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'created_at', 'name', 'rating', 'review', 'image', 'show']
        

