from django.shortcuts import render

from .models import CustomUser
from recipes.models import Recipe
from .forms import LoginForm, RegisterForm


def login_page(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'users/login.html', context={'form': form})


def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('recipes')
        else:
            form = RegisterForm()
        return render(request, 'users/register.html', {'form':form})