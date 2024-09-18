from django.contrib.admin import (
    register,
    ModelAdmin
)
from .models import (
    Event,
    UserEvent
)


@register(Event)
class EventAdmin(ModelAdmin):
    list_display = ("name", "date", "address", "author")
    search_fields = ("name", "author")

@register(UserEvent)
class UserEventAdmin(ModelAdmin):
    list_display = ("user", "event")
    search_fields = ("user", "event")