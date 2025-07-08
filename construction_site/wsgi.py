"""
WSGI config for construction_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Use production settings if DJANGO_SETTINGS_MODULE is not set and we're on Railway
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    if os.environ.get('RAILWAY_ENVIRONMENT'):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings_production')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')

application = get_wsgi_application()
