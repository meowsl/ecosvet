"""Auth settings"""
from datetime import timedelta

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth"
            ".password_validation.UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth" ".password_validation.MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth"
            ".password_validation.CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth"
            ".password_validation.NumericPasswordValidator"
        ),
    },
]

LOGIN_URL = "/auth/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

AUTH_USER_MODEL = "auth_api.User"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

REST_SESSION_LOGIN = True
REST_USE_JWT = True
JWT_AUTH_COOKIE = "access-token"
JWT_AUTH_SECURE = True
JWT_AUTH_HTTPONLY = True
JWT_AUTH_SAMESITE = "None"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
}
