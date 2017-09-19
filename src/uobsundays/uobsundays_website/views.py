from django.views.generic import ListView
from uobsundays_website.models import SignupContent, Branches, HomepageImage


class IndexView(ListView):
    context_object_name = 'images'
    model = HomepageImage
    template_name = 'uob_sundays_website/index.html'


class LocateUsView(ListView):
    context_object_name = 'branches'
    model = Branches
    template_name = 'uob_sundays_website/locate_us.html'


class SignUpView(ListView):
    template_name = 'uob_sundays_website/sign_up.html'
    model = SignupContent
    context_object_name = 'contents'
