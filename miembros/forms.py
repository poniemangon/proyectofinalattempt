from socket import fromshare
from django.contrib.auth.forms import  UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'imagen')
        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control'})
        }

class PasswordChange(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2', 'first_name','last_name']
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'


class CambiarUserForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ['username','email', 'first_name','last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),

        }


