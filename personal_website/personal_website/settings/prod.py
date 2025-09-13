from .base import *
from decouple import Config, Csv,RepositoryEnv
import dj_database_url
import os

env_file = os.getenv("ENV_FILE", ".env")
config = Config(RepositoryEnv(env_file))
DEBUG = config("DEBUG", default=False, cast=bool)
SECRET_KEY = config("SECRET_KEY")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

DATABASES = {
    "default": dj_database_url.parse(config("DATABASE_URL"))
}

# Security
SECURE_HSTS_SECONDS = 31536000  # 1 anno
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

