from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.api.auth.models import User
from .event import Event

class UserEvent(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Пользователь"),
        related_name="user_event"
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        verbose_name=_("Мероприятие"),
        related_name="user_event"
    )

    def __str__(self):
        return f"{self.user} - {self.event}"

    class Meta:
        verbose_name = "Мероприятие пользователя"
        verbose_name_plural = "Мероприятия пользователей"
        unique_together = ("user", "event")