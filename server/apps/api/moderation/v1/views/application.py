from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from apps.api.moderation.models import Application
from apps.api.moderation.v1.serializers import ApplicationSerializer


class ApplicationAPIListView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (IsAdminUser,)

class ApplicationCreateAPIView(generics.CreateAPIView):
    """
    Создание новой заявки
    """
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    permission_classes = (AllowAny,)