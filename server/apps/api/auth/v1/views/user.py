from rest_framework import generics, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from apps.api.auth.v1.serializers import (
    UserSerializer,
    UserRegistrationSerializer
)
from apps.api.auth.models import User

class UserAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def get(self, request):
        user = request.user
        return Response(self.get_serializer(user, read_only=True).data)

class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer