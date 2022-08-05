from socket import fromshare
from django.contrib.auth.forms import  UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django import forms
from .models import Post
from miembros.models import Profile


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','resume','author','imagen','body' )
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'resume': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

class EditProfileForm(forms.ModelForm):


    class Meta:
        model = Profile
        fields = ['bio','imagen']
        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control'})
            

        }


