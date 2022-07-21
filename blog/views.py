from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post
from django.urls import reverse_lazy

# Create your views here.



class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details.html'
     
class NewArticleView(CreateView):
    model = Post
    template_name = 'blog/new_post.html'
    fields = '__all__'

class EditArticle(UpdateView):
    model = Post
    template_name = 'blog/edit_post.html'
    fields = ['title', 'resumen', 'body']

class DeleteArticle(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')