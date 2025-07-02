from rest_framework import serializers
from company.legaldocs.models import LegalDocs

class LegalDocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalDocs
        fields = ['id', 'image_file', 'image_link']
        read_only_fields = ['id', 'created_at', 'updated_at']

def validate(self, data):
        image_file = data.get('image_file')
        image_link = data.get('image_link')

        if image_file and image_link:
            raise serializers.ValidationError('Please proivide either image file or image link, not both')

        if not image_file and not image_link:
            raise serializers.ValidationError('Either image file or image link must be provided.')

        return data