# authentication/forms.py
from django import forms
from .models import CustomUser

class LoginForm(forms.Form):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_nameq<"" = forms.CharField(max_length=30, required=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class ProfileUpdtaeForm():
    pass