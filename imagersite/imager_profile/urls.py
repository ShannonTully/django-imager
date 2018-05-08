"""Page doc string."""

from django.urls import path
from .views import ProfileView


urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('<str:username>', ProfileView.as_view(), name='named_profile'),
]
