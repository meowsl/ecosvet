from django.urls import path
from .views import (
    EventAPIListView,
    EventDetailView,
    EventUpdateView,
    EventDeleteView,
    EventCreateView,
    UserEventAPIListView,
    UserEventRegistrationView,
    UserEventCreateView
)

app_name = "event"

urlpatterns = [
    path("event-list/", EventAPIListView.as_view(), name="event-list"),
    path("event/<int:pk>/", EventDetailView.as_view(), name="event-detail"),
    path("event/create/", EventCreateView.as_view(), name="event-create"),
    path("event/<int:pk>/update/", EventUpdateView.as_view(), name="event-update"),
    path("event/<int:pk>/delete/", EventDeleteView.as_view(), name="event-delete"),
    path("user-event/", UserEventAPIListView.as_view(), name="user_event"),
    path("event/<int:pk>/register/", UserEventRegistrationView.as_view(), name="event-registration"),
    path("event/<int:pk>/join/", UserEventCreateView.as_view(), name="event-join")
]
