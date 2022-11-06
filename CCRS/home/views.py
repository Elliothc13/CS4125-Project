from django.shortcuts import render
from tokens import sub

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        tokenBalance = sub.GenerateToken.get_current_tokens(request.user.id)
        print(tokenBalance)
        return render(request, 'home/home.html', {'tokenBalance': tokenBalance})
    return render(request, 'home/home.html')