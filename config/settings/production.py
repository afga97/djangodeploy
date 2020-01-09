from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

STATIC_ROOT = "/var/www/static/tasks/"

MEDIA_ROOT = "/var/www/media/tasks/"

ALLOWED_HOSTS = [*]

DATABASES = {
    'default': {
        'ENGINE':       get_secret("ENGINE_DB"),
        'NAME':         get_secret("NAME_DB_PRODUCTION"),
        'USER':         get_secret("USER_DB_PRODUCTION"),
        'PASSWORD':     get_secret("PASSWORD_DB_PRODUCTION"),
        'HOST':         get_secret("HOST_DB_PRODUCTION"),
        'PORT':         get_secret("PORT_DB_PRODUCTION"),
    }
}