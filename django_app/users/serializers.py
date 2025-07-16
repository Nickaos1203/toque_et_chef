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
        fields = ['username', 'email', 'phone_number', 'first_name', 'last_name', 'birthday_date', 'is_active', 'is_superuser', 'password', 'recipes', 'comments']


# class CreateCustomUserSerializer(serializers.Serializer)