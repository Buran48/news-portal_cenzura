from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(post_type='NW').order_by('-created_at')


class ArticlesList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(post_type='AR').order_by('-created_at')


class NewsDetail(DetailView):
    model = Post
    template_name = 'one_news.html'
    context_object_name = 'one_news'


class ArticleDetail(DetailView):
    model = Post
    template_name = 'one_article.html'
    context_object_name = 'one_article'