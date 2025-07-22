from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import CustomUser
from recipes.models import Recipe
from .forms import LoginForm, RegisterForm, UserUpdateForm


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenue {user.username} !')
            return redirect('home')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'users/login.html')


@login_required
def logout_page(request):
    user_name = request.user.first_name or request.user.username
    logout(request)
    messages.success(request, f'Au revoir {user_name} ! Vous êtes maintenant déconnecté.')
    return redirect('home')


def register_page(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = False
            user.is_staff = False
            user.save()
            messages.success(request, "Votre compte a été créé avec succès !")
            return redirect('home')
        else:
            form = RegisterForm()
            messages.warning(request, 'Un ou plusieurs champs sont mal remplis.')
    return render(request, 'users/register.html', {'form':form})


def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)       
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Profil mis à jour avec succès!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
    return render(request, 'users/profile.html', {
        'user_form': user_form,
    })