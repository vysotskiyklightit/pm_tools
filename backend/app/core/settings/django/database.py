import os

from .app import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB', 'not set'),
        'USER': os.environ.get('POSTGRES_USER', 'not set'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'not set'),
        'HOST': os.environ.get('POSTGRES_SERVER', 'not set'),
        'PORT': '',
    }
}
