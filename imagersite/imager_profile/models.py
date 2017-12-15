"""Imager profile models."""
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver


class ImageActiveProfile(models.Manager):
    """."""

    def get_queryset(self):
        """."""
        return super(ImageActiveProfile, self).get_queryset().filter(user__is_active=True)


class ImagerProfile(models.Model):
    """The imager profile model."""

    objects = models.Manager
    active = ImageActiveProfile()

    CAMERAS = (
        ('Nikon', 'NK'),
        ('Cannon', 'CN')
    )

    STYLES = (
        ('Old', 'O'),
        ('New', 'N'),
        ('Modern', 'M')
    )

    SERVICES = (
        ('Portraits', 'P'),
        ('Weddings', 'W')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    website = models.URLField(blank=True, null=True)
    fee = models.DecimalField(max_digits=5, decimal_places=2,
                              blank=True, null=True)
    location = models.CharField(max_length=180, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    camera = models.CharField(max_length=50, choices=CAMERAS,
                              blank=True, null=True)
    services = models.CharField(max_length=50, choices=SERVICES,
                                blank=True, null=True)
    photo_styles = models.CharField(max_length=50, choices=STYLES,
                                    blank=True, null=True)

    active = ImageActiveProfile()

    def __str__(self):
        """Print function returns this."""
        return self.user.username

    @property
    def is_active(self):
        """Is_active method for user profile."""
        return self.user.is_active


@receiver(models.signals.post_save, sender=User)
def create_profile(sender, **kwargs):
    """Create the profile when a user is created."""
    if kwargs['created']:
        profile = ImagerProfile(user=kwargs['instance'])
        profile.save()
