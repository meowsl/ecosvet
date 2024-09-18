from drf_spectacular.extensions import OpenApiSerializerFieldExtension
from rest_framework import serializers


class ChoiceField(serializers.ChoiceField):
    def to_representation(self, value):
        return {
            "label": self._choices[value],
            "value": super().to_representation(value),
        }


class IntegerChoiceField(ChoiceField):
    pass


class TextChoiceField(ChoiceField):
    pass


class IntegerChoiceFieldSchema(OpenApiSerializerFieldExtension):
    target_class = "apps.core.utils.fields.IntegerChoiceField"

    def map_serializer_field(self, auto_schema, direction):
        return {
            "type": "object",
            "properties": {
                "label": {"type": "string"},
                "value": {"type": "integer"},
            },
        }


class TextChoiceFieldSchema(OpenApiSerializerFieldExtension):
    target_class = "apps.core.utils.fields.TextChoiceField"

    def map_serializer_field(self, auto_schema, direction):
        return {
            "type": "object",
            "properties": {
                "label": {"type": "string"},
                "value": {"type": "string"},
            },
        }
