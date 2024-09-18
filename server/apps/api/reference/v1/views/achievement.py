from rest_framework import generics
from apps.api.reference.models import Achievement
from apps.api.reference.v1.serializers import AchievementSerializer

class AchievementAPIListView(generics.ListAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer