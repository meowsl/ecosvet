from rest_framework import serializers
from apps.api.event.models import UserEvent
from apps.api.auth.models import User

class UserEventSerializer(serializers.ModelSerializer):

    user = serializers.CharField(source="user.username", read_only=True)
    event = serializers.CharField(source="event.name", read_only=True)

    class Meta:
        model = UserEvent
        fields = "__all__"

class UserEventRegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField()
    event = serializers.IntegerField()

    class Meta:
        model = UserEvent
        fields = ["first_name", "last_name", "surname", "email", "event"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            surname=validated_data.get('surname')
        )
        event = validated_data['event']
        user_event = UserEvent.objects.create(user=user, event_id=event)
        return validated_data

