import os
import shutil

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command remove assets files"""

    help = "Remove assets files"

    def clean_public_static_dir(self):
        try:
            for root, folders, files in os.walk(settings.PUBLIC_STATIC_DIR):
                for file in files:
                    if file != ".gitignore":
                        os.remove(os.path.join(root, file))
                for folder in folders:
                    shutil.rmtree(os.path.join(root, folder))

            self.stdout.write(
                self.style.SUCCESS(
                    f"  • Folder {settings.PUBLIC_STATIC_DIR} cleaned"
                )
            )
        except FileNotFoundError:
            pass

    def handle(self, *args, **options):
        self.clean_public_static_dir()
