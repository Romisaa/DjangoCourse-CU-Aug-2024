from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# def home(request):
#     context = {'posts': Post.objects.all()}
#     return render(request, 'socual_media_home/post_list.html', context)


def about(request):
    return render(request, 'socual_media_home/about.html', {'content': 'View'})


class PostList(ListView):
    model = Post
    context_object_name = 'posts'


class PostDetails(DetailView):
    model = Post


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
