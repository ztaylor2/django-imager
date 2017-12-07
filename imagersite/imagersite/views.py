"""Views."""
from django.template import loader
from django.shortcuts import render
from django.views import generic
from imager_profile.models import ImagerProfile
import random


class HomeView(generic.ListView):
    """Home page view."""
    model = ImagerProfile
    template_name = 'imagersite/home.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        """."""
        context = super(HomeView, self).get_context_data(**kwargs)
        photos = context['data'][2].photo.all()
        rand_photo_index = random.randint(0, len(photos) - 1)
        photo_url = photos[rand_photo_index].image.url

        context['data'] = {
            'photo': photo_url,
        }

        return context
