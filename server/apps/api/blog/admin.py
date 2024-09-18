from django.contrib.admin import (
    register, ModelAdmin
)
from .models import Post


@register(Post)
class PostAdmin(ModelAdmin):
    list_display = ["title", "author", "publish_date", "content_type"]
    search_fields = ["title", "author", "publish_date"]
    list_filter = ["title", "author", "publish_date"]