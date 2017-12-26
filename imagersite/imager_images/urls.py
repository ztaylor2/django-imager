"""Imager profile app urls."""
from django.conf.urls import url

from imager_images.views import LibraryView, PhotoView, AlbumView, AlbumGalleryView, PhotoGalleryView, NewAlbumView, NewPhotoView, EditPhotoView, EditAlbumView

urlpatterns = [
    url(r'^library/',
        LibraryView.as_view(),
        name='library'),
    url(r'^albums/(?P<pk>\d+)/$',
        AlbumView.as_view(template_name='imager_images/album.html'),
        name='album'),
    url(r'^albums/$', AlbumGalleryView.as_view(), name='albums'),
    url(r'^photos/(?P<pk>\d+)/$',
        PhotoView.as_view(template_name='imager_images/photo.html'),
        name='photo'),
    url(r'^photos/$', PhotoGalleryView.as_view(), name='photos'),
    url(r'^albums/add/$', NewAlbumView.as_view(), name='add_album'),
    url(r'^photos/add/$', NewPhotoView.as_view(), name='add_photo'),
    url(r'^photos/(?P<pk>\d+)/edit$', EditPhotoView.as_view(), name='edit_photo'),
    url(r'^albums/(?P<pk>\d+)/edit$', EditAlbumView.as_view(), name='edit_album'),
]
