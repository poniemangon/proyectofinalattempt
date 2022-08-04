from socket import fromshare
from django.contrib.auth.forms import  UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django import forms
from .models import Post
from miembros.models import Profile


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author','resume','body', )
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'resume': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

class EditProfileForm(forms.ModelForm):


    class Meta:
        model = Profile
        fields = ['bio','imagen']
        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control'})
            

        }


