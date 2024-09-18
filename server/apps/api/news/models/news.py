from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    """
    Новости
    """

    def upload_path(self, file):
        return f"news/{self.name}/{self.image.name}"

    title = models.CharField(
        max_length=127,
        verbose_name=_("Заголовок"),
    )

    publish_date = models.DateField(
        verbose_name=_("Дата публикации"),
        auto_now_add=True
    )

    update_date = models.DateField(
        verbose_name=("Дата изменения"),
        auto_now=True
    )

    text = models.TextField(
        verbose_name=_("Контент"),
    )

    image = models.ImageField(
        upload_to=upload_path,
        verbose_name=_("Изображение для новости"),
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Новость")
        verbose_name_plural = _("Новости")