"""Views."""
from django.template import loader
from django.shortcuts import render


def home_view(request):
    """Home page view."""
    return render(request, 'imagersite/home.html')


# def login_view(request):
#     """Login page view."""
#     return render(request, 'imagersite/login.html')


def logout_view(request):
    """Logout page view."""
    return render(request, 'imagersite/logout.html')
