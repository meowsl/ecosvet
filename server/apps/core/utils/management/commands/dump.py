import os
from datetime import datetime

from django.conf import settings
from django.core.management.commands import dumpdata


class Command(dumpdata.Command):
    """Command generate fixtures file"""

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            "--pretty",
            default=False,
            action="store_true",
            dest="pretty",
            help="Avoid unicode escape symbols",
        )
        parser.add_argument(
            "--unique",
            default=False,
            action="store_true",
            dest="unique",
            help="Generate unique name file",
        )

    def get_name_file(self, args, unique: bool, file_format: str):
        """Get file name dump"""
        name = "all"
        suffix = ""
        if unique:
            timestamp = str(datetime.timestamp(datetime.now()))
            timestamp = timestamp[: timestamp.find(".")]
            suffix = f"_{timestamp}"
        if args:
            if len(args) == 1:
                name = args[0].replace(".", "_")
            else:
                apps = list(set(map(lambda s: s[: s.find(".")], args)))
                if len(apps) == 1:
                    name = apps[0]
                else:
                    name = "_".join(apps)
        return f"{name}{suffix}.{file_format}"

    def handle(self, *args, **kwargs):
        name = self.get_name_file(args, kwargs["unique"], kwargs["format"])
        path = os.path.join(settings.FIXTURES_DIR, name)
        kwargs["output"] = path
        data = super().handle(*args, **kwargs)
        if kwargs.get("pretty"):
            content = (
                open(path)
                .read()
                .encode()
                .decode("unicode_escape")
                .encode("utf8")
            )
            open(path, "wb").write(content)
        return data
