import os
import random

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command init .env file"""

    help = "Create .env file from .env.example and generate SECRET_KEY"

    def add_arguments(self, parser):
        parser.add_argument(
            "--debug",
            default=False,
            action="store_true",
            help="Create .env file with settings for debugging",
        )

    def get_example_env(self):
        """Get content .env.example"""
        path_example = settings.ENV_FILE_EXAMPLE
        example = open(path_example, "r")
        return example.read()

    def generate_secret_key(self):
        """Generate secret key"""
        return "".join(
            [
                random.choice(
                    "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
                )
                for i in range(50)
            ]
        )

    def create_env_file(self, content, is_debug):
        """Create .env file if not exist"""
        path = settings.ENV_FILE
        if not os.path.exists(path):
            env = open(path, "w+")
            env.write(content)
            env.close()

            message = ".env file for production created"

            if is_debug:
                message = ".env file for debug created"

            self.stdout.write(self.style.SUCCESS(f"  • {message}"))
            return

        self.stdout.write(self.style.SUCCESS("  • .env file already exists"))

    def replace_line(self, content, old_value, new_value):
        """Replace line"""
        lines = content.splitlines(True)
        lines = map(
            lambda l: l if old_value not in l else f"{new_value}\n", lines
        )

        return "".join(lines)

    def handle(self, *args, **options):
        is_debug = options["debug"]
        content = self.get_example_env()
        key = self.generate_secret_key()

        content = self.replace_line(
            content, "SECRET_KEY", f"SECRET_KEY='{key}'"
        )

        if is_debug:
            content = self.replace_line(content, "DEBUG", "DEBUG=True")
            content = self.replace_line(
                content, "USE_SQLITE", "USE_SQLITE=True"
            )
            content = self.replace_line(
                content,
                "USE_FILE_EMAIL_BACKEND",
                "USE_FILE_EMAIL_BACKEND=True",
            )
            content = self.replace_line(
                content, "SITE_DOMAIN", "SITE_DOMAIN='*'"
            )

        self.create_env_file(content, is_debug)
