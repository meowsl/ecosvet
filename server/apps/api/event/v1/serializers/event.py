from rest_framework import serializers
from apps.api.event.models import Event

class EventBasicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ["id", "name", "description", "image"]


class EventDetailSerializer(serializers.ModelSerializer):

    author = serializers.CharField(source="author.username")
    class Meta:
        model = Event
        fields = "__all__"
