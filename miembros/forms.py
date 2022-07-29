from socket import fromshare
from django.contrib.auth.forms import  UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


# class SignUpForm(UserChangeForm):
#     username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(widget=forms.EmailInput)
#     nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     apellido = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
#     class Meta:
#         model = User
#         fields = ('username','first_name','last_name')