from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _


class ProxyGroup(Group):
    class Meta:
        proxy = True
        verbose_name = _("group")
        verbose_name_plural = _("groups")