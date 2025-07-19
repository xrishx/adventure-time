from rest_framework import serializers
from adventure.activities.models import Activity

class ActivityWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['name', 'destination', 'image']

class ActivityReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'image', 'name', 'destination']