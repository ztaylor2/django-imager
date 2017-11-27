"""Test imager profile."""
from django.test import TestCase
import factory
from imager_profile.models import ImagerProfile, User


class UserFactory(factory.django.DjangoModelFactory):
    """Factory to create test users."""

    class Meta:
        """User."""

        model = User

    username = factory.Sequence(lambda n: 'zach{}'.format(n))
    email = factory.Sequence(lambda n: 'zach{}@example.com'.format(n))


class ProfileTest(TestCase):
    """Test profile connection to user."""

    def setUp(self):
        """50 users in database last one has profile."""
        profile = ImagerProfile(location='Seattle',
                                website='example.com',
                                fee=0.0,
                                phone=None,
                                camera='NK',
                                services='P',
                                photo_styles='O')
        for i in range(50):
            user = UserFactory.create()
            user.set_password('potatoes')
            user.save()

        profile.user = user
        profile.save()

    def test_user_defaults(self):
        """Test built 50 users and last one has profile with specified settings."""
        one_user = User.objects.get(id=50)
        all_users = User.objects.all()
        website = one_user.profile.website
        location = one_user.profile.location
        fee = one_user.profile.fee
        phone = one_user.profile.phone
        camera = one_user.profile.camera
        services = one_user.profile.services
        photo_styles = one_user.profile.photo_styles
        self.assertIsNotNone(one_user.profile)
        self.assertEqual(len(all_users), 50)
        self.assertEqual(str(one_user), "zach49")
        self.assertEqual(one_user.email, "zach49@example.com")
        self.assertEqual(website, "example.com")
        self.assertEqual(location, "Seattle")
        self.assertEqual(fee, 0.0)
        self.assertEqual(phone, None)
        self.assertEqual(camera, 'NK')
        self.assertEqual(services, 'P')
        self.assertEqual(photo_styles, 'O')
