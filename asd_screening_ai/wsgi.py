"""
WSGI config for asd_screening_ai project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asd_screening_ai.settings')

application = get_wsgi_application()
