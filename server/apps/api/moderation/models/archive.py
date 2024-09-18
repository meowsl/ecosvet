from django.db import models
from django.utils.translation import gettext_lazy as _

from .application import Application


class Archive(models.Model):

    class ApplicationStatus(models.IntegerChoices):
        APPROVED = 1, _("Одобрено")
        REJECTED = 2, _("Отклонено")

    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        verbose_name="Заявка"
    )

    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Дата")
    )

    status = models.PositiveIntegerField(
        choices=ApplicationStatus.choices,
        editable=False,
        verbose_name=_("Статус заявки")
    )

    def __str__(self):
        return f"{self.application.last_name} {self.application.first_name} ({self.date})"


    class Meta:
        ordering = ["-id"]
        verbose_name = "Архив"
        verbose_name_plural = "Архив"
