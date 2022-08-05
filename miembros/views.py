from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import  PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from miembros.forms import SignUpForm, CambiarUserForm, PasswordChange
from miembros.models import Profile


# Create your views here.





class NuevaPassView(PasswordChangeView):
    form_class = PasswordChange
    success_url = reverse_lazy('home')



class RegistroView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')



class EdicionUserView(generic.UpdateView):
    form_class = CambiarUserForm
    template_name = 'registration/editar-user.html'
    success_url = reverse_lazy('home')

  

    def get_object(self):
        return self.request.user

