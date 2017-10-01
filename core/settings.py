"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#i9@vu0!1!%sic($$1($@dcn0!#um6*b)uv4pl9t@flb*%vpl6'


# AWS_ACCESS_KEY_ID = os.environ.get('AKIAIREUGRU2A57Q5UAA')
# AWS_SECRET_ACCESS_KEY = os.environ.get('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')
# AWS_STORAGE_BUCKET_NAME = 'cneweb'

# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
# ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'control',
    'storages',
    # 'djcelery',
    # 'kombu.transport.django',
    # 'djcelery_email',
]

# import djcelery
# djcelery.setup_loader()
# BROKER_URL = 'django://'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
PROJECT_ROOT = 'core'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates').replace('\\','/'),],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {}

# DATABASES['default'] =  dj_database_url.config(default='postgres://user:pass@host/db')
# DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'

DATABASES['default'] = dj_database_url.config(default='sqlite:////{0}'.format(os.path.join(BASE_DIR, 'db.sqlite3')))


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'coredev2017@gmail.com'

#Must generate specific password for your app in [gmail settings][1]
EMAIL_HOST_PASSWORD = 'Tw3nty53v3n'

EMAIL_PORT = 587

#This did the trick
#DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT= os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT= os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

S3_USE_SIGV4 = True
#Storage on S3 settings are stored as os.environs to keep settings.py clean 
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
if not DEBUG:
   AWS_STORAGE_BUCKET_NAME = 'corewebapp'
   AWS_ACCESS_KEY_ID = 'AKIAJT2MOLQOQG42XBMQ'
   AWS_SECRET_ACCESS_KEY = '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'
   AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
   AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
    }
   # STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
   AWS_LOCATION = 'static'
   S3_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
   STATIC_URL = S3_URL