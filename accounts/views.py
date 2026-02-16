# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import login
import logging

logger = logging.getLogger(__name__)


def accounts_home(request):
    return render(request, 'accounts/home.html')


def signup(request):
    """Handle user registration"""
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                messages.success(request, f'Welcome {user.username}! Your account has been created.')
                logger.info(f'New user registered: {user.username} ({user.email})')
                return redirect('blog:profile')  # Redirect to profile after signup
            except Exception as e:
                logger.error(f'Error during signup: {str(e)}')
                messages.error(request, 'An error occurred during signup. Please try again.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form})
