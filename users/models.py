from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.hashers import make_password

NULLABLE = {'blank': True, 'null': True}


class CustomUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = User(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    objects = CustomUserManager()
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    chat_id = models.CharField(max_length=50, verbose_name='Ссылка на Телеграмм')
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=50, verbose_name='Номер телефона', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
