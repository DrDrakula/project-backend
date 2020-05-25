"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import environ
import os

ROOT_DIR = environ.Path(__file__) - 3

env = environ.Env()
if env('DJANGO_SETTINGS_MODULE') != 'config.settings.aws':
    environ.Env.read_env(env_file=ROOT_DIR('.env'))
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=True)

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'rest_auth',
    'rest_auth.registration',
    'corsheaders',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'werkzeug',
]

LOCAL_APPS = [
    'apps.api'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MAIN_URL = '/'

STATIC_URL = '/static/'

STATIC_ROOT = str(ROOT_DIR('static'))

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# media_url for production
MEDIA_URL = MAIN_URL + '/media/'
MEDIA_ROOT = str(ROOT_DIR('media'))
FILE_UPLOAD_PERMISSIONS = 0o775
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o775

# Auth and Permissions

# Configure the JWTs to expire after 6 hour,
# and allow users to refresh near-expiration tokens
import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=6),
    'JWT_ALLOW_REFRESH': True,
}

# Make JWT Auth the default authentication mechanism for Django
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'config.settings.utils.CSRFExemptSessionAuthentication',  # Prevent CSRF issue in DRF https://stackoverflow.com/questions/30871033/django-rest-framework-remove-csrf/34316546
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

# Sets serializers for the rest auth app (These were customized)
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'apps.api.serializers.custom_rest_auth.UserDetailsSerializer',
}

# Enables django-rest-auth to use JWT tokens instead of regular tokens.
REST_USE_JWT = True

# Use this model for user
AUTH_USER_MODEL = 'api.User'
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_LOGOUT_ON_GET = True
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

SITE_ID = 1

# Set up DB persistent connections
CONN_MAX_AGE = None


# Sets ask for old password before allowing change password
OLD_PASSWORD_FIELD_ENABLED = True
