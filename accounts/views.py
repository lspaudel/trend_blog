# accounts/views.py
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login


def accounts_home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after signing up
            return redirect('accounts:login')  # Redirect to the login page after signup
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
