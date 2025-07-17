from django.urls import path, include
from .views import recipes_list, recipe_detail, recipe_create, recipe_update

urlpatterns = [
    path('', recipes_list, name="recipes_list"),
    path('<int:id>/', recipe_detail, name="recipe_detail"),
    path('create/', recipe_create, name="recipe_create"),
    path('update/<int:id>/', recipe_update, name="recipe_update")
]