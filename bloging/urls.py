from django.urls import path

from .views import index, RegistrationUser, UserLoginView, damp_view
from .import views


urlpatterns = [
    path('damp/', views.damp_view, name='damp'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration_user/', RegistrationUser.as_view(), name='RegistrationUser'),
    path('', index, name='index'),
]