"""Urls for the imager api."""

from django.urls import path
from .views import PhotoListApi, UserApi
from rest_framework.authtoken import views


urlpatterns = [
    path('photos/', PhotoListApi.as_view(), name='photo_list_api'),
    path('user/', UserApi.as_view(), name='user-detail'),
    path('login', views.obtain_auth_token),
]
