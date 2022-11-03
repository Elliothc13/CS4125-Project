from django.shortcuts import render
# from tokens

# Create your views here.
def home(request):
    return render(request, 'home/home.html')