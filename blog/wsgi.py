"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


try:
    import mysqlclient
except ModuleNotFoundError:
    import pymysql
    pymysql.install_as_MySQLdb()

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
profile = os.environ.get('BLOG_PROFILE', 'product')
os.environ.update({"DJANGO_SETTINGS_MODULE": "blog.settings.%s" % profile})

application = get_wsgi_application()
