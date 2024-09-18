from django.db import models
from django.utils.translation import gettext_lazy as _


class Application(models.Model):
    """
    Заявка
    """
    username = models.CharField(_("Имя пользователя"), max_length=100)

    first_name = models.CharField(_("Имя"), max_length=30)

    last_name = models.CharField(_("Фамилия"), max_length=150)

    surname = models.CharField(
        _("Отчество"),
        max_length=150,
        blank=True,
        null=True
    )

    email = models.EmailField(verbose_name=_("e-mail"))

    password = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name=_("Новый пароль участника")
    )

    def __str__(self):
        if self.surname:
            return f"{self.last_name} {self.first_name[0]}. {self.surname[0]}."
        else:
            return f"{self.last_name} {self.first_name[0]}."

    class Meta:
        verbose_name = _("Заявка на участие")
        verbose_name_plural = _("Заявки на участие")