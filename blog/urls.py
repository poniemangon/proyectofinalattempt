from django.urls import path
from .views import  MyPosts, index, CreateProfileView, EditProfileView , ProfileView, search_posts, DeleteArticle, HomeView, ArticleDetailView, NewArticleView, EditArticle

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('new_post', NewArticleView.as_view(), name='new_post'),
    path('article/edit/<int:pk>', EditArticle.as_view(), name='edit_post'),
    path('article/<int:pk>/delete', DeleteArticle.as_view(), name='delete_post'),
    path('search', search_posts, name='search'),
    path('profile/<int:pk>', ProfileView.as_view(), name="profile-details"),
    path('profile_edit/<int:pk>', EditProfileView.as_view(), name="profile-edit"),
    path('new-profile', CreateProfileView.as_view(), name='new-profile'),
    path('index/', index),
    path('myposts/', MyPosts.as_view(), name="myposts"),
    
    
    
    
    
]



