from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
# posts = [
#     {'auther': 'Romisaa',
#      'content': 'This is my first post'
#      },
#
#     {'auther': 'Ahmed',
#      'content': 'Hello'
#      },
#
#     {'auther': 'Mona',
#      'content': 'Good Morning'
#      }
# ]


def home(request):
    context ={'posts': Post.objects.all()}
    return render(request, 'SocialMediaPlatform/home.html', context)


def about(request):
    return render(request, 'SocialMediaPlatform/about.html', {'content': 'View'})
