from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command create django app"""

    help = (
        "Creates a Django app directory structure"
        " for the given app name in the apps directory."
    )

    def handle(self, *args, **options):
        if not settings.DEFAULT_FIXTURES:
            self.stdout.write(
                self.style.SUCCESS("  • Default fixtures not found")
            )

        for name in settings.DEFAULT_FIXTURES:
            management.call_command("loaddata", name)

        if settings.DEFAULT_FIXTURES:
            count = len(settings.DEFAULT_FIXTURES)
            self.stdout.write(
                self.style.SUCCESS(f"  • Fixtures count completed:{count}")
            )
