# -*- coding: utf-8 -*-
# Django settings for os2online project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('V. Sergeyev', 'vova.sergeyev@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    #     'NAME': 'os2online',                      # Or path to database file if using sqlite3.
    #     'USER': 'root',                      # Not used with sqlite3.
    #     'PASSWORD': 'rootwdp',                  # Not used with sqlite3.
    #     'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
    #     'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    # }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'npsl*xea%5&_*f-h1&r!r&l)c_%s9*#a*us@)gdhedr!$f3i%b'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'os2online.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.sites',
    # 'django.contrib.admin',
    # 'django.contrib.flatpages',
    'os2online.desktop',
)

APPEND_SLASH = True

try:
    from local_settings import *
except:
    pass