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
        profile = ImagerProfile(location='Seattle',
                                website='example.com',
                                fee=0.0,
                                phone=None,
                                camera='NK',
                                services='P',
                                photo_styles='O')

        user = User(password='potatoes', username='zachary')
        user.save()
        profile.user = user
        profile.save()

        photo = Photo(user=profile,
                      image='http://via.placeholder.com/350x150',
                      title='title',
                      description='description of stuff',
                      date_published='1994-10-12',
                      published='PU')
        photo.save()

    def test_user_defaults(self):
        """Test built 50 users and last one has profile with specified settings."""
        one_user = User.objects.get(id=1)
        # import pdb; pdb.set_trace()
        photo = Photo.objects.get(user=one_user.profile)

        self.assertEqual(photo.user.location, "Seattle")
        self.assertEqual(photo.image.name, "http://via.placeholder.com/350x150")
        self.assertEqual(photo.title, "title")
        self.assertEqual(photo.description, "description of stuff")
        self.assertEqual(photo.date_published, datetime.date(datetime(1994, 10, 12)))
        self.assertEqual(photo.published, "PU")
