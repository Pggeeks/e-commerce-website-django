exit
"""
Django settings for cwp project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY = 'django-insecure-a7ah-lr6bp_0vx2)*2#^a0&#%*v-vdr4=g@t9+bd_srt3sqxlk' 


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ["django-course-selling.herokuapp.com","localhost","*"]

WSGI_APPLICATION = 'cwp.wsgi.application'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'whitenoise.runserver_nostatic',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'courses',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cwp.urls'

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

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# for herokuapp databases settings
# DATABASES = {

#     'default': {

#         'ENGINE': 'django.db.backends.postgresql_psycopg2',

#         'NAME': os.environ['DB_NAME'],

#         'USER': os.environ['DB_USER'],

#         'PASSWORD': os.environ['DB_PASSWORD'],

#         'HOST': os.environ['DB_HOST'],

#         'PORT': '5432',

#     }

# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
APPEND_SLASH = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = 'files/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'files/media')
# kEY_ID = os.environ['SECRET_ID_PAYMENT']
# KEY_SECRET = os.environ['SECRET_KEY_PAYMENT']
kEY_ID = "rzp_test_VaHuboa2uUNBiN"
KEY_SECRET = "9QYaDYFfE3Xc5jGdJSx1xbld"
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#smpt configration ( simple mail tranfer protocol)
# for forgot password feature commented for safety puposes
# EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST='smtp.gmail.com'
# EMAIL_PORT='587'
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER = os.environ['HOST_MAIL']
# EMAIL_HOST_PASSWORD= os.environ['HOST_PASSWORD']
