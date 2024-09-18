from django.urls import include, path, re_path

from .views import MainRedirectView

urlpatterns = [
    path("", MainRedirectView.as_view()),
    re_path(r"^ckeditor/", include("ckeditor_uploader.urls")),
    path("api/", include("apps.core.api.urls"), name="api"),
]
