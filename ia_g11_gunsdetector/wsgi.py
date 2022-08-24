import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ia_g11_gunsdetector.settings')

application = get_wsgi_application()
