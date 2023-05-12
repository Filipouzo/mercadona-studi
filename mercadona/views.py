from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def index(request):
    return render(request, "mercadona/home.html")


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(
                'offers_list')  # Remplacez 'home' par le nom de l'URL vers laquelle vous voulez rediriger l'utilisateur
    else:
        form = LoginForm()
    return render(request, 'mercadona/login.html', {'form': form})
