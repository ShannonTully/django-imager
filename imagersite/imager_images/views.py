"""Views for imager_images."""

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from .models import Album, Photo
from .forms import AlbumForm, PhotoForm
from django.urls import reverse_lazy


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


class AlbumView(ListView):
    """Define the album view class."""

    template_name = 'imager_images/album.html'
    model = Album

    def get(self, *args, **kwargs):
        """Check that user is authenticated, get args and kwargs."""
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """Filter the context for display."""
        context = super().get_context_data(**kwargs)

        public_albums = Album.objects.filter(published='PUBLIC')

        context = {
            'public_albums': public_albums,
        }

        return context


class PhotoView(ListView):
    """Define the album view class."""

    template_name = 'imager_images/photo.html'
    model = Photo

    def get(self, *args, **kwargs):
        """Check that user is authenticated, get args and kwargs."""
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """Filter the context for display."""
        context = super().get_context_data(**kwargs)

        public_photos = Photo.objects.filter(published='PUBLIC')

        context = {
            'public_photos': public_photos,
        }

        return context


class AlbumDetailView(DetailView):
    """Define the album detail view class."""

    template_name = 'imager_images/album_detail.html'
    model = Album
    context_object_name = 'album'
    slug_url_kwarg = 'id'
    slug_field = 'id'

    def get(self, *args, **kwargs):
        """Check that user is authenticated, get args and kwargs."""
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """Filter the context for display."""
        context = super().get_context_data(**kwargs)
        id = context['album'].id
        this_album = Album.objects.filter(id=id).first()

        context = {
            'this_album': this_album,
        }

        return context


class PhotoDetailView(DetailView):
    """Define the album detail view class."""

    template_name = 'imager_images/photo_detail.html'
    model = Photo
    context_object_name = 'photo'
    slug_url_kwarg = 'id'
    slug_field = 'id'

    def get(self, *args, **kwargs):
        """Check that user is authenticated, get args and kwargs."""
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """Filter the context for display."""
        context = super().get_context_data(**kwargs)
        id = context['photo'].id
        this_photo = Photo.objects.filter(id=id).first()

        context = {
            'this_photo': this_photo,
        }

        return context


class AddAlbumView(CreateView):
    """Define the add album view class."""

    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy('library')

    def get(self, *args, **kwargs):
        """Check that user is authenticated, get args and kwargs."""
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        """Check that user is authenticated, get args and kwargs."""
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().post(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.username})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddPhotoView(CreateView):
    """Define the add Photo view class."""

    model = Photo
    form_class = PhotoForm
    success_url = reverse_lazy('library')

    def get(self, *args, **kwargs):
        """Check that user is authenticated, get args and kwargs."""
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        """Check that user is authenticated, get args and kwargs."""
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().post(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.username})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
