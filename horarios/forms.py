from django import forms
from .models import Rote

class RoteForms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput)
    box = forms.IntegerField(widget=forms.NumberInput)
    weekly_time = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Digite os horarios separados por vírgula'}
    ))
    sartuday_time = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Digite os horarios separados por vírgula'}
    ))
    alternative_time = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Digite os horarios separados por vírgula'}
    ))


    class Meta:
        model = Rote
        fields = ['name', 'box', 'weekly_time', 'sartuday_time', 'alternative_time', 'rote']


    def clean_time(self, field_name):
        data = self.cleaned_data[field_name]
        time_list = [time.strip() for time in data.split(',')]
        return time_list
    

    def clean_weekly_time(self):
        return self.clean_time('weekly_time')
    
    def clean_sartuday_time(self):
        return self.clean_time('sartuday_time')
    
    def clean_alternative_time(self):
        return self.clean_time('alternative_time') 

    
