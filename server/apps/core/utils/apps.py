from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UtilsConfig(AppConfig):
    """Default app config"""

    name = "apps.core.utils"
    verbose_name = _("Утилиты")
