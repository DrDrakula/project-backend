import os
from .base import *


ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]

CORS_ORIGIN_WHITELIST = (
    'http://localhost',
)

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': '',
        'PORT': '',
    }
}
