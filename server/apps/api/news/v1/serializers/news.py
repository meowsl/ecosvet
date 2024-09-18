from rest_framework import serializers
from apps.api.news.models import News

class NewsBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ["id", "title", "text", "image"]

class NewsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = "__all__"