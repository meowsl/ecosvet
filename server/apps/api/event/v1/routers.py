from django.urls import path
from .views import (
    EventAPIListView,
    EventDetailView,
    UserEventAPIListView,
    UserEventRegistrationAPIView
)

app_name = "event"

urlpatterns = [
    path("event-list/", EventAPIListView.as_view(), name="events"),
    path("event/<int:pk>/", EventDetailView.as_view(), name="event_detail"),
    path("user-event/<int:pk>", UserEventAPIListView.as_view(), name="user_event"),
    path("register/", UserEventRegistrationAPIView.as_view(), name="user_event_registration")
]
