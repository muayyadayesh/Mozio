from .base import *

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
