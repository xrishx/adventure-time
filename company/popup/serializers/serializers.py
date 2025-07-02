from rest_framework import serializers
from company.popup.models import Popup

class PopupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Popup
        fields = ['id', 'title', 'image_file', 'image_link']
        read_only_fields = ['id', 'created_at', 'updated_at']

def validate(self, data):
        image_file = data.get('image_file')
        image_link = data.get('image_link')

        if image_file and image_link:
            raise serializers.ValidationError('Please proivide either image file or image link, not both')

        if not image_file and not image_link:
            raise serializers.ValidationError('Either image file or image link must be provided.')

        return data