from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.URLField(max_length=250)
    image = 