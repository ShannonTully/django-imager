"""Page doc string."""

from django.urls import path
from .views import profile_view


urlpatterns = [
    path('', profile_view, name='profile'),
    path('<str:username>', profile_view, name='named_profile'),
    path('settings/<str:username>', profile_view, name='settings')  # The view is not correct here. You need to define settings_view
]
