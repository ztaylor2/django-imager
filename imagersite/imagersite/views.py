"""Views."""
from django.views import generic
from imager_profile.models import ImagerProfile
import random
from django.conf import settings


class HomeView(generic.ListView):
    """Home page view."""
    model = ImagerProfile
    template_name = 'imagersite/home.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        """."""
        context = super(HomeView, self).get_context_data(**kwargs)
        if context['data']:
            while True:
                photos = random.choice(context['data']).photo.all()
                try:
                    rand_photo_index = random.randint(0, len(photos) - 1)
                except ValueError:
                    continue
                photo_url = photos[rand_photo_index].image.url
                break
        else:
            photo_url = settings.STATIC_URL + 'imagersite/noimageavailable.png'
        context['data'] = {
            'photo': photo_url,
        }

        return context
