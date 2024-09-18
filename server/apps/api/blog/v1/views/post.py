from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.api.blog.models import Post
from apps.api.blog.v1.serializers import (
    PostBasicSerializer,
    PostDetailSerialiser
)

class PostAPIListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostBasicSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        content_type = self.request.query_params.get("content_type")
        if content_type is not None:
            queryset = queryset.filter(content_type=content_type)
        return queryset

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerialiser

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerialiser

class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerialiser

class PostDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerialiser