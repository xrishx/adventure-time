from rest_framework import serializers
from adventure.collection.models import Collection

class CollectionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['name', 'destination']

class CollectionReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name', 'destination']

