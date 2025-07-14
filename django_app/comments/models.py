from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from recipes.models import Recipe

# Create your models here.
class Comment(models.Model):
    grade = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    title = models.CharField(max_length=20)
    contain = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe.title + " : " + self.title
