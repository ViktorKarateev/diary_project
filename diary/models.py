from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    """Тег, прикрепляемый к записям дневника."""

    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Название тега",
    )

    def __str__(self):
        return self.name


class Mood(models.Model):
    """Настроение пользователя во время создания записи."""

    name = models.CharField(
        max_length=50,
        verbose_name="Настроение",
    )
    emoji = models.CharField(
        max_length=5,
        verbose_name="Эмодзи",
    )

    def __str__(self):
        return f"{self.emoji} {self.name}"


class Entry(models.Model):
    """Запись в личном дневнике пользователя."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="entries",
        verbose_name="Автор",
    )
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
    )
    text = models.TextField(
        verbose_name="Содержимое",
    )
    mood = models.ForeignKey(
        Mood,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Настроение",
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name="Теги",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Создано",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Обновлено",
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return f"{self.title} ({self.created_at.date()})"
