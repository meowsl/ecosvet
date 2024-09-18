from rest_framework import generics, views
from apps.api.event.models import UserEvent
from apps.api.event.v1.serializers import UserEventSerializer

class UserEventAPIListView(generics.ListAPIView):
    queryset = UserEvent.objects.all()
    serializer_class = UserEventSerializer