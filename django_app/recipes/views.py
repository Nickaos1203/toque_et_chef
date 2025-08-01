from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

import random
import json
from django.http import JsonResponse

from django.urls import reverse_lazy
from django.contrib import messages

from .models import Recipe
from .forms import RecipeForm
from .rag_system import rag_system


def home(request):
    recipes = Recipe.objects.order_by("?")[:6]
    return render(request, "recipes/home.html", {'recipes':recipes})


def recipes_list(request):
    recipes = Recipe.objects.all()
    pagination = Paginator(recipes, 12)     # Pagination de 10 recettes par page

    page_number = request.GET.get('page')
    page_obj = pagination.get_page(page_number)
    return render(request=request,template_name="recipes/recipes_list.html", context={'page_obj':page_obj, 'recipes': page_obj.object_list})


def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    comments = recipe.comments.all()
    return render(request=request, template_name="recipes/recipes_detail.html", context={'recipe':recipe, 'comments':comments})


@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user

            # Récupération des ingrédients dynamiques
            ingredients = []
            steps = []

            for key, value in request.POST.items():
                if key.startswith('ingredient_') and value.strip():
                    ingredients.append(value.strip())
                if key.startswith('step_') and value.strip():
                    steps.append(value.strip())

            recipe.ingredients = ";".join(ingredients)
            recipe.steps = ";".join(steps)

            recipe.save()
            messages.success(request, "La recette est créée avec succès !")
            return redirect('recipes_list')  # Assure-toi que cette route existe
    else:
        form = RecipeForm()

    return render(request, 'recipes/recipe_create.html', {'form': form})


@login_required
def recipe_update(request, id):
    recipe = get_object_or_404(Recipe, id=id, author=request.user)
    ingredients = recipe.ingredients
    steps = recipe.steps

    if request.method == 'POST':
        form = RecipeForm(request.POST or None, instance=recipe)
        form.save()
        return redirect('recipe_detail', id=id)
    else:
        form = RecipeForm(instance=recipe)

    ingredients = recipe.ingredients.split(';') if recipe.ingredients else []
    ingredients = [i.strip() for i in ingredients]

    steps = recipe.steps.split(";") if recipe.steps else []
    steps = [s.strip() for s in steps]
    
    return render(request, 'recipes/recipe_update.html', {'form':form, 'recipe':recipe, 'ingredients':ingredients, 'steps':steps})


@login_required
def recipe_delete(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.user != recipe.author:
        return render(request, '403.html', status=403)  # Ou redirige vers une page d'erreur

    if request.method == 'POST':
        recipe.delete()
        messages.success(request, 'Recette supprimée avec succès!')
        return redirect('my_recipes')
    return render(request, 'recipes/recipe_delete.html', {'recipe':recipe})


@login_required
def my_recipes(request):
    recipes = Recipe.objects.filter(author=request.user)
    return render(request, 'recipes/my_recipes.html', {'recipes': recipes})


@csrf_exempt
def chatbot_api(request):
    """API pour le chatbot RAG"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            question = data.get('message', '').strip()
            
            if not question:
                return JsonResponse({
                    'response': 'Veuillez poser une question sur les recettes.'
                })
            
            # Obtenir la réponse du système RAG
            response = rag_system.get_recipe_recommendations(question)
            
            return JsonResponse({
                'response': response
            })
            
        except json.JSONDecodeError:
            return JsonResponse({
                'response': 'Erreur dans le format de la requête.'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'response': f'Désolé, une erreur s\'est produite: {str(e)}'
            }, status=500)
    
    return JsonResponse({
        'response': 'Méthode non autorisée.'
    }, status=405)