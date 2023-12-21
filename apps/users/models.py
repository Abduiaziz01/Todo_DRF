from django.db import models
from django.core.validators import RegexValidator

from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Имя"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Почта"
    )
    phone_regex = RegexValidator(
        regex=r'^\+996\d{9}$', 
        message="Номер телефона должен быть в формате +996XXXXXXXXX."
    )
    phone_number = models.CharField(
        max_length=50,
        unique=True, validators=[phone_regex],
        verbose_name="Номер телефона"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    age = models.PositiveIntegerField(
        verbose_name="Возраст",
        blank=True, null=True
    )

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"