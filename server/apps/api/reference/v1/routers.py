from django.urls import path
from apps.api.reference.v1.views import AchievementAPIListView, AchievementCreateView

app_name = "reference"

urlpatterns = [
    path("achievements/", AchievementAPIListView.as_view(), name="achievement-list"),
    path("achievement/create/", AchievementCreateView.as_view(), name="create-achievement")
]
