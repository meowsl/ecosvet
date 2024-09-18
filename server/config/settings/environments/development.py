"""Development settings"""

from config.settings.base import DEVELOPER_APPS, DEVELOPER_MIDDLEWARE, env
from config.settings.components.paths import (
    DEV_DATABASE_FILE,
    TEST_DATABASE_FILE,
)

INTERNAL_IPS = [
    "127.0.0.1",
]
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [*DEVELOPER_APPS]

MIDDLEWARE = [
    *DEVELOPER_MIDDLEWARE
]

if env("USE_SQLITE", default=True):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": DEV_DATABASE_FILE,
            "TEST": {"NAME": TEST_DATABASE_FILE,},
        },
    }
else:
    DATABASES = {
        "default": env.db(),
    }
