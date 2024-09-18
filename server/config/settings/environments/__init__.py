# flake8: noqa
from config.settings.base import env

from .common import *

if DEBUG:
    SECRET_KEY = env(
        "SECRET_KEY",
        default="-qf)o7hs$jk@b8o)zidroo9wskuf^95m2$@k)5^@hl-=)349-7",
    )
    from .development import *
else:
    SECRET_KEY = env("SECRET_KEY")
    from .production import *
