from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from apps.api.reference.models import Achievement
from apps.api.reference.v1.serializers import AchievementSerializer

class AchievementAPIListView(generics.ListAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class AchievementCreateView(generics.CreateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = (IsAdminUser,)