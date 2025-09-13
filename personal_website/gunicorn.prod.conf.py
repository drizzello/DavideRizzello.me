import os
import multiprocessing

# Legge la variabile ENV (default: dev)
env = os.getenv("ENV", "dev")

if env == "prod":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_website.settings.prod")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_website.settings.dev")

bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1  # Formula consigliata
reload = env != "prod"  # In dev autoreload, in prod no
timeout = 120
