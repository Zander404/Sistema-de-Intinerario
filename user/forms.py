from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label='Usuário')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Senha')
