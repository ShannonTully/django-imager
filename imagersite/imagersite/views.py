"""imagersite views."""

from django.shortcuts import render
from imager_images.models import Photo


def home_view(request):
    """Get the home view."""
    public_photos = Photo.objects.filter(published='PUBLIC')

    context = {
        'public_photos': public_photos,
    }

    return render(request, 'generic/home.html', context)
