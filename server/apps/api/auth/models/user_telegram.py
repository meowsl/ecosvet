from django.db import models
from .user import User
from django.utils.translation import gettext_lazy as _

class UserTelegram(models.Model):
    """
    Данные телеграм пользователя
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Пользователь")
    )

    telegram_id = models.CharField(
        max_length=64,
        verbose_name=_("ID телеграм аккаунта")
    )

    class Meta:
        verbose_name = _("Телеграм пользователя")
        verbose_name_plural= _("Телеграмм пользователей")