from django.urls import path
from .views import (
    PostAPIListView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostUpdateView
)

app_name = "blog"

urlpatterns = [
    path("post-list/", PostAPIListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete")
]
