from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib import messages

# poor design, currently forced by djangos lack of support for same urls with different views (forced binding) and circular redirects

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user and user.is_authenticated:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, ("Login failed, please try again"))
            return redirect('login')
    else:
        return render(request, 'registration/login.html', {})

# Create your views here.
def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out successfully"))
    return redirect('home')