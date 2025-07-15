from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Recipe
from .serializers import RecipeSerializer


class RecipeViewSet(ModelViewSet):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeByAuthorViewSet(ModelViewSet):

    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.request.GET.get('author')
        if author_id:
            queryset = queryset.filter(author_id=author_id)
            return queryset