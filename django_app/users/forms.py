# authentication/forms.py
from django import forms
from .models import CustomUser

class LoginForm(forms.Form):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class RegisterForm(forms.Form):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password']