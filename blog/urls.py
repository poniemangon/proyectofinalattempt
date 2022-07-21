from django.urls import path
from .views import HomeView, ArticleDetailView, NewArticleView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('new_post', NewArticleView.as_view(), name='new_post')
]
