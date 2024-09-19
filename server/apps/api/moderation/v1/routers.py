from django.urls import path
from .views import ApplicationCreateAPIView, ApplicationAPIListView

app_name = "moderation"

urlpatterns = [
    path("applications/", ApplicationAPIListView.as_view(), name="application-list"),
    path("application/create/", ApplicationCreateAPIView.as_view(), name="create-application")
]
