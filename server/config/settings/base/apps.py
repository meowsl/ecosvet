DEFAULT_APPS = [
    "admin_interface",
    "colorfield",
    "extra_settings",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.sitemaps",
    "import_export",
    "corsheaders",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "django_filters",
    "easy_select2",
    "service_objects",
    "ckeditor",
    "ckeditor_uploader",
    "adminsortable2",
]

PROJECT_APPS = [
    "apps.core.utils",
    "apps.core.main",
    "apps.core.api",
    "apps.api.auth",
    "apps.api.event",
    "apps.api.news",
]

DEVELOPER_APPS = [
    *DEFAULT_APPS,
    "django_extensions",
    *PROJECT_APPS,
    "debug_toolbar",
]

PRODUCTION_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
]
