from django.contrib.auth.models import AbstractUser
from django.db import models

from django import forms


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    birthday_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.username
