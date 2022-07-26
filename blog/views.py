from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.forms import  NewPostForm
from blog.models import Post
from django.urls import reverse_lazy
from miembros.models import Profile, User
from miembros.forms import NewProfileForm
from .forms import EditPostForm, EditProfileForm
from django.core.paginator import Paginator


# Create your views here.




def page_not_found_view(request, exception):
   

    return render(request, 'blog/404.html')



class CreateProfileView(CreateView):
    model = Profile
    form_class = NewProfileForm
    template_name = 'blog/create-profile.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfileView(UpdateView):
    model = Profile
    template_name = 'blog/profile-edit.html'
    
    form_class = EditProfileForm
    success_url = reverse_lazy('home')

class ProfileView(DetailView):
    model = Profile
    template_name = 'blog/profile-details.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['users'] = users
        return context

def about(request):
    return render(request, "blog/about.html", {})

class HomeView(ListView):
    paginate_by = 4
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-post_date','-post_time']

    

class MyPosts(ListView):
    model = Post
    paginate_by = 3
    template_name = 'blog/mis-posts.html'
    ordering = ['-post_date','-post_time']
       


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details.html'
     
class NewArticleView(CreateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/new_post.html'
    success_url = reverse_lazy('home')

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        request.POST['author'] = request.user.id
        return super(NewArticleView, self).post(request, **kwargs)


class EditArticle(UpdateView):
    model = Post
    template_name = 'blog/edit_post.html'
    form_class = EditPostForm
    success_url = reverse_lazy('home')

class DeleteArticle(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')



def search_posts(request):
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(title__contains=searched)

        return render(request, 'blog/search.html',{'searched':searched, 'posts':posts})
    else:
        return render(request, 'blog/search.html', {})


