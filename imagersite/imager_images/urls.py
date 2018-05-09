"""Page doc string."""

from django.urls import path
from .views import LibraryView, AlbumView, PhotoView, AlbumDetailView, PhotoDetailView


urlpatterns = [
    path('library/', LibraryView.as_view(), name='library'),
    path('albums/', AlbumView.as_view(), name='album'),
    path('photos/', PhotoView.as_view(), name='photo'),
    path('albums/<int:id>', AlbumDetailView.as_view(), name='album_detail'),
    path('photos/<int:id>', PhotoDetailView.as_view(), name='photo_detail'),
]
