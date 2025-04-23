from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from datetime import datetime

x = datetime.now()

# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged In!"))
            return redirect('product:home')
        else:
            messages.success(request, ("There was an error, please try again..."))
            return redirect('login')

    else:
        return render(request, 'login.html', {})

def signup_view(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Username Created - Please Fill Out Your User Info Below..."))
            return redirect('product:home')
        else:
            messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
            return render(request, 'signup.html', {'form': form})
    else:
        return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, ("You have been logged out...Thanks for stopping by..."))
    return render(request, 'signup.html')

