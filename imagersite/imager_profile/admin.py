"""Register the models for the admin."""

from django.contrib import admin
from .models import ImagerProfile

# Register your models here.
admin.site.register(ImagerProfile)
