from django.urls import include, path

from .views import RedocView, SchemaAPIView, SwaggerView

app_name = "api"

urlpatterns = [
    path(
        "schema/",
        SchemaAPIView().as_view(),
        name="schema",
    ),
    path(
        "",
        SwaggerView().as_view(),
        name="documentation",
    ),
    path("redoc/", RedocView().as_view()),
    path("v1/", include("apps.core.api.v1")),
]
