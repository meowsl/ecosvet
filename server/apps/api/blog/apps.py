from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlogConfig(AppConfig):
    """Default app config"""

    name = "apps.api.blog"
    verbose_name = _("Blog")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
