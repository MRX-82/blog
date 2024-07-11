from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy

from .models import LocalUser
from .forms import UserForm

from django.views.generic.edit import CreateView

def index(request):
    prb = 'skusime to'
    context = {'PROBA': prb}
    return render(request, 'bloging/index.html', context)

class RegistrationUser(CreateView):
    template_name = 'bloging/registration_user.html'
    form_class = UserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = form.cleaned_data['username']
        user.set_password(form.cleaned_data['password1'])
        user.save()
        return super().form_valid(form)



