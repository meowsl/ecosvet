from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ModerationConfig(AppConfig):
    """Default app config"""

    name = "apps.api.moderation"
    verbose_name = _("Moderation")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
