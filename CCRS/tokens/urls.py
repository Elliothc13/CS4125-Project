from django.urls import path
from . import views

urlpatterns = [
    path('generate', views.confirmed_events, name='list-confirmed-events'),
    path('entryid/<int:pk>', views.approve_tokens, name='approve-tokens-for')
]