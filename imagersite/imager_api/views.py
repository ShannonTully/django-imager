"""Views for the imager api."""

from rest_framework import generics
from .serializers import PhotoSerializer
from imager_images.models import Photo


class PhotoListApi(generics.ListAPIView):
    """Api for the photos."""

    serializer_class = PhotoSerializer

    def get_queryset(self):
        """Overwrite django get queryset to get photos where the owner is the user."""
        return Photo.objects.filter(user=self.request.user)