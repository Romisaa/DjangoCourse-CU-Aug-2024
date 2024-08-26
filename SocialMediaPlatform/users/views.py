from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserReistration
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserReistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} Your Account has been created')
            return redirect('UserLogin')

    else:
        form = UserReistration()

    return render(request, 'users/user_registertion.html', {'form': form})


def profile(request):
    return render(request, 'users/user_profile.html')









# class CustomLogoutView(LogoutView):
#     def get_next_page(self):
#         return redirect('MySocialHome')

def Userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'users/user_login.html')
        else:
            return render(request, 'users/user_registertion.html')
    else:
        return render(request, 'users/user_login.html')


# def Userlogout(request):
#     logout(request)
#     return render(request, 'users/user_logout.html')
