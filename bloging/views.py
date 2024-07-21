from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy

from .models import LocalUser
from .forms import UserForm

from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()

def index(request):
    """
    Функция представление для главной страницы
    """
    prb = 'skusime to'
    context = {'PROBA': prb}
    return render(request, 'bloging/index.html', context)

@login_required
def damp_view(request):
    """
    пробник
    """
    print('Представление damp')
    return render(request, 'bloging/damp.html')


class RegistrationUser(CreateView):
    """
    Функция представление для регистрации нового пользователя
    """
    template_name = 'bloging/registration_user.html'
    form_class = UserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = form.cleaned_data['username']
        user.set_password(form.cleaned_data['password1'])
        user.save()
        return super().form_valid(form)


class UserLoginView(LoginView):
    """
    Класс для авторизации пользователя по логину и паролю
    """
    template_name = "bloging/login.html"
    success_url = reverse_lazy('damp')

    def get_success_url(self):
        """
        Пробничек
        """
        return self.success_url