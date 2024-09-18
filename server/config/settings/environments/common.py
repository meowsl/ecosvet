"""Common settings"""

from config.settings.base import env
from config.settings.components.paths import TEMPLATES_DIR

DEBUG = env("DEBUG", default=True)

ADMIN_USERNAME = env("ADMIN_USERNAME", default=None)
ADMIN_PASSWORD = env("ADMIN_PASSWORD", default=None)
ADMIN_EMAIL = env("ADMIN_EMAIL", default=None)

DEFAULT_FIXTURES = env.list("DEFAULT_FIXTURES", default=[])

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            TEMPLATES_DIR,
        ],
        "OPTIONS": {
            "loaders": [
                "apptemplates.Loader",
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
            ],
        },
    },
]

SITE_ID = 1

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]
