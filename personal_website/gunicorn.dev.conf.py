import os

# Settings di sviluppo
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_website.settings.dev")

bind = "127.0.0.1:8000"
workers = 3
reload = True  # Ricarica automatica in dev
