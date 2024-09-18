from rest_framework.permissions import AllowAny
from rest_framework import generics, views
from apps.api.event.models import UserEvent, Event
from apps.api.event.v1.serializers import (
    UserEventSerializer,
    UserEventRegistrationSerializer
)

class UserEventAPIListView(generics.ListAPIView):
    queryset = UserEvent.objects.all()
    serializer_class = UserEventSerializer

class UserEventRegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Event.objects.all()
    serializer_class = UserEventRegistrationSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['event'] = self.get_object()
        return context