from django.urls import path

from .views import index, RegistrationUser

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration_user/', RegistrationUser.as_view(), name='RegistrationUser'),
    path('', index, name='index'),
]