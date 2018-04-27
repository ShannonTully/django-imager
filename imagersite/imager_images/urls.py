"""Page doc string."""

from django.urls import path
from .views import library_view, album_view, photo_view, album_detail_view, photo_detail_view


urlpatterns = [
    path('library/', library_view, name='library'),
    path('albums/', album_view, name='album'),
    path('photos/', photo_view, name='photo'),
    path('albums/<int:id>', album_detail_view, name='album_detail'),
    path('photos/<int:id>', photo_detail_view, name='photo_detail'),
]
