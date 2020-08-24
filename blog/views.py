from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.base import RedirectView

from .models import Post

# Create your views here.


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'


class PostRedirectDetailView(RedirectView):
    permanent = True
    query_string = True
    #pattern_name = 'blog:detail'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        return post.get_absolute_url()
