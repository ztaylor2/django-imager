from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView
from imager_profile.models import ImagerProfile

from imager_images.models import Album, Photo


class LibraryView(ListView):
    """Library view."""
    model = ImagerProfile
    template_name = 'imager_images/library.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        """."""
        context = super(LibraryView, self).get_context_data(**kwargs)
        photos = context['data'][2].photo.all()
        albums = context['data'][2].album.all()
        # import pdb; pdb.set_trace()
        num_photos = len(photos)
        num_albums = len(albums)

        context['data'] = {
            'num_photos': num_photos,
            'num_albums': num_albums,
            'photos': photos,
            'albums': albums,
        }

        return context


class PhotoView(TemplateView):
    """Photo view class based view."""

    def get_context_data(self, pk=None):
        """Get context data for view."""
        photo = Photo.objects.get(id=pk)
        return {'photo': photo}


class AlbumView(TemplateView):
    """Album view class based view."""

    def get_context_data(self, pk=None):
        """Get context data for view."""
        album = Album.objects.get(id=pk)
        return {'album': album}
