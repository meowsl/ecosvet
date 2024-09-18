from rest_framework import serializers
from apps.api.blog.models import Post

class PostBasicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["id", "title", "text", "content_type", "image"]

class PostDetailSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"