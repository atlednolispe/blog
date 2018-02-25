import sys

from .base import *


# make db document in top blog, or in the directory of settings
BASE_DIR = os.path.dirname(BASE_DIR)

DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

THEME_DIR = 'themes'
THEME_TYPE = 'html5up'
# THEME = THEME_DIR + '/' + THEME_TYPE
THEME = os.path.join(THEME_DIR, THEME_TYPE)

SITE_PACKAGES = [s_p for s_p in sys.path if s_p.endswith('site-packages')][0]

INSTALLED_APPS += [
    'debug_toolbar',
    'silk',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'silk.middleware.SilkyMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates', THEME),
            os.path.join(SITE_PACKAGES, 'xadmin/templates'),
            os.path.join(SITE_PACKAGES, 'crispy_forms/templates'),
            os.path.join(SITE_PACKAGES, 'reversion/templates'),
            os.path.join(SITE_PACKAGES, 'ckeditor/templates'),
            os.path.join(SITE_PACKAGES, 'ckeditor_uploader/templates'),
            os.path.join(SITE_PACKAGES, 'rest_framework/templates'),
            os.path.join(SITE_PACKAGES, 'debug_toolbar/templates'),
            os.path.join(SITE_PACKAGES, 'silk/templates'),
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

            'libraries': {
                'filters': 'templatetags.filters'
            }
        },
    },
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(SITE_PACKAGES, 'rest_framework/static'),
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/django_cache',
    }
}

CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {  # set the name of the config
        'toolbar': 'Full',
        'height': 300,
        # 'width': 1200,
        'tabSpaces': 4,
    },
}

DEFAULT_FILE_STORAGE = 'blog.storage.MyStorage'

SILKY_PYTHON_PROFILER = True
