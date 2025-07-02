from rest_framework import serializers
from company.homepage.models import HomepageVideo

class HomepageVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomepageVideo
        fields = ['id', 'video_file', 'video_link', 'position']
        read_only_fields = ['id', 'created_at', 'updated_at']

def validate(self, data):
        video_file = data.get('video_file')
        video_link = data.get('video_link')

        if video_file and video_link:
            raise serializers.ValidationError('Please proivide either video file or video link, not both')

        if not video_file and not video_link:
            raise serializers.ValidationError('Either video file or video link must be provided.')

        return data
