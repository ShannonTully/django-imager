"""This is where the forms are defined."""

from django.forms import ModelForm
from .models import Album, Photo


class AlbumForm(ModelForm):
    """Define the Album form."""

    class Meta:
        """Meta data for album form."""

        model = Album
        fields = ['cover', 'title', 'description', 'published']

    def __init__(self, *args, **kwargs):
        """Init for album form."""
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)
        self.fields['cover'].queryset = Photo.objects.filter(albums__user__username=username)


class PhotoForm(ModelForm):
    """Define the Photo form."""

    class Meta:
        """Meta data for Photo form."""

        model = Photo
        fields = ['albums', 'title', 'description', 'image', 'published']

    def __init__(self, *args, **kwargs):
        """Init for Photo form."""
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)
        self.fields['albums'].queryset = Album.objects.filter(user__username=username)


class AlbumEditForm(ModelForm):
    """Define the album edit class."""

    class Meta:
        """Define the meta data for the form."""

        model = Album
        fields = ['cover', 'title', 'description', 'published']

    def __init__(self, *args, **kwargs):
        """Set the initial form fields to be filled."""
        super().__init__(*args, **kwargs)


class PhotoEditForm(ModelForm):
    """Define the photo edit class."""

    class Meta:
        """Define the meta data for the form."""

        model = Photo
        fields = ['title', 'description', 'published']

    def __init__(self, *args, **kwargs):
        """Set the initial form fields to be filled."""
        super().__init__(*args, **kwargs)
