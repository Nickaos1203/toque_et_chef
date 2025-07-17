from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from recipes.models import Recipe
from users.models import CustomUser

# Create your models here.
class Comment(models.Model):
    grade = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    title = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    contain = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')


    def __str__(self):
        return self.recipe.name + " : " + self.title + " : " + self.date
