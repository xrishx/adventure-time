from rest_framework import serializers
from queries.models import Query

class QueryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ['name', 'phone_number', 'message']

class QueryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ['id', 'created_at', 'name', 'phone_number', 'message']

        