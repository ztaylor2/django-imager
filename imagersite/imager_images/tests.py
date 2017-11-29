"""Test imager profile."""
from django.test import TestCase
import factory
from imager_profile.models import ImagerProfile, User
from imager_images.models import Photo, Album
from datetime import datetime


class UserFactory(factory.django.DjangoModelFactory):
    """Factory to create test users."""

    class Meta:
        """User."""

        model = User

    username = factory.Sequence(lambda n: 'zach{}'.format(n))
    email = factory.Sequence(lambda n: 'zach{}@example.com'.format(n))


class PhotoTest(TestCase):
    """Test photo model."""

    def setUp(self):
        """50 users in database last one has profile."""
        user = User(password='potatoes', username='zachary')
        user.save()
        user.profile.location = 'Seattle'
        user.profile.website = 'example.com'
        user.profile.fee = 0.0
        user.profile.phone = None
        user.profile.camera = 'NK'
        user.profile.services = 'P'
        user.profile.photo_styles = 'O'
        user.profile.save()

        photo = Photo(user=user.profile,
                      image='http://via.placeholder.com/350x150',
                      title='photo title',
                      description='description of photo',
                      date_published='1994-10-12',
                      published='PU')
        photo.save()

        album = Album(user=user.profile,
                      image='http://via.placeholder.com/350x150',
                      title='album title',
                      description='description of album',
                      date_published='1994-10-12',
                      published='PU')
        album.photo = photo
        album.save()

    def test_photo_model(self):
        """Test photo model."""
        one_user = User.objects.get(id=1)
        photo = Photo.objects.get(user=one_user.profile)

        self.assertEqual(photo.user.location, "Seattle")
        self.assertEqual(photo.image.name, "http://via.placeholder.com/350x150")
        self.assertEqual(photo.title, "photo title")
        self.assertEqual(photo.description, "description of photo")
        self.assertEqual(photo.date_published, datetime.date(datetime(1994, 10, 12)))
        self.assertEqual(photo.published, "PU")

    def test_album_model(self):
        """Test album model."""
        one_user = User.objects.get(id=1)
        # import pdb; pdb.set_trace()
        album = Album.objects.get(user=one_user.profile)

        self.assertEqual(album.user.location, "Seattle")
        self.assertEqual(album.image.name, "http://via.placeholder.com/350x150")
        self.assertEqual(album.title, "album title")
        self.assertEqual(album.description, "description of album")
        self.assertEqual(album.date_published, datetime.date(datetime(1994, 10, 12)))
        self.assertEqual(album.published, "PU")
