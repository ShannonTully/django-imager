from django.shortcuts import render, redirect
from .models import ImagerProfile
from imager_images.models import Album, Photo


# Create your views here.
def profile_view(request, username=None):
    """Doc string."""
    owner = False

    if not username:
        username = request.user.get_username()
        if username == '':
            return redirect('home')

    profile = get_object_or_404(ImagerProfile, user__username=username)
    albums = Album.objects.filter(user__username=username)
    photos = Photo.objects.filter(albums__user__username=usermane)

    if not owner:
        photos = Photo.objects.filter(published='PUBLIC')
        albums = Album.objects.filter(published='PUBLIC')

    context = {
        'profile': profile'
        'albums': albums,
        'photos': photos
    }

    return render(request, 'profile.html', context)