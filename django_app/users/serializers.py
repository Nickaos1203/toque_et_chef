from rest_framework import serializers
from .models import CustomUser

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from comments.serializers import CommentSerializer


class CustomUserSerializer(serializers.ModelSerializer):

    recipes = RecipeSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = '__all__'