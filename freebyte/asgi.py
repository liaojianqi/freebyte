import os

from channels.asgi import get_channel_layer
# from channels.routing import get_default_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freebyte.settings")
channel_layer = get_channel_layer()
