from django.contrib.admin import (
    register,
    ModelAdmin
)
from .models import Event


@register(Event)
class EventAdmin(ModelAdmin):
    list_display = ("name", "date", "address", "author")
    search_fields = ("name", "author")