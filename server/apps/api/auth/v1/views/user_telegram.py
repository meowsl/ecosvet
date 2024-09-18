from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from apps.api.auth.models import UserTelegram, User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny
from apps.api.auth.v1.serializers import TelegramLoginSerializer

class TelegramLoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = TelegramLoginSerializer

    def post(self, request, *args, **kwargs):
        telegram_id = request.data.get('telegram_id')
        username = request.data.get('username')
        if not telegram_id:
            return Response({'error': 'telegram_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_telegram = UserTelegram.objects.get(telegram_id=telegram_id)
            user = user_telegram.user
        except UserTelegram.DoesNotExist:
            password = make_password(None)
            user = User.objects.create(username=username, password=password)
            UserTelegram.objects.create(user=user, telegram_id=telegram_id)

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })