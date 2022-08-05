from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.CharField(max_length=255, default=None)
    imagen = models.ImageField(upload_to='media/postimages', null=True, blank = True)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True, )


    def __str__(self):
        return self.title + ' from ' + str(self.author)
    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))



