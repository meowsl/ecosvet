from django.db.models import Model
from rest_framework.serializers import ModelSerializer, Serializer


def get_serializer_class(
    *,
    fields: dict,
):
    return type("", (Serializer,), fields)


def inline_serializer(*, fields: dict, **kwargs):
    serializer_class = get_serializer_class(fields=fields)
    return serializer_class(**kwargs)


def get_model_serializer_class(
    *,
    model: Model,
    model_fields: list = None,
    fields: dict = None,
    ref_name: str = None,
):
    fields = fields or {}
    name = f"{model.__name__}Serializer"

    meta_class = type(
        "Meta",
        (object,),
        {
            "model": model,
            "fields": model_fields or "__all__",
            "ref_name": ref_name or model.__name__,
        },
    )

    return type(name, (ModelSerializer,), {"Meta": meta_class, **fields})


def inline_model_serializer(
    *,
    model: Model,
    model_fields: list = None,
    fields: dict = None,
    ref_name: str = None,
    **kwargs,
):
    fields = fields or {}
    model_fields = model_fields or "__all__"

    serializer_class = get_model_serializer_class(
        model=model,
        model_fields=model_fields,
        fields=fields,
        ref_name=ref_name,
    )

    return serializer_class(**kwargs)
