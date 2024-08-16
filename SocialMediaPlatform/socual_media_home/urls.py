from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='MySocialHome'),
    path('about/', views.about, name="MySocialAbout"),
]