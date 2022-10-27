from django.shortcuts import render
from django.http import HttpResponse

# Equivalent of controller in MVC

def index(request):
    return HttpResponse("Index for recommender")