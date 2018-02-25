import sys

import atlednolispe_settings  # private_password

from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': atlednolispe_settings.DATABASE_NAME,
        'USER': atlednolispe_settings.USER,
        'PASSWORD': atlednolispe_settings.PASSWORD,
        'HOST': atlednolispe_settings.HOST,
        'PORT': '3306',
    }
}

THEME_DIR = 'themes'
THEME_TYPE = 'html5up'
THEME = os.path.join(THEME_DIR, THEME_TYPE)

SITE_PACKAGES = [s_p for s_p in sys.path if s_p.endswith('site-packages')][0]

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

ALLOWED_HOSTS = [  # required if DEBUG = False
    '127.0.0.1',
]
