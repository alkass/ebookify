#!/usr/bin/env python
import os
from django.core.management import execute_from_command_line as execute

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ebookify.settings")
    execute(["manage.py", "createsuperuser"])
