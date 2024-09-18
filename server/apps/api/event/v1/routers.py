from django.urls import path
from .views import EventAPIListView

app_name = "event"

urlpatterns = [
    path("event/", EventAPIListView.as_view(), name="events"),
]
