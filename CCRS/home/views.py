from django.shortcuts import render
from tokens import sub
from login import user_utils

# Create your views here.


def home(request):
    if (request.user.is_authenticated and user_utils.isVolunteer(request.user.id)):
        tokenBalance = sub.GenerateToken.get_current_tokens(request.user.id)
        print(tokenBalance)
        return render(request, 'home/home.html', {'tokenBalance': tokenBalance})
    return render(request, 'home/home.html')
