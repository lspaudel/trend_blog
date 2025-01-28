# accounts/urls.py
from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.accounts_home, name='accounts_home'),  # Redirect to home page
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  
    path('logout/', views.accounts_home, name='logout'),
]