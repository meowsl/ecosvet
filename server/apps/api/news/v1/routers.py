from django.urls import path
from .views import (
    NewsAPIListView,
    NewsCreateView,
    NewsDeleteView,
    NewsUpdateView,
    NewsDetailView
)

app_name = "news"

urlpatterns = [
    path("news-list/", NewsAPIListView.as_view(), name="news-list"),
    path("news/<int:pk>/", NewsDetailView.as_view(), name="news-detail"),
    path("news/create/", NewsCreateView.as_view(), name="news-create"),
    path("news/<int:pk>/update/", NewsUpdateView.as_view(), name="news-update"),
    path("news/<int:pk>/delete", NewsDeleteView.as_view(), name="news-delete")
]
