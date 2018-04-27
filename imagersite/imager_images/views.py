"""Views for imager_images."""

from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Photo
from django.contrib.auth.models import User


def library_view(request, username=None):
    """Define the library view."""
    owner = False

    if not username:
        username = request.user.get_username()
        owner = True
        if username == '':
            return redirect('home')
    # import pdb; pdb.set_trace()
    profile = get_object_or_404(User, username=username)
    albums = Album.objects.filter(user__username=username)
    photos = Photo.objects.filter(user__username=username)
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

    return render(request, 'imager_images/library.html', context)


def album_view(request):
    """Define the library view."""
    public_albums = Album.objects.filter(published='PUBLIC')

    num_public_albums = len(public_albums)

    context = {
        'public_albums': public_albums,
        'num_public_albums': num_public_albums,
    }

    return render(request, 'imager_images/album.html', context)


def photo_view(request):
    """Define the library view."""
    public_photos = Photo.objects.filter(published='PUBLIC')

    num_public_photos = len(public_photos)

    context = {
        'public_photos': num_public_photos,
        'num_public_photos': num_public_photos,
    }

    return render(request, 'imager_images/photo.html', context)


def album_detail_view(request):
    """Define the library view."""
    public_albums = Album.objects.filter(published='PUBLIC')

    num_public_albums = len(public_albums)

    context = {
        'public_albums': public_albums,
        'num_public_albums': num_public_albums,
    }

    return render(request, 'imager_images/album.html', context)


def photo_detail_view(request):
    """Define the library view."""
    public_photos = Photo.objects.filter(published='PUBLIC')

    num_public_photos = len(public_photos)

    context = {
        'public_photos': num_public_photos,
        'num_public_photos': num_public_photos,
    }

    return render(request, 'imager_images/photo.html', context)
