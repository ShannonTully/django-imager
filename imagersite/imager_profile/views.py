"""Make the profile view page."""

from django.shortcuts import render, redirect, get_object_or_404
from .models import ImagerProfile
from imager_images.models import Album, Photo


def profile_view(request, username=None):
    """Define the profile view."""
    owner = False

    if not username:
        username = request.user.get_username()
        owner = True
        if username == '':
            return redirect('home')

    profile = get_object_or_404(ImagerProfile, user__username=username)
    albums = Album.objects.filter(user__username=username)
    photos = Photo.objects.filter(album__user__username=username)
    public_photos = photos.filter(published='PUBLIC')
    public_albums = albums.filter(published='PUBLIC')    

    if not owner:
        photos = Photo.objects.filter(published='PUBLIC')
        albums = Album.objects.filter(published='PUBLIC')

    num_albums = len(albums)
    num_photos = len(photos)
    num_public_albums = len(public_albums)
    num_public_photos = len(public_photos)

    context = {
        'profile': profile,
        'albums': albums,
        'photos': photos,
        'num_albums': num_albums,
        'num_photos': num_photos,
        'num_public_albums': num_public_albums,
        'num_public_photos': num_public_photos,
    }

    return render(request, 'imager_profile/profile.html', context)


