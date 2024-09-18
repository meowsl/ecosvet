from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, views
from apps.api.event.models import UserEvent, Event
from apps.api.event.v1.serializers import (
    UserEventSerializer,
    UserEventRegistrationSerializer
)

class UserEventAPIListView(generics.ListAPIView):
    queryset = UserEvent.objects.all()
    serializer_class = UserEventSerializer

    def get_queryset(self):
        user = self.request.user
        return UserEvent.objects.filter(user=user)

class UserEventCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserEvent.objects.all()
    serializer_class = UserEventSerializer

    def perform_create(self, serializer):
        event_id = self.kwargs.get("pk")
        event = Event.objects.get(id=event_id)
        serializer.save(user=self.request.user, event=event)

class UserEventRegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Event.objects.all()
    serializer_class = UserEventRegistrationSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['event'] = self.get_object()
        return context