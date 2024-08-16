from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
posts = [
    {'auther': 'Romisaa',
     'content' : 'This is my first post'
     },

    {'auther': 'Ahmed',
     'content': 'Hello'
     },

    {'auther': 'Mona',
     'content': 'Good Morning'
     }
]

def home(request):
    context = {'posts': posts}
    return render(request, 'SocialMediaPlatform/home.html', context)


def about(request):
    return HttpResponse("This is the About Page")
