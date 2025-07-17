from django.shortcuts import render, redirect

from .models import Recipe
from .forms import RecipeForm


def recipes_list(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request=request,template_name="recipes/recipes_list.html", context=context)


def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    comments = recipe.comments.all()
    context = {
        'recipe': recipe,
        'comments': comments
        }
    return render(request,template_name='recipes/recipes_detail.html', context=context)


def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
    else:
        form = RecipeForm()
    return render(request, 
        'recipes/recipes_create.html',
        {'form':form})


def recipe_update(request, id):
    recipe = Recipe.objects.get(id=id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe.id)
    else:
        form = RecipeForm(instance=recipe)

    return render(request,
        'recipes/recipes_update.html',
        {'form':form})