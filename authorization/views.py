from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from core.forms import SignUpForm


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            # Get the authentication form from django
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('competition_home')
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            form = AuthenticationForm()

        return render(request, 'authorization/login.html', {
            'form': form
        })
    return redirect('competition_home')


def logout_view(request):
    logout(request)
    return redirect('login')


def profile_view(request):
    return render(request, 'authorization/profile.html')


def create_profile(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            login(request, user)

            return redirect("competition_home")
    else:
        form = SignUpForm()

    return render(request, 'authorization/create_profile.html', {
        'form': form
    })
