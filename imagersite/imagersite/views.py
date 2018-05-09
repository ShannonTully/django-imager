"""Define the imagersite home view."""

from django.views.generic.base import TemplateView
from imager_images.models import Photo


class HomeView(TemplateView):
    """Make the HomeView class."""

    template_name = 'generic/home.html'

    def get_context_data(self, **kwargs):
        """Get the context to fill the page."""
        context = super().get_context_data(**kwargs)

        public_photos = Photo.objects.filter(published='PUBLIC')

        if public_photos.count():
            image = public_photos.order_by('?').first()
            image_url = image.image.url
            image_title = image.title

        else:
            image_url = 'media/images/Honey_Hug.jpg'
            image_title = 'HoneyHug'

        context['image_url'] = image_url
        context['image_title'] = image_title

        return context
