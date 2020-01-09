from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_ROOT = "/var/www/static/tasks/"

MEDIA_ROOT = "/var/www/media/tasks/"

DATABASES = {
    'default': {
        'ENGINE':       get_secret("ENGINE_DB"),
        'NAME':         get_secret("NAME_DB_DEV"),
        'USER':         get_secret("USER_DB_DEV"),
        'PASSWORD':     get_secret("PASSWORD_DB_DEV"),
        'HOST':         get_secret("HOST_DB_DEV"),
        'PORT':         get_secret("PORT_DB_DEV"),
    }
}