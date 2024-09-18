from django.contrib.admin import (
    register,
    ModelAdmin
)

from .models import News


@register(News)
class NewsAdmin(ModelAdmin):
    list_display = ("title", "publish_date")
    search_fields = ("title",)
    list_filter = ("title", "publish_date")