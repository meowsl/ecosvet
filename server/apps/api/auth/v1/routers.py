from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    UserAPIView,
    UserRegistrationView,
    TelegramLoginView
)

app_name = "auth"

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("info/", UserAPIView.as_view(), name="get_user_info"),
    path("register/", UserRegistrationView.as_view(), name="register-user"),
    path("telegram-login/", TelegramLoginView.as_view(), name="telegram-login"),
]
