from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from imager_profile.models import ImagerProfile
from django.core.urlresolvers import reverse_lazy
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


class PhotoGalleryView(ListView):
    """All photos view."""

    model = ImagerProfile
    template_name = 'imager_images/photo_gallery.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        """."""
        context = super(PhotoGalleryView, self).get_context_data(**kwargs)
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


class AlbumView(TemplateView):
    """Album view class based view."""

    def get_context_data(self, pk=None):
        """Get context data for view."""
        album = Album.objects.get(id=pk)
        return {'album': album}


class AlbumGalleryView(ListView):
    """All albums based view."""

    model = ImagerProfile
    template_name = 'imager_images/album_gallery.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        """."""
        context = super(AlbumGalleryView, self).get_context_data(**kwargs)
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


class NewPhotoView(CreateView):
    """View to create new photo."""

    model = Photo
    template_name = 'imager_images/add_photo.html'
    fields = ['user', 'image', 'title', 'description', 'published', 'date_published']
    success_url = reverse_lazy('library')


class NewAlbumView(CreateView):
    """View to create new album."""

    model = Album
    template_name = 'imager_images/add_album.html'
    fields = ['user', 'photo', 'title', 'description', 'cover', 'published', 'date_published']
    success_url = reverse_lazy('library')


class EditPhotoView(UpdateView):
    """View to edit photo."""

    model = Photo
    template_name = 'imager_images/edit_photo.html'
    fields = ['user', 'image', 'title', 'description', 'published']
    success_url = reverse_lazy('library')


class EditAlbumView(UpdateView):
    """View to add album."""

    model = Album
    template_name = 'imager_images/edit_album.html'
    fields = ['user', 'photo', 'title', 'description', 'cover', 'published']
    success_url = reverse_lazy('library')
