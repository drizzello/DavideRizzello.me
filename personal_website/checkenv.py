import os
from pathlib import Path
from decouple import Config, RepositoryEnv, Csv

# Path base del progetto
BASE_DIR = Path(__file__).resolve().parent

# Prende ENV_FILE da variabile d'ambiente, default .env
ENV_FILE = os.getenv("ENV_FILE", ".env")
ENV_PATH = BASE_DIR / ENV_FILE

print(f"🔍 Usando ENV_FILE={ENV_FILE}")
print(f"📂 Path risolto={ENV_PATH}")

# Carica le variabili
config = Config(RepositoryEnv(ENV_PATH))

try:
    secret_key = config("SECRET_KEY")
    debug = config("DEBUG", default=False, cast=bool)
    allowed_hosts = config("ALLOWED_HOSTS", default="127.0.0.1,localhost", cast=Csv())
except Exception as e:
    print("❌ Errore nel leggere l'env file:", e)
    exit(1)

print("✅ Variabili lette correttamente:")
print(f"   DEBUG = {debug}")
print(f"   SECRET_KEY (len) = {len(secret_key)}")
print(f"   ALLOWED_HOSTS = {allowed_hosts}")
