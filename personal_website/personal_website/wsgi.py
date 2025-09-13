import os
from django.core.wsgi import get_wsgi_application

# Usa ENV=prod o ENV=dev (default: dev)
env = os.getenv("ENV", "dev")

if env == "prod":
    settings_module = "personal_website.settings.prod"
else:
    settings_module = "personal_website.settings.dev"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()
