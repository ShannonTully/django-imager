"""Make the profile view page."""

from django.views.generic.detail import DetailView
from django.views.generic import UpdateView
from django.shortcuts import redirect
from .models import ImagerProfile
from .forms import ProfileEditForm
from imager_images.models import Album, Photo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ProfileView(LoginRequiredMixin, DetailView):
    """Define the ProfileView class."""

    model = ImagerProfile
    template_name = 'imager_profile/profile.html'
    context_object_name = 'profile'
    slug_url_kwarg = 'username'
    slug_field = 'user__username'

    login_url = reverse_lazy('auth_login')

    def get(self, *args, **kwargs):
        """Get args and kwargs."""
        if self.kwargs == {}:
            self.kwargs['username'] = self.request.user.get_username()

        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """Get all the context, filter and determine what to display by username."""
        context = super().get_context_data(**kwargs)
        username = context['profile'].user.username
        owner = False
        if username == '':
            username = self.request.user.get_username()
            owner = True
            if username == '':
                return redirect('home')
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
        context.update({
            'albums': albums,
            'photos': photos,
            'num_albums': num_albums,
            'num_photos': num_photos,
            'num_public_albums': num_public_albums,
            'num_public_photos': num_public_photos,
        })
        return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    """Define the profile edit view."""

    template_name = 'imager_profile/profile_edit.html'
    model = ImagerProfile
    form_class = ProfileEditForm
    login_url = reverse_lazy('auth_login')
    success_url = reverse_lazy('profile')
    slug_url_kwarg = 'username'
    slug_field = 'user__username'

    def get(self, *args, **kwargs):
        """Get the args and kwargs for the authorized user."""
        self.kwargs['username'] = self.request.user.get_username()
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        """Post the new args and kwargs for the user."""
        self.kwargs['username'] = self.request.user.get_username()
        return super().post(*args, **kwargs)

    def get_form_kwargs(self):
        """Get the form data that is submitted by the user to update their profile."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.get_username()})
        return kwargs

    def form_valid(self, form):
        """Check that the form information is valid, then save the data."""
        form.instance.user.email = form.data['email']
        form.instance.user.first_name = form.data['first_name']
        form.instance.user.last_name = form.data['last_name']
        form.instance.user.save()
        return super().form_valid(form)
