from django.urls import path
from . import views
from .views import PostList, PostDetails, PostCreate

app_name = 'users'
urlpatterns = [
    path('', PostList.as_view(template_name='/socual_media_home/post_list.html'), name='MySocialHome'),
    path('posts/<int:pk>', PostDetails.as_view(template_name="socual_media_home/post_details.html"),
         name="MyPostDetails"),
    path('posts/new',PostCreate.as_view(template_name='socual_media_home/post_form.html'), name="NewPost" ),
    path('about/', views.about, name="MySocialAbout"),
]

# Template_name
# app/model_viewType
# socual_media_home/post_list.html
