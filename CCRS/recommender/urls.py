from django.urls import path
from . import views

urlpatterns = [
    path('recommender', views.confirmed_events, name='list-recommendations')
]