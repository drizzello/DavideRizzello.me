### 🔹 Dev environment ###
up-dev:
	@echo "🚀 Starting Gunicorn (dev) + Caddy..."
	@ENV_FILE=.env.dev gunicorn -c gunicorn.dev.conf.py personal_website.wsgi:application & echo $$! > gunicorn-dev.pid
	@ENV_FILE=.env.dev caddy run --config Caddyfile.dev & echo $$! > caddy-dev.pid
	@echo "✅ Dev services running: visit https://localhost"

down-dev:
	@echo "🛑 Stopping Gunicorn + Caddy (dev)..."
	@kill -9 `cat gunicorn-dev.pid` || true
	@kill -9 `cat caddy-dev.pid` || true
	@rm -f gunicorn-dev.pid caddy-dev.pid
	@echo "✅ Dev services stopped."

migrate-dev:
	ENV_FILE=.env.dev python manage.py migrate --settings=personal_website.settings.dev

createsuperuser-dev:
	ENV_FILE=.env.dev python manage.py createsuperuser --settings=personal_website.settings.dev

collectstatic-dev:
	ENV_FILE=.env.dev python manage.py collectstatic --settings=personal_website.settings.dev --noinput


### 🔹 Prod environment ###
up-prod:
	@echo "🚀 Starting Gunicorn (prod) + Caddy..."
	@ENV_FILE=.env.prod gunicorn -c gunicorn.prod.conf.py personal_website.wsgi:application & echo $$! > gunicorn-prod.pid
	@ENV_FILE=.env.prod caddy run --config Caddyfile.prod & echo $$! > caddy-prod.pid
	@echo "✅ Prod services running: visit https://yourdomain.com"

migrate-prod:
	ENV_FILE=.env.prod python manage.py migrate --settings=personal_website.settings.prod

createsuperuser-prod:
	ENV_FILE=.env.prod python manage.py createsuperuser --settings=personal_website.settings.prod

collectstatic-prod:
	ENV_FILE=.env.prod python manage.py collectstatic --settings=personal_website.settings.prod --noinput

check-prod:
	ENV_FILE=.env.prod python manage.py check --deploy --settings=personal_website.settings.prod

check-dev:
	ENV_FILE=.env.dev python manage.py check --settings=personal_website.settings.dev

### 🔹 Debug ENV ###
debug-prod:
	ENV_FILE=.env.prod python -c "import os; from pathlib import Path; BASE_DIR = Path.cwd(); ENV_FILE = os.getenv('ENV_FILE', '.env'); ENV_PATH = (BASE_DIR / ENV_FILE).resolve(); print(f'ENV_FILE={ENV_FILE}'); print(f'ENV_PATH={ENV_PATH}'); print(f'File exists? {ENV_PATH.exists()}')"
