from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class LocalUser(AbstractUser):
    """
    Модель для сохранения в бд пользователя
    """
    is_actevated = models.BooleanField(default=True)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=28)

    groups = models.ManyToManyField(
        Group,
        related_name = 'local_user_set',
        blank = True,
        verbose_name = 'groups',
        help_text = (
            'The groups this user belongs to, A user will get all permissions'
            'granted to each of their groups.'
        ),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name = 'local_user_set',
        blank = True,
        verbose_name = 'user permissions',
        help_text = 'Specific permissions for this user.',
    )