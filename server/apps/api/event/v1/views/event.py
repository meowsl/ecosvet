from rest_framework import views, generics
from rest_framework.permissions import AllowAny
from apps.api.event.v1.serializers import EventBasicSerializer, EventDetailSerializer
from apps.api.event.models import Event

class EventAPIListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Event.objects.all()
    serializer_class = EventBasicSerializer

class EventDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer