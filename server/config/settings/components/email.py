"""Email settings"""

from config.settings.base import env

from .paths import LOGS_DIR

EMAIL_SUBJECT_PREFIX = ""
SERVER_EMAIL = env("EMAIL_NAME", default="no-reply@localhost")
DEFAULT_FROM_EMAIL = env("EMAIL_NAME", default="no-reply@localhost")
MANAGERS = [
    ("Manager", env("EMAIL_MANAGER", default="manager@localhost")),
]

if env("USE_FILE_EMAIL_BACKEND", default=True):
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = LOGS_DIR
else:
    EMAIL_CONFIG = env.email_url(
        "EMAIL_URL", default="smtp+ssl://user:password@localhost:25"
    )
    vars().update(EMAIL_CONFIG)
