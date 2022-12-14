from django.urls import path
from . import views

urlpatterns = [
    path('signin', views.login_user, name='login'),
    path('signout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('registerorg', views.register_org, name='registerorg'),
]