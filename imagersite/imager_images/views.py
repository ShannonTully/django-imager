"""Views for imager_images."""

from django.views.generic.list import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Photo
from django.contrib.auth.models import User


class LibraryView(ListView):
    """Define the library view class."""

    template_name = 'imager_images/library.html'
    context_object_name = 'albums_and_photos'

    def get(self, *args, **kwargs):
        """Check that user is authenticated, get args and kwargs."""
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().get(*args, **kwargs)

    def get_queryset(self):
        """Get the context to display."""
        username = self.request.user.get_username()
        albums = Album.objects.filter(user__username=username)
        photos = Photo.objects.filter(user__username=username)

        return albums, photos     

    def get_context_data(self, **kwargs):
        """Filter the context for display."""
        context = super().get_context_data(**kwargs)
        albums = context['albums_and_photos'][0]
        photos = context['albums_and_photos'][1]

        context.update({
            'albums': albums,
            'photos': photos,
        })

        return context












# def library_view(request):
#     """Define the library view."""
#     username = request.user.get_username()

#     if username == '':
#         return redirect('home')
#     profile = get_object_or_404(User, username=username)
#     albums = Album.objects.filter(user__username=username)
#     photos = Photo.objects.filter(user__username=username)

#     context = {
#         'profile': profile,
#         'albums': albums,
#         'photos': photos,
#     }

#     return render(request, 'imager_images/library.html', context)


# def album_view(request):
#     """Define the library view."""
#     public_albums = Album.objects.filter(published='PUBLIC')

#     context = {
#         'public_albums': public_albums,
#     }

#     return render(request, 'imager_images/album.html', context)


# def photo_view(request):
#     """Define the library view."""
#     public_photos = Photo.objects.filter(published='PUBLIC')

#     context = {
#         'public_photos': public_photos,
#     }

#     return render(request, 'imager_images/photo.html', context)


# def album_detail_view(request, id=None):
#     """Define the library view."""
#     this_album = Album.objects.filter(id=id).first()

#     context = {
#         'this_album': this_album,
#     }

#     return render(request, 'imager_images/album_detail.html', context)


# def photo_detail_view(request, id=None):
#     """Define the library view."""
#     this_photo = Photo.objects.filter(id=id).first()

#     context = {
#         'this_photo': this_photo,
#     }

#     return render(request, 'imager_images/photo_detail.html', context)
