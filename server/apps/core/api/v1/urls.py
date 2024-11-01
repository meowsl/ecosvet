from django.urls import include, path

app_name = "v1"

urlpatterns = [
    path("auth/", include("apps.api.auth.v1")),
    path("events/", include("apps.api.event.v1")),
    path("news/", include("apps.api.news.v1")),
    path("blog/", include("apps.api.blog.v1")),
    path("reference/", include("apps.api.reference.v1")),
    path("moderation/", include("apps.api.moderation.v1"))
]
