from apps.api.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователя"""

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "surname"
        )

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    full_name = serializers.CharField(write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['email', 'password', 'full_name']

    def create(self, validated_data):
        full_name = validated_data.pop('full_name')
        name_parts = full_name.split()
        first_name = name_parts[1]
        last_name = name_parts[0]
        surname = name_parts[2] if len(name_parts) > 2 else ''

        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=first_name,
            last_name=last_name,
            surname=surname
        )
        return user


class TelegramLoginSerializer(serializers.Serializer):
    telegram_id = serializers.IntegerField(required=True)
    username = serializers.CharField(max_length=150, required=True)