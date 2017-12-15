"""Views."""
from django.views import generic
from imager_profile.models import ImagerProfile
import random
from django.conf import settings
from imager_images.models import Photo


class HomeView(generic.ListView):
    """Home page view."""

    model = ImagerProfile
    template_name = 'imagersite/home.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        """."""
        context = super(HomeView, self).get_context_data(**kwargs)
        photos = Photo.objects.all()
        if photos:
            photo_url = random.choice(photos).image.url
        else:
            photo_url = settings.STATIC_URL + 'imagersite/noimageavailable.png'
        context['data'] = {
            'photo': photo_url,
        }

        return context
