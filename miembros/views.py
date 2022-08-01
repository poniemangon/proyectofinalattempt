from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import  PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from miembros.forms import SignUpForm, CambiarUserForm


# Create your views here.





class NuevaPassView(PasswordChangeView):
    form_class = PasswordChangeForm
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

# class UserUpdate(LoginRequiredMixin, UpdateView):
#     model = Usertemplate_name = 'registration/editar-user.html'
#     fields = ['username', 'email', 'first_name', 'last_name']

#     def get_success_url(self):
#         return reverse_lazy('user-detail', kwargs={'pk': self.request.user.id})