"""imagersite views."""

from django.shortcuts import render


def home_view(request):
    """Get the home view."""
    return render(request, 'generic/home.html')
