from django.shortcuts import render, get_object_or_404
from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post
from django.urls import reverse_lazy
from miembros.models import Profile



# Create your views here.
class EditProfileView(UpdateView):
    model = Profile
    template_name = 'blog/profile-edit.html'
    fields = ['bio', 'imagen']
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
    success_url = reverse_lazy('home')

class EditArticle(UpdateView):
    model = Post
    template_name = 'blog/edit_post.html'
    fields = ['title', 'body','resume']
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


