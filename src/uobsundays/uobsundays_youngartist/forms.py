from django import forms
from uobsundays_youngartist.constants import CREATED_CHOICES, LOCATION_CHOICES


class YoungArtistFilterForm(forms.Form):
    created = forms.ChoiceField(choices=CREATED_CHOICES)
    location = forms.ChoiceField(choices=LOCATION_CHOICES)
