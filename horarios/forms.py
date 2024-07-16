from django.forms import forms
from .models import Rote

class RoteForms(forms.Form):

    class Meta:
        model = Rote
        fields = ['name', 'box', 'weekly_time', 'sartuday_time', 'alternative_time', 'rote']