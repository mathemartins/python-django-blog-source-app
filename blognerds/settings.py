"""
Django settings for blognerds project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#=$3j43$c-w388r-e5z!v8$kz(j+thhx&u**w@o+1$e_hgp=13'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.primenerds.com']

AUTH_USER_MODEL = 'accounts.MyUser'

FULL_DOMAIN_NAME = 'http://www.primenerds.com'

LOGIN_URL = "/login/"

RECENT_COMMENT_NUMBER = 10


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #user custom apps
    'comments',
    'posts',
    'newsletter',
    'videos',
    'questions',
    'accounts',
    'notifications',
    'analytics',

    #third-party apps from github
    'django_filters',
    'crispy_forms',
    'markdown_deux',
    'pagedown',
    'dashing',
]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#TEMPLATE_CONTEXT_PROCESSORS = [
#    "django.contrib.auth.context_processors.auth",
#    "django.template.context_processors.debug",
#    "django.template.context_processors.i18n",
#    "django.template.context_processors.media",
#    "django.template.context_processors.request",
#    "django.template.context_processors.static",
#    "django.template.context_processors.tz",
#    "django.contrib.messages.context_processors.messages"
#]

ROOT_URLCONF = 'blognerds.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = 'blognerds.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'primenerds_db.sqlite3'),
    }
}
# settings.py
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'OPTIONS': {
#            'read_default_file': '/path/to/my.cnf',
#        },
#    }
#}


# my.cnf
#[client]
#database = NAME
#user = USER
#password = PASSWORD
#default-character-set = utf8


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    #'var/www/static/',
]

STATIC_ROOT = os.path.join( os.path.dirname (BASE_DIR), "static_cdn")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join( os.path.dirname (BASE_DIR), "media_cdn")
