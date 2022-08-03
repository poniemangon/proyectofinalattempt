from socket import fromshare
from django.contrib.auth.forms import  UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir password', widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2', 'first_name','last_name']


class CambiarUserForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username','email', 'first_name','last_name']
       


