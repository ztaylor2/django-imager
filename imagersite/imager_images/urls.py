"""Imager profile app urls."""
from django.conf.urls import url

from imager_images.views import LibraryView, PhotoView, AlbumView

urlpatterns = [
    url(r'^library/',
        LibraryView.as_view(),
        name='library'),
    url(r'^albums/(?P<pk>\d+)/$',
        AlbumView.as_view(template_name='imager_images/album.html'),
        name='album'),
    url(r'^photos/(?P<pk>\d+)/$',
        PhotoView.as_view(template_name='imager_images/photo.html'),
        name='photo'),
]
