from apps.api.auth.models import User
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class UserSerializer(ModelSerializer):
    """Сериализатор пользователя"""

    questionnaire_type_name = SerializerMethodField()
    faculty_name = SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "surname",
            "role",
            "faculty",
            "faculty_name",
            "questionnaire_type",
            "questionnaire_type_name",
            "organization",
        )

    def get_questionnaire_type_name(self, obj):
        if obj.questionnaire_type:
            return obj.questionnaire_type.name
        return ""

    def get_faculty_name(self, obj):
        if obj.faculty:
            return obj.faculty.name
        return ""
