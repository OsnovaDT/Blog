"""ASGI of the project"""

from os import environ

from django.core.asgi import get_asgi_application


environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

application = get_asgi_application()
