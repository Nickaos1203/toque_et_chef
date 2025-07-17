from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    title = forms.CharField(max_length=1000)
    image_url = forms.URLField(max_length=250)
    season = forms.CharField(max_length=20)
    category = forms.CharField(max_length=20)
    duration = forms.CharField(max_length=10)
    level = forms.CharField(max_length=20)
    cost = forms.CharField(max_length=20)
    number = forms.IntegerField()
    persons_number = forms.CharField(max_length=20)
    ingredients = forms.CharField(max_length=1000)
    steps = forms.CharField(max_length=1000)