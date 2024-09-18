from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.api.auth.models import User


class Post(models.Model):
    class ContentType(models.TextChoices):
        ARTICLE = "AR", "Статьи"
        INTERVIEW = "IN", "Интервью"
        RESEARCH = "RE", "Исследования"
        REPORT = "RP", "Отчеты"
        UPDATE = "UP", "Обновления платформы"

    def upload_path(self, file):
        return f"posts/{self.title}/{self.image.name}"

    title = models.CharField(
        verbose_name=_("Заголовок"),
        max_length=255,
    )

    text = models.TextField(
        verbose_name=_("Контент")
    )

    content_type = models.CharField(
        max_length=2,
        choices=ContentType.choices,
        default=ContentType.ARTICLE,
        verbose_name=("Тип контента")
    )

    image = models.ImageField(
        upload_to=upload_path,
        verbose_name=_("Изображение для поста"),
        blank=True
    )

    publish_date = models.DateField(
        auto_now_add=True,
        verbose_name=_("Дата публикации")
    )

    update_date = models.DateField(
        auto_now=True,
        verbose_name=_("Дата изменения")
    )

    author = models.ForeignKey(
        User,
        verbose_name=_("Автор поста"),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"