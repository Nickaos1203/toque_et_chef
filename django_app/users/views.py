from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import CustomUser
from .serializers import CustomUserSerializer

# Create your views here.
class CustomUserViewSet(ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    
