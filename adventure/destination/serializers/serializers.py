from rest_framework import serializers
from adventure.destination.models import Destination, Departure, GalleryImage 
from adventure.package.models import Package

class DestinationReadSerializer(serializers.ModelSerializer):
    package = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Destination
        fields = ['id', 'title', 'package']

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'image']

class DepartureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departure
        fields = ['id', 'start_date', 'end_date', 'price', 'currency', 'status']

class DestinationWriteSerializer(serializers.ModelSerializer):
    departures = DepartureSerializer(many=True, required=False)
    gallery_images = GalleryImageSerializer(many=True, required=False)
    package = serializers.PrimaryKeyRelatedField(
        queryset=Package.objects.all(), many=True)

    class Meta:
        model = Destination
        fields = [
            'id', 'title', 'package', 'price', 'currency', 'is_allowed',
            'feature_image', 'trip_pdf',
            'overview', 'inclusion_exclusions', 'itinerary', 'trip_map', 'trip_map_link',
            'gear_equipment', 'useful_info',
            'duration', 'trip_grade', 'best_season', 'max_altitude', 'meals',
            'nature_of_trip', 'accomodation', 'group_size',
            'meta_keywords', 'meta_descrip',
            'departures', 'gallery_images',
        ]

    def create(self, validated_data):
        departures_data = validated_data.pop('departures', [])
        gallery_images_data = validated_data.pop('gallery_images', [])
        packages = validated_data.pop('package', [])

        destination = Destination.objects.create(**validated_data)
        destination.package.set(packages)

        for dep_data in departures_data:
            Departure.objects.create(destination=destination, **dep_data)

        for img_data in gallery_images_data:
            GalleryImage.objects.create(destination=destination, **img_data)

        return destination

    def update(self, instance, validated_data):
        departures_data = validated_data.pop('departures', [])
        gallery_images_data = validated_data.pop('gallery_images', [])
        packages = validated_data.pop('package', [])

        # Update basic fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if packages:
            instance.package.set(packages)

        # Clear existing departures and create new ones (or update logic can be implemented)
        if departures_data:
            instance.departures.all().delete()
            for dep_data in departures_data:
                Departure.objects.create(destination=instance, **dep_data)
                
        # Clear existing gallery images and create new ones
        if gallery_images_data:
            instance.gallery_images.all().delete()
            for img_data in gallery_images_data:
                GalleryImage.objects.create(destination=instance, **img_data)

        return instance