"""
WSGI config for simple_dj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv

load_dotenv(verbose=True, override=True)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_dj.settings.base')

application = get_wsgi_application()
