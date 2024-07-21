from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from .models import LocalUser

class UserForm(UserCreationForm):
    """
    Форма для регистрации нового пользователя
    """
    class Meta:
        model = LocalUser
        fields=('username', 'email', 'password1', 'password2')