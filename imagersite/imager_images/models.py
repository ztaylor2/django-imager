"""Photo model managment."""
from django.db import models
from imager_profile.models import ImagerProfile


class Photo(models.Model):
    """The photo model."""

    PUBLISHED = (
        ('private', 'PR'),
        ('shared', 'SH'),
        ('public', 'PU')
    )

    user = models.ForeignKey(ImagerProfile, related_name='photo')
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
        ('private', 'PR'),
        ('shared', 'SH'),
        ('public', 'PU')
    )

    user = models.ForeignKey(ImagerProfile, related_name='album')
    photo = models.ManyToManyField(Photo)

    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    date_uploaded = models.DateField(auto_now=False, auto_now_add=True)
    date_modified = models.DateField(auto_now=True, auto_now_add=False)
    date_published = models.DateField(auto_now=False, auto_now_add=False)
    published = models.CharField(max_length=50, choices=PUBLISHED,
                                 blank=True, null=True)
