from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from tokens.models import Volunteer, Organisation


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user and user.is_authenticated:
            login(request, user)
            return redirect('list-recommendations')
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

def register_user(request):
    # print(request.POST.get('password'))
    if request.method == 'POST':
        registrationForm = UserCreationForm(request.POST)
        if registrationForm.is_valid():
            registrationForm.save()
            username = registrationForm.cleaned_data['username']
            password = registrationForm.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                volunteer = Volunteer(firstName=request.POST.get('firstName'),
                                        lastName=request.POST.get('lastName'),
                                        userId = user.id,
                                        userEmail=request.POST.get('email'),
                                        tokenBalance=1)
                volunteer.save()
                messages.success(request, ("You were logged in: registration successful"))
                return redirect('home')
        else:
            messages.error(request, ("Registration failed, please try again"))
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
        
def register_org(request):
    # print(request.POST.get('password'))
    if request.method == 'POST':
        registrationForm = UserCreationForm(request.POST)
        if registrationForm.is_valid():
            registrationForm.save()
            username = registrationForm.cleaned_data['username']
            password = registrationForm.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                org = Organisation(name=request.POST.get('organisationName'),
                                        userId = user.id,
                                        userEmail=request.POST.get('email'))
                org.save()
                messages.success(request, ("You were logged in: registration successful"))
                return redirect('home')
        else:
            messages.error(request, ("Registration failed, please try again"))
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register_org.html', {'form': form})