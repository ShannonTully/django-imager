"""Serializers for the imager api."""

from rest_framework import serializers
from imager_images.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    """Serializer for the Photo model."""

    class Meta:
        model = Photo
        fields = ('id', 'title', 'description', 'image', 'published')
