"""Logging settings"""

# from .paths import LOG_FILE

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "request": {
#             "format": (
#                 "{levelname} {asctime} {status_code} {request} ",
#                 "{module} {process:d} {thread:d} {message}",
#             ),
#             "style": "{",
#         },
#     },
#     "handlers": {
#         "file-request": {
#             "class": "logging.FileHandler",
#             "filename": LOG_FILE,
#             "formatter": "request",
#         }
#     },
#     "loggers": {
#         "django.request": {"handlers": ["file-request"], "propagate": True,}
#     },
# }
