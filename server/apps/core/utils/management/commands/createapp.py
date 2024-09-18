import os

from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """Command create django app"""

    help = (
        "Creates a Django app directory structure"
        " for the given app name in the apps directory."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "name", type=str, help="Name of the application or project"
        )
        parser.add_argument(
            "--default",
            default=False,
            action="store_true",
            help="Create app in folder apps not subfolders",
        )
        parser.add_argument(
            "--core",
            default=False,
            action="store_true",
            help="Create app in folder core",
        )

    def handle(self, *args, **options):
        name = options["name"]
        is_default = options["default"]
        is_core = options["core"]
        path = os.path.join(settings.APPS_DIR, "api")
        template = settings.API_APP_TEMPLATE

        if is_default and is_core:
            raise CommandError("--default and --core can't be used together")
        if is_default:
            path = settings.APPS_DIR
            template = settings.DEFAULT_APP_TEMPLATE
        if is_core:
            path = os.path.join(settings.APPS_DIR, "core")
            template = settings.CORE_APP_TEMPLATE
            if not os.path.exists(path):
                raise CommandError("Package core is not exist")
        path = os.path.join(path, name)
        if not os.path.exists(path):
            os.mkdir(path)
        management.call_command(
            "startapp", name, path, f"--template={template}"
        )
