"""WSGI config of the project"""

from os import environ

from django.core.wsgi import get_wsgi_application


environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

application = get_wsgi_application()
