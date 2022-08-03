from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Avatar(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    imagen = models.ImageField(upload_to='media/profile', null=True, blank = True)

    def __str__(self):
        return str(self.user)
    def get_aboslute_url(self):
        return reverse('home')
