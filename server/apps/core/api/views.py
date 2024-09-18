from django.template.loader import render_to_string
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework import permissions


class SchemaAPIView(SpectacularAPIView):
    urlconf = (path("api/", include("apps.core.api.urls")),)
    permission_classes = (permissions.AllowAny,)
    serve_public = True

    custom_settings = dict(
        TITLE=_("API"),
        DESCRIPTION=render_to_string("api/desctiption.html"),
        VERSION="1.0.0",
        CONTACT=dict(
            name="DIGITAL RSUE",
            url="https://digital.rsue.ru/",
            email="digital@rsue.ru",
        ),
        LICENSE=dict(name="MIT License"),
        SCHEMA_PATH_PREFIX="/api/v[0-9]",
        SCHEMA_PATH_PREFIX_TRIM=False,
        SCHEMA_COERCE_PATH_PK_SUFFIX=True,
        CAMELIZE_NAMES=True,
        COMPONENT_SPLIT_REQUEST=True,
        SWAGGER_UI_DIST="SIDECAR",
        SWAGGER_UI_FAVICON_HREF="SIDECAR",
        SWAGGER_UI_SETTINGS=dict(
            deepLinking=True,
            persistAuthorization=True,
            displayOperationId=True,
        ),
        POSTPROCESSING_HOOKS=(
            "drf_spectacular.contrib"
            ".djangorestframework_camel_case"
            ".camelize_serializer_fields",
        ),
    )


class SwaggerView(SpectacularSwaggerView):
    url_name = "api:schema"


class RedocView(SpectacularRedocView):
    url_name = "api:schema"
