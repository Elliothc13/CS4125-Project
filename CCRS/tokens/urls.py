from django.urls import path
from . import views

urlpatterns = [
    path('generate', views.confirmed_events, name='list-confirmed-events')
]