"""Views for imager_images."""

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView
from .models import Album, Photo
from .forms import AlbumForm, AlbumEditForm, PhotoEditForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class LibraryView(LoginRequiredMixin, ListView):
    """Define the library view class."""

    template_name = 'imager_images/library.html'
    context_object_name = 'albums_and_photos'

    login_url = reverse_lazy('auth_login')

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


class AlbumView(LoginRequiredMixin, ListView):
    """Define the album view class."""

    template_name = 'imager_images/album.html'
    model = Album
    queryset = Album.objects.filter(published='PUBLIC')
    login_url = reverse_lazy('auth_login')
    context_object_name = 'public_albums'


class PhotoView(LoginRequiredMixin, ListView):
    """Define the album view class."""

    template_name = 'imager_images/photo.html'
    model = Photo
    queryset = Photo.objects.filter(published='PUBLIC')
    login_url = reverse_lazy('auth_login')
    context_object_name = 'public_photos'


class AlbumDetailView(LoginRequiredMixin, DetailView):
    """Define the album detail view class."""

    template_name = 'imager_images/album_detail.html'
    model = Album
    context_object_name = 'this_album'
    pk_url_kwarg = 'id'
    login_url = reverse_lazy('auth_login')


class PhotoDetailView(LoginRequiredMixin, DetailView):
    """Define the album detail view class."""

    template_name = 'imager_images/photo_detail.html'
    model = Photo
    context_object_name = 'this_photo'
    pk_url_kwarg = 'id'
    login_url = reverse_lazy('auth_login')


class AddAlbumView(LoginRequiredMixin, CreateView):
    """Define the add album view class."""

    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy('library')
    login_url = reverse_lazy('auth_login')

    def get_form_kwargs(self):
        """Get the username."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.username})
        return kwargs

    def form_valid(self, form):
        """Add the user to the photo."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddPhotoView(LoginRequiredMixin, CreateView):
    """Define the add Photo view class."""

    model = Photo
    fields = ['title', 'description', 'image', 'published']
    # form_class = PhotoForm
    success_url = reverse_lazy('library')
    login_url = reverse_lazy('auth_login')

    # def get_form_kwargs(self):
    #     """Get the username."""
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({'username': self.request.user.username})
    #     return kwargs

    def form_valid(self, form):
        """Add the user to the photo."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class AlbumEditView(LoginRequiredMixin, UpdateView):
    """Define the album edit view."""

    template_name = 'imager_images/album_edit.html'
    model = Album
    form_class = AlbumForm
    login_url = reverse_lazy('auth_login')
    success_url = reverse_lazy('library')
    pk_url_kwarg = 'id'

    def get_form_kwargs(self):
        """Get the form data that is submitted by the album to update the album."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.username})
        return kwargs


class PhotoEditView(LoginRequiredMixin, UpdateView):
    """Define the photo edit view."""

    template_name = 'imager_images/photo_edit.html'
    model = Photo
    form_class = PhotoEditForm
    login_url = reverse_lazy('auth_login')
    success_url = reverse_lazy('library')
    pk_url_kwarg = 'id'
