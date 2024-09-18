from rest_framework import serializers
from apps.api.event.models import UserEvent
from apps.api.auth.models import User

class UserEventSerializer(serializers.ModelSerializer):

    user = serializers.CharField(source="user.username")
    event = serializers.CharField(source="event.name")

    class Meta:
        model = UserEvent
        fields = "__all__"