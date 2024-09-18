from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.api.news.models import News
from apps.api.news.v1.serializers import (
    NewsBaseSerializer, NewsDetailSerializer
)

class NewsAPIListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = News.objects.all()
    serializer_class = NewsBaseSerializer

class NewsDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer

class NewsCreateView(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsBaseSerializer

class NewsUpdateView(generics.UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsBaseSerializer

class NewsDeleteView(generics.DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsBaseSerializer