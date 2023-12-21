from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user_todo',
        verbose_name="Пользователь"
    )
    title = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    is_completed = models.BooleanField(
        default = False,
        verbose_name="Статус описание"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    image = models.ImageField(
        upload_to="todo_image/",
        blank=True, null=True,
        verbose_name="Фотография"
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name="Опирация"
        verbose_name_plural="Опирации"