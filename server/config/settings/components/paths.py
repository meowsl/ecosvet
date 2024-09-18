"""Paths settings"""

import os

# Base
CONFIG_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
APP_DIR = os.path.dirname(CONFIG_DIR)
PROJECT_DIR = os.path.dirname(APP_DIR)
ENV_FILE = os.path.join(PROJECT_DIR, ".env")
ENV_FILE_EXAMPLE = os.path.join(PROJECT_DIR, ".env.example")

# Nginx
PUBLIC_DIR = os.path.join(PROJECT_DIR, "public")
PRIVATE_DIR = os.path.join(PROJECT_DIR, "private")
PUBLIC_MEDIA_DIR = os.path.join(PUBLIC_DIR, "media")
PUBLIC_STATIC_DIR = os.path.join(PUBLIC_DIR, "static")

# Backend
LOGS_DIR = os.path.join(PRIVATE_DIR, "logs")
APPS_DIR = os.path.join(APP_DIR, "apps")
FIXTURES_DIR = os.path.join(APP_DIR, "fixtures")
LOG_FILE = os.path.join(LOGS_DIR, "django-error.log")
DEV_DATABASE_FILE = os.path.join(PRIVATE_DIR, "db.sqlite3")
TEST_DATABASE_FILE = os.path.join(PRIVATE_DIR, "test_db.sqlite3")
FIXTURE_DIRS = [
    FIXTURES_DIR,
]

# Apps templates
APP_TEMPLATES = os.path.join(APPS_DIR, "core", "utils", "app_templates")
API_APP_TEMPLATE = os.path.join(APP_TEMPLATES, "api.zip")
CORE_APP_TEMPLATE = os.path.join(APP_TEMPLATES, "core.zip")
DEFAULT_APP_TEMPLATE = os.path.join(APP_TEMPLATES, "default.zip")

# Frontend
STATIC_DIR = os.path.join(PRIVATE_DIR, "static")
DIST_DIR = os.path.join(STATIC_DIR, "dist")
TEMPLATES_DIR = os.path.join(APP_DIR, "templates")

# Locale
LOCALE_DIR = os.path.join(PRIVATE_DIR, "locale")
