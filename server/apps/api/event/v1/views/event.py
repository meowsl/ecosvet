from rest_framework import views, generics
from apps.api.event.v1.serializers import EventSerializer
from apps.api.event.models import Event


class EventAPIListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer