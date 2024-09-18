import os

import environ

CONFIG_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
APP_DIR = os.path.dirname(CONFIG_DIR)
PROJECT_DIR = os.path.dirname(APP_DIR)
ENV_FILE = os.path.join(PROJECT_DIR, ".env")


env = environ.Env(
    DEBUG=(bool, True),
    USE_SQLITE=(bool, True),
    USE_FILE_EMAIL_BACKEND=(bool, True),
)

if os.path.isfile(ENV_FILE):
    env.read_env(ENV_FILE)
