"""
Settings file for OpenSlides.
"""

# SECURITY WARNING: Keep the secret key used in production secret! CHANGE THIS
SECRET_KEY = 'CQoRStjigwstY!4jCS@u@i!hFijgq*mgmL4iS64Q*9pr%%Yd6f'

# Email settings
# For SSL/TLS specific settings see https://docs.djangoproject.com/en/1.11/topics/email/#smtp-backend
EMAIL_USE_SSL = True
EMAIL_HOST = 'example.de'
EMAIL_PORT = '465'
EMAIL_HOST_USER = 'slides@example.de'
EMAIL_HOST_PASSWORD = 'EMAILPASSWORD'
DEFAULT_FROM_EMAIL = 'slides@example.de'

# Jitsi integration
JITSI_DOMAIN = 'meet.example.de' 
JITSI_ROOM_NAME = 'ROOMNAME'
JITSI_PASSWORD = 'PASSWORD'

# Controls if electronic voting (means non-analog polls) are enabled.
ENABLE_ELECTRONIC_VOTING = True

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

TIME_ZONE = 'Europe/Berlin'





## Advanced Options below

import os
from openslides.global_settings import *

# The directory for user specific data files
OPENSLIDES_USER_DATA_DIR = '/root/.local/share/openslides'

# Add plugins to this list (see example entry in comment).
INSTALLED_PLUGINS += (
#    'plugin_module_name',
)

INSTALLED_APPS += INSTALLED_PLUGINS

# Important settings for production use
# https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/


# Use 'DEBUG = True' to get more details for server errors.
# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = False

# Controls the verbosity on errors during a reset password. If enabled, an error
# will be shown, if there does not exist a user with a given email address. So one
# can check, if a email is registered. If this is not wanted, disable verbose
# messages. An success message will always be shown.

RESET_PASSWORD_VERBOSE_ERRORS = False


# Increasing Upload size to 100mb (default is 2.5mb)
DATA_UPLOAD_MAX_MEMORY_SIZE = 104857600

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# Change this setting to use e. g. PostgreSQL or MySQL.

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mydatabase',
#         'USER': 'mydatabaseuser',
#         'PASSWORD': 'mypassword',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(OPENSLIDES_USER_DATA_DIR, 'db.sqlite3'),
    }
}


# Set use_redis to True to activate redis as cache-, asgi- and session backend.
use_redis = False

if use_redis:
    # Django Channels

    # https://channels.readthedocs.io/en/latest/topics/channel_layers.html#configuration
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [("localhost", 6379)],
                "capacity": 100000,
            },
        },
    }
    # Collection Cache

    # Can be:
    # a Redis URI — "redis://host:6379/0?encoding=utf-8";
    # a (host, port) tuple — ('localhost', 6379);
    # or a unix domain socket path string — "/path/to/redis.sock".
    REDIS_ADDRESS = "redis://127.0.0.1"
    # REDIS_READ_ONLY_ADDRESS
    AMOUNT_REPLICAS = 1

    # Session backend

    # Redis configuration for django-redis-sessions.
    # https://github.com/martinrusev/django-redis-sessions

    SESSION_ENGINE = 'redis_sessions.session'
    SESSION_REDIS = {
        'host': '127.0.0.1',
        'port': 6379,
        'db': 0,
        'prefix': 'session',
        'socket_timeout': 2
    }

# SAML integration
# Please read https://github.com/OpenSlides/OpenSlides/blob/master/openslides/saml/README.md
# for additional requirements.

ENABLE_SAML = False
if ENABLE_SAML:
    INSTALLED_APPS += ['openslides.saml']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_DIRS = [os.path.join(OPENSLIDES_USER_DATA_DIR, 'static')] + STATICFILES_DIRS

STATIC_ROOT = os.path.join(OPENSLIDES_USER_DATA_DIR, 'collected-static')


# Files
# https://docs.djangoproject.com/en/1.10/topics/files/

MEDIA_ROOT = os.path.join(OPENSLIDES_USER_DATA_DIR, 'media', '')


# Password validation
# https://docs.djangoproject.com/en/1.10/topics/auth/passwords/#module-django.contrib.auth.password_validation
# AUTH_PASSWORD_VALIDATORS = []


# Logging
# see https://docs.djangoproject.com/en/2.2/topics/logging/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'gunicorn': {
            'format': '{asctime} [{process:d}] [{levelname}] {name} {message}',
            'style': '{',
            'datefmt': '[%Y-%m-%d %H:%M:%S %z]',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'gunicorn',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'openslides': {
            'handlers': ['console'],
            'level': os.getenv('OPENSLIDES_LOG_LEVEL', 'INFO'),
        }
    },
}

SETTINGS_FILEPATH = __file__
