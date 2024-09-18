from django.conf import settings
from django.urls import reverse
from django.views.generic.base import RedirectView
from extra_settings.models import Setting


class MainRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if settings.DEBUG or self.request.user.is_staff:
            url = reverse("admin:index")
        else:
            url = Setting.get(
                "MAIN_REDIRECT_URL", default=settings.DEFAULT_REDIRECT_URL
            )

        return url
