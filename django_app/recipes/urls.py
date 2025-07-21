from django.urls import path, include
from .views import home,recipes_list, recipe_detail, recipe_create, recipe_update, my_recipes, recipe_delete

urlpatterns = [
    path('', home, name='home'),
    path('recipes/', recipes_list, name="recipes_list"),
    path('recipes/<int:id>/', recipe_detail, name="recipe_detail"),
    path('recipes/create/', recipe_create, name="recipe_create"),
    path('recipes/update/<int:id>/', recipe_update, name="recipe_update"),
    path('recipes/<int:id>/delete/', recipe_delete, name='recipe_delete'),
    path('my-recipes/', my_recipes, name='my_recipes'),
]