from django.urls import path
from .views import DeleteArticle, HomeView, ArticleDetailView, NewArticleView, EditArticle

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('new_post', NewArticleView.as_view(), name='new_post'),
    path('article/edit/<int:pk>', EditArticle.as_view(), name='edit_post'),
    path('article/<int:pk>/delete', DeleteArticle.as_view(), name='delete_post')
]
