from rest_framework.response import Response
from rest_framework import views, generics, status
from rest_framework.permissions import AllowAny
from apps.api.event.v1.serializers import EventBasicSerializer, EventDetailSerializer
from apps.api.event.models import Event, UserEvent
from apps.api.event.v1.permissions import IsEventAuthor

class EventAPIListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Event.objects.all()
    serializer_class = EventBasicSerializer

class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

    def perform_create(self, serializer):
        event = serializer.save(author=self.request.user)
        UserEvent.objects.create(user=self.request.user, event=event)

class EventUpdateView(generics.UpdateAPIView):
    permission_classes = [IsEventAuthor]
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

class EventDeleteView(generics.DestroyAPIView):
    permission_classes = [IsEventAuthor]
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

class EventDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

