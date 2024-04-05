from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = DearUser
        fields = ['username', 'email', 'password1', 'password2']