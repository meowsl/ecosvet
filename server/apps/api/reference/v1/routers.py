from django.urls import path
from apps.api.reference.v1.views import AchievementAPIListView

app_name = "reference"

urlpatterns = [
    path("achievements/", AchievementAPIListView.as_view(), name="achievement-list"),
]
