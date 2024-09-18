from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NewsConfig(AppConfig):
    """Default app config"""

    name = "apps.api.news"
    verbose_name = _("News")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
