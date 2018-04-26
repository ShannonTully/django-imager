"""Make the profile view page."""

from django.shortcuts import render, redirect, get_object_or_404
from .models import ImagerProfile
from imager_images.models import Album, Photo


def profile_view(request, username=None):
    """Define the profive view."""
    owner = False

    if not username:
        username = request.user.get_username()
        owner = True
        if username == '':
            return redirect('home')

    profile = get_object_or_404(ImagerProfile, user__username=username)
    albums = Album.objects.filter(user__username=username)
    photos = Photo.objects.filter(album__user__username=username)

    if not owner:
        photos = Photo.objects.filter(published='PUBLIC')
        albums = Album.objects.filter(published='PUBLIC')

    context = {
        'profile': profile,
        'albums': albums,
        'photos': photos
    }

    return render(request, 'imager_profile/profile.html', context)
