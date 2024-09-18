from django.db import models
from django.utils.translation import gettext_lazy as _

class Achievement(models.Model):

    def upload_path(self, file):
        return f"achievements/{self.name}/{self.image.name}"

    name = models.CharField(
        verbose_name=_("Название"),
        max_length=100,
    )

    description = models.TextField(
        verbose_name=_("Описание достижения")
    )

    icon = models.ImageField(
        upload_to=upload_path,
        verbose_name=_("Иконка достижения")
    )