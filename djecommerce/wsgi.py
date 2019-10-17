import os
import sys

sys.path.append(' /var/www/djecommerce')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djecommerce.settings')

application = get_wsgi_application()
