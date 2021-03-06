"""Page doc string."""

from django.urls import path
from .views import LibraryView, AlbumView, PhotoView, AlbumDetailView, PhotoDetailView, AddAlbumView, AddPhotoView, AlbumEditView, PhotoEditView


urlpatterns = [
    path('library/', LibraryView.as_view(), name='library'),
    path('albums/', AlbumView.as_view(), name='album'),
    path('photos/', PhotoView.as_view(), name='photo'),
    path('albums/<int:id>', AlbumDetailView.as_view(), name='album_detail'),
    path('photos/<int:id>', PhotoDetailView.as_view(), name='photo_detail'),
    path('albums/<int:id>/edit/', AlbumEditView.as_view(), name='album_edit'),
    path('photos/<int:id>/edit/', PhotoEditView.as_view(), name='photo_edit'),
    path('albums/add/', AddAlbumView.as_view(), name='add_album'),
    path('photos/add/', AddPhotoView.as_view(), name='add_photo'),
]
