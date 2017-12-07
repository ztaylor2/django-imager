"""Photo model managment."""
from django.db import models
from imager_profile.models import ImagerProfile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Photo(models.Model):
    """The photo model."""

    PUBLISHED = (
        ('private', 'Private'),
        ('shared', 'Shared'),
        ('public', 'Public')
    )

    user = models.ForeignKey(ImagerProfile,
                             on_delete=models.CASCADE,
                             related_name='photo')
    image = models.ImageField(upload_to='documents/%Y/%m/%d')

    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    date_uploaded = models.DateField(auto_now=False, auto_now_add=True)
    date_modified = models.DateField(auto_now=True, auto_now_add=False)
    date_published = models.DateField(auto_now=False, auto_now_add=False)
    published = models.CharField(max_length=50, choices=PUBLISHED,
                                 blank=True, null=True)


class Album(models.Model):
    """The album model."""

    PUBLISHED = (
        ('private', 'Private'),
        ('shared', 'Shared'),
        ('public', 'Public')
    )

    user = models.ForeignKey(ImagerProfile,
                             on_delete=models.CASCADE,
                             related_name='album')
    photo = models.ManyToManyField(Photo, blank=True, default='',
                                   related_name='album')
    cover = models.ImageField(upload_to='documents/%Y/%m/%d',
                              blank=True,
                              null=True)
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    date_uploaded = models.DateField(auto_now=False, auto_now_add=True)
    date_modified = models.DateField(auto_now=True, auto_now_add=False)
    date_published = models.DateField(auto_now=False, auto_now_add=False)
    published = models.CharField(max_length=50, choices=PUBLISHED,
                                 blank=True, null=True)


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    """Create the profile when a user is created."""
    if kwargs['created']:
        profile = ImagerProfile(user=kwargs['instance'])
        profile.save()
