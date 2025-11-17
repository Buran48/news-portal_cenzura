from django.urls import path
from .views import NewsList, NewsDetail, ArticlesList, ArticleDetail

urlpatterns = [
    path('news/', NewsList.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('articles/', ArticlesList.as_view(), name='articles_list'),
    path('articles/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
]