"""Make the profile view page."""

from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .models import ImagerProfile
from imager_images.models import Album, Photo


class ProfileView(DetailView):
    """Define the ProfileView class."""

    model = ImagerProfile
    template_name = 'imager_profile/profile.html'
    context_object_name = 'profile'
    slug_url_kwarg = 'username'
    slug_field = 'user__username'

    def get(self, *args, **kwargs):
        """Check that user is authenticated, get args and kwargs."""
        if not self.request.user.is_authenticated:
            return redirect('home')
        # import pdb; pdb.set_trace()
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


    
    # num_albums = len(albums)
    # num_photos = len(photos)
    # num_public_albums = len(public_albums)
    # num_public_photos = len(public_photos)

    # context = {
    #     'profile': profile,
    #     'albums': albums,
    #     'photos': photos,
    #     'num_albums': num_albums,
    #     'num_photos': num_photos,
    #     'num_public_albums': num_public_albums,
    #     'num_public_photos': num_public_photos,
    # }

    # return render(request, 'imager_profile/profile.html', context)


# def profile_view(request, username=None):
#     """Define the profile view."""
#     owner = False

#     if not username:
#         username = request.user.get_username()
#         owner = True
#         if username == '':
#             return redirect('home')

#     profile = get_object_or_404(ImagerProfile, user__username=username)
#     albums = Album.objects.filter(user__username=username)
#     photos = Photo.objects.filter(albums__user__username=username)
#     public_photos = photos.filter(published='PUBLIC')
#     public_albums = albums.filter(published='PUBLIC')   

#     if not owner:
#         photos = Photo.objects.filter(published='PUBLIC')
#         albums = Album.objects.filter(published='PUBLIC')

#     num_albums = len(albums)
#     num_photos = len(photos)
#     num_public_albums = len(public_albums)
#     num_public_photos = len(public_photos)

#     context = {
#         'profile': profile,
#         'albums': albums,
#         'photos': photos,
#         'num_albums': num_albums,
#         'num_photos': num_photos,
#         'num_public_albums': num_public_albums,
#         'num_public_photos': num_public_photos,
#     }

#     return render(request, 'imager_profile/profile.html', context)
