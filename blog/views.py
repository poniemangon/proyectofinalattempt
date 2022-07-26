from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post
from django.urls import reverse_lazy
from blog.forms import BusquedaFormulario


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

# def search_posts(request):
#     if request.method == "POST":
#         searched = request.POST['searched']
         

#         return render(request, 'blog/search.html', {'searched':searched})
#     else:
#         return render(request, 'blog/search.html', {})

def search_posts(request):
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(title__contains=searched)

        return render(request, 'blog/search.html',{'searched':searched, 'posts':posts})
    else:
        return render(request, 'blog/search.html', {})
