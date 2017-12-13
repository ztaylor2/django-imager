"""Views for profile."""
from django.views import generic
from imager_profile.models import ImagerProfile
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from imager_images.models import Photo
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy


class ProfileView(generic.ListView):
    """Profile page view."""

    model = ImagerProfile
    template_name = 'imager_profile/profile.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        """Get data."""
        context = super(ProfileView, self).get_context_data(**kwargs)
        photos = context['data'][2].photo.all()
        photo_url = photos[0].image.url
        num_photos = len(photos)
        num_albums = context['data'][2].album.all().count()
        context['data'] = {
            'photo_url': photo_url,
            'num_photos': num_photos,
            'num_albums': num_albums,
        }

        return context


class GuestView(TemplateView):
    """Guest profile page view."""

    model = ImagerProfile
    template_name = 'imager_profile/guest_profile.html'
    context_object_name = 'data'

    def get_context_data(self, username=None):
        """."""
        # import pdb; pdb.set_trace()
        user = get_object_or_404(User, username=username)
        # user = User.objects.get(username=username)
        photo = Photo.objects.order_by('?').first()
        return {'photo': photo,
                'user': user}


class UpdateProfile(generic.UpdateView):
    """Update profile view."""

    model = ImagerProfile
    template_name = 'imager_profile/update_profile.html'
    fields = ['website', 'fee', 'camera', 'services', 'bio', 'phone', 'photo_styles']
    success_url = reverse_lazy('profile')
