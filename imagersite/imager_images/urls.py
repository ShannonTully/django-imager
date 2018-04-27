"""Page doc string."""

from django.urls import path
from .views import library_view
# from .imagersite import home_view


urlpatterns = [
    # path('', home_view, name='home'),
    path('library/<str:username>', library_view, name='library'),
]
