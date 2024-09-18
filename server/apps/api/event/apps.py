from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EventConfig(AppConfig):
    """Default app config"""

    name = "apps.api.event"
    verbose_name = _("Event")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
