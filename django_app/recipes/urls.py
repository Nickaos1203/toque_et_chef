from django.urls import path, include
from .views import home,recipes_list, recipe_detail, recipe_create, recipe_update, my_recipes, recipe_delete

urlpatterns = [
    path('', recipes_list, name="recipes_list"),
    path('<int:id>/', recipe_detail, name="recipe_detail"),
    path('create/', recipe_create, name="recipe_create"),
    path('update/<int:id>/', recipe_update, name="recipe_update"),
    path('delete/<int:id>/', recipe_delete, name='recipe_delete'),
    path('my-recipes/', my_recipes, name='my_recipes'),
]