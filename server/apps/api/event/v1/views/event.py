from rest_framework.response import Response
from rest_framework import views, generics, status
from rest_framework.permissions import AllowAny
from apps.api.event.v1.serializers import EventBasicSerializer, EventDetailSerializer, UserEventRegistrationSerializer
from apps.api.event.models import Event, UserEvent

class EventAPIListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Event.objects.all()
    serializer_class = EventBasicSerializer

class EventDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

class UserEventRegistrationAPIView(generics.CreateAPIView):
    queryset = UserEvent.objects.all()
    serializer_class = UserEventRegistrationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)