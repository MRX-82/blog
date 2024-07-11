from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from .models import LocalUser

class UserForm(UserCreationForm):
    #password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    #password2 = forms.CharField(label='Пароль еще раз', widget=forms.PasswordInput)

    class Meta:
        model = LocalUser
        fields=('username', 'email', 'password1', 'password2')