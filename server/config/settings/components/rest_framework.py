"""Rest framework settings"""
from ..environments import env

DATE_INPUT_FORMATS = [
    ("%d-%m-%Y"),
    ("%d.%m.%Y"),
    ("%d/%m/%Y"),
    "iso-8601",
]


REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        # "rest_framework.permissions.IsAuthenticated",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    "DEFAULT_RENDERER_CLASSES": (
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
        "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": (
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DATE_FORMAT": "%d.%m.%Y",
    "DATE_INPUT_FORMATS": DATE_INPUT_FORMATS,
    "DATETIME_FORMAT": "%d.%m.%Y %H:%M",
}

CORS_ALLOW_CREDENTIALS = True

if env("DEBUG"):
    CORS_ALLOWED_ORIGINS = ("https://localhost:8080",)
else:
    CORS_ALLOWED_ORIGINS = list(
        map(lambda d: f"https://{str.strip(d)}", env("SITE_DOMAIN").split(","))
    )
