from rest_framework import serializers
from apps.api.moderation.models import Application

class ApplicationSerializer(models.Model):

    class Meta:
        model = Application
        fields = "__all__"

