# # for use customuser model
# from django.contrib.auth import get_user_model
# User = get_user_model()

from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = '__all__'