from rest_framework import serializers
from apps.api.event.models import Event, UserEvent

class EventBasicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ["id", "name", "description", "image"]


class EventDetailSerializer(serializers.ModelSerializer):

    is_registered = serializers.SerializerMethodField()
    author = serializers.CharField(source="author.username")
    class Meta:
        model = Event
        fields = "__all__"

    def get_is_registered(self, obj):
        user = self.context["request"].user
        return UserEvent.objects.filter(user=user, event=obj).exists()


class UserEventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEvent
        fields = ["user", "event"]