#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freebyte.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

# TODO:WebSocket channels upgrade to 2.0
