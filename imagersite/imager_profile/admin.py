"""Admin."""
from django.contrib import admin
from imager_profile.models import ImagerProfile, ImageActiveProfile

admin.site.register(ImagerProfile, ImageActiveProfile)
