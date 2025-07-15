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


    title = models.CharField(max_length=50)
    image_url = models.URLField(max_length=250, null=True, blank=True)
    season = models.CharField(choices=Season.choices, max_length=20)
    category = models.CharField(choices=Category.choices, max_length=20)
    tags = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=10)
    level = models.CharField(max_length=20)
    cost = models.CharField(max_length=20)
    number = models.IntegerField()
    persons_number = models.CharField(max_length=20)
    ingredients = models.TextField()
    steps = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='recipes')

    def __str__(self):
        return self.title

