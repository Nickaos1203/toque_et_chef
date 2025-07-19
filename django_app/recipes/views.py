from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

from .models import Recipe
from .forms import RecipeForm


def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request=request,template_name="recipes/recipes_list.html", context={'recipes':recipes})


def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    comments = recipe.comments.all()
    return render(request=request, template_name="recipes/recipes_detail.html", context={'recipe':recipe, 'comments':comments})


@login_required
def recipe_create(request):
    form = RecipeForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('recipes')
    return render(request, 
        'recipes/recipes_create.html',
        {'form':form})


@login_required
def recipe_update(request, id):
    recipe = get_object_or_404(Recipe, id=id, author=request.user)
    form = RecipeForm(request.POST or None, instance=recipe)
    if request.method == 'POST':
        form.save()
        return redirect('recipe_detail', id=id)
    return render(request, 'recipes/recipes_create.html', {'form':form})


@login_required
def recipe_delete(request, id):
    recipe = get_object_or_404(Recipe, id=id, author=request.user)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes')
    return render(request, 'recipes/recipe_delete.html', {'recipe':recipe})