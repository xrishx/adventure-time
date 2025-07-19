from rest_framework import serializers
from adventure.package.models import Package

class PackageWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['name', 'package_image']

class PackageReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'package_image', 'name']

