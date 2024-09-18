"""Internationalization settings"""
from .paths import LOCALE_DIR

LANGUAGE_CODE = "ru"
LANGUAGES = (("ru", "Русский"), ("en", "English"))
TIME_ZONE = "Europe/Moscow"
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = (LOCALE_DIR,)
