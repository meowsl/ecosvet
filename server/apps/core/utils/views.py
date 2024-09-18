from rest_framework.response import Response
from rest_framework.serializers import (
    CharField,
    IntegerField,
    Serializer,
    SerializerMethodField,
)
from rest_framework.views import APIView


class BaseChoiceView(APIView):
    """
    Базовый класс представления API
    для получения списка choices
    """

    objects = None

    class ChoiceSerializer(Serializer):
        """Сериализатор для ModelChoice"""

        id = IntegerField(read_only=True)
        name = CharField(read_only=True, max_length=100)
        short_name = SerializerMethodField()

        def get_short_name(self, obj):
            return obj["name"][0]

    def choice_to_dict(self, items):
        """Метод преобразовывает ModelChoice в dict"""
        for el in items:
            yield {"id": el[0], "name": el[1]}

    def get(self, request):
        objetcs = list(self.choice_to_dict(self.objects))
        serializer = self.ChoiceSerializer(objetcs, many=True)
        return Response(serializer.data)
