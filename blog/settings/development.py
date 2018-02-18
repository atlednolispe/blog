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


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates', THEME),
            os.path.join(SITE_PACKAGES, 'django/contrib/admin/templates'),
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
]
