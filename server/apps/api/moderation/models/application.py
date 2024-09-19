from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.api.auth.models import User


class Application(models.Model):
    """
    Заявка
    """
    def upload_path(self, file):
        return f"events/{self.name}/{self.image.name}"

    name = models.CharField(
        max_length=127,
        verbose_name=_("Название мероприятия")
    )

    description = models.TextField(
        verbose_name=_("Описание")
    )

    image = models.ImageField(
        upload_to=upload_path,
        verbose_name=_("Картинка мероприятия"),
        blank=True
    )

    date = models.DateTimeField(
        verbose_name=_("Дата мероприятия")
    )

    author = models.ForeignKey(
        User,
        verbose_name=_("Автор"),
        on_delete=models.CASCADE,
    )

    address = models.CharField(
        max_length=64,
        verbose_name=_("Адрес мероприятия")
    )

    landmark = models.CharField(
        max_length=100,
        verbose_name=_("Ориентир"),
        blank=True
    )

    def __str__(self):
        return f"{self.name}, {self.author}"



    class Meta:
        verbose_name = _("Заявка на мероприятие")
        verbose_name_plural = _("Заявки на мероприятие")