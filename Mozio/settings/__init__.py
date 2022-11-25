from .base import *
import os


if os.environ.get("DJANGO_SETTINGS_MODULE") == 'Production':
    from .production import *
else:
    from .local import *
