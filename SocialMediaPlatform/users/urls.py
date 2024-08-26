from django.urls import path
from . import views
# from .views import CustomLogoutView

urlpatterns = [
    path('', views.register, name='UserRegisteration'),
    path('profile/', views.profile, name="user_profile"),
    path('login/', views.Userlogin, name="UserLogin"),
    # path('logout/', CustomLogoutView.as_view(template_name='users/user_logout'), name='UserLogout')

]