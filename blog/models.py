from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.CharField(max_length=255, default=None)
    body = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to='media/profile', null=True, blank = True)

    def __str__(self):
        return self.title + ' from ' + str(self.author)
    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="media/profile")

    def __str__(self):
        
        return str(self.user)
