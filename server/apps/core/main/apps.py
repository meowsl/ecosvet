from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MainConfig(AppConfig):
    """Default app config"""

    name = "apps.core.main"
    verbose_name = _("Главное")
