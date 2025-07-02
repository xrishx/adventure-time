from rest_framework import serializers
from blog.models import Blog

class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'reading_time', 'description', 'image_file', 'popular']

class BlogReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'created_at', 'updated_at', 'title', 'reading_time', 'popular']