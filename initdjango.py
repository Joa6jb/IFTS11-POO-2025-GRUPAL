import os
import django

def init_django(app):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', app)
    django.setup()