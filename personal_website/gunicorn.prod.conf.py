import os
import multiprocessing

# Settings di produzione
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_website.settings.prod")

bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1  # Formula consigliata
reload = False
timeout = 120
