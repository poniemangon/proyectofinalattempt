from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post

# Create your views here.



class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details.html'
     
