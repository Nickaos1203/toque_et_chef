from django.db import models
from users.models import CustomUser

# Create your models here.
class Recipe(models.Model):

    class Season(models.TextChoices):
        SEASON = 'De saison'
        NOT_SEASON = 'Pas de saison'


    class Category(models.TextChoices):
        APPETIZER = 'Entrée'
        DISH = 'Plat principal'
        DESSERT = 'Dessert'


    title = models.CharField(max_length=200)
    image_url = models.URLField(max_length=250, null=True, blank=True)
    season = models.CharField(choices=Season.choices, max_length=100)
    category = models.CharField(choices=Category.choices, max_length=100)
    tags = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)
    number = models.IntegerField(null=True, blank=True)
    persons_number = models.CharField(max_length=50)
    ingredients = models.TextField()
    steps = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='recipes')

    # conversion de texte en liste avec séparateur ";"
    def display_tags_list(self):
        return [item.strip() for item in self.tags.split(";") if item.strip()]

    def display_ingredients_list(self):
        return [item.strip() for item in self.ingredients.split(";") if item.strip()]

    def display_steps_list(self):
        return [item.strip() for item in self.steps.split(";") if item.strip()]
    
    def __str__(self):
        return f'{self.id} : {self.title}'