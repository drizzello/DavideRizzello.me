# DavideRizzello.me - Personal Website

A Django-based personal website with production-ready deployment configuration using Gunicorn and Caddy.

## 🚀 Features

### Core Application
- **Article Management**: Simple blog/article system with Django admin interface
- **Homepage**: Dynamic homepage displaying article count and current year
- **Admin Interface**: Full Django admin with custom Article admin configuration
- **Responsive Design**: Clean, modern CSS styling with mobile-friendly layout

### Technical Features
- **Environment-based Configuration**: Separate settings for development and production with custom .env file support
- **Database Flexibility**: SQLite for development, PostgreSQL for production
- **Static File Management**: WhiteNoise for efficient static file serving in production
- **Security**: Production-ready security settings with SSL/HTTPS enforcement, HSTS headers, and secure cookies
- **Process Management**: Automated service management with Makefile commands
- **Environment File Validation**: Automatic .env file detection and validation
- **Django Check Commands**: Built-in deployment and configuration validation

## 🛠️ Tech Stack

- **Backend**: Django 5.2.5
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **WSGI Server**: Gunicorn
- **Reverse Proxy**: Caddy
- **Static Files**: WhiteNoise
- **Configuration**: python-decouple
- **Process Management**: Makefile

## 📁 Project Structure

```
personal_website/
├── core/                           # Main Django app
│   ├── models.py                   # Article model
│   ├── views.py                    # Home view
│   ├── urls.py                     # App URL patterns
│   ├── admin.py                    # Admin configuration
│   └── migrations/                 # Database migrations
├── personal_website/               # Django project settings
│   ├── settings/
│   │   ├── base.py                 # Base settings
│   │   ├── dev.py                  # Development settings
│   │   └── prod.py                 # Production settings
│   ├── urls.py                     # Main URL configuration
│   ├── wsgi.py                     # WSGI configuration
│   └── asgi.py                     # ASGI configuration
├── templates/                      # HTML templates
│   ├── base.html                   # Base template
│   └── home.html                   # Homepage template
├── static/                         # Static files
│   └── css/
│       └── style.css               # Custom styles
├── staticfiles/                    # Collected static files (prod)
├── Caddyfile.dev                   # Caddy config for development
├── Caddyfile.prod                  # Caddy config for production
├── gunicorn.dev.conf.py            # Gunicorn config for development
├── gunicorn.prod.conf.py           # Gunicorn config for production
├── Makefile                        # Service management commands
└── manage.py                       # Django management script
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip
- Caddy (for reverse proxy)
- PostgreSQL (for production)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd DavideRizzello.me
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**
   
   Create environment files in the `personal_website/` directory:
   
   **Development** (`.env.dev`):
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost
   DATABASE_URL=sqlite:///db.sqlite3
   ```
   
   **Production** (`.env.prod`):
   ```env
   SECRET_KEY=your-production-secret-key
   DEBUG=False
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   DATABASE_URL=postgresql://user:password@localhost/dbname
   ```

4. **Database Setup**
   
   **Development:**
   ```bash
   cd personal_website
   make migrate-dev
   make createsuperuser-dev
   ```
   
   **Production:**
   ```bash
   cd personal_website
   make migrate-prod
   make createsuperuser-prod
   ```

## 🏃‍♂️ Development

### Start Development Server

```bash
cd personal_website
make up-dev
```

This will:
- Start Gunicorn with development settings
- Start Caddy reverse proxy
- Serve the site at `https://localhost`

### Stop Development Server

```bash
make down-dev
```

### Development Features

- **Auto-reload**: Code changes automatically restart the server
- **Debug Mode**: Full Django debug information
- **Console Email**: Email output to console for testing
- **SQLite Database**: Lightweight database for development

## 🚀 Production Deployment

### Production Environment Setup

1. **Environment Variables**
   
   Create `.env.prod` file with production settings (see installation section above).

2. **Database Migration and Static Files**
   ```bash
   make migrate-prod
   make collectstatic-prod
   ```

3. **Configuration Validation**
   ```bash
   make check-prod
   ```

4. **Start Production Services**
   ```bash
   make up-prod
   ```

### Production Features

- **Security Hardening**: SSL redirect, secure cookies, CSRF protection, HSTS headers
- **Optimized Static Files**: Compressed and cached static files
- **Process Management**: Multiple Gunicorn workers for performance
- **Reverse Proxy**: Caddy handles SSL termination and static file serving
- **Database**: PostgreSQL for production reliability
- **Environment Validation**: Automatic .env file detection and validation
- **Deployment Checks**: Built-in Django deployment validation

### Production Configuration

The production setup includes:

- **Gunicorn**: Multi-worker WSGI server with CPU-optimized worker count
- **Caddy**: Automatic HTTPS, static file serving, reverse proxy
- **WhiteNoise**: Efficient static file serving with compression
- **Security**: SSL enforcement, secure cookies, CSRF protection

## 📊 Database Models

### Article Model
- `title`: CharField (max 200 characters)
- `content`: TextField for article content
- `created_at`: DateTimeField (auto-generated)

### Admin Interface
- Custom Article admin with:
  - List display showing title and creation date
  - Search functionality for title and content
  - Chronological ordering (newest first)

## 🎨 Frontend

### Templates
- **Base Template**: Common layout with header, main content, and footer
- **Home Template**: Dynamic homepage with article count and year display

### Styling
- Clean, modern CSS design
- Responsive layout
- Professional color scheme
- Mobile-friendly design

## 🔧 Configuration

### Settings Structure
- **Base Settings**: Common configuration with environment file validation
- **Development**: Debug mode, console email, SQLite, `.env.dev` support
- **Production**: Security hardening, PostgreSQL, optimized static files, `.env.prod` support

### Environment Variables
- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode flag
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DATABASE_URL`: Database connection string
- `ENV_FILE`: Custom environment file path (defaults to `.env`)

### Environment File Management
- **Automatic Detection**: Base settings automatically detect and validate .env files
- **Custom Paths**: Support for custom environment file locations via `ENV_FILE` variable
- **Validation**: File existence validation with helpful error messages
- **Separate Files**: Support for `.env.dev` and `.env.prod` files

## 📝 Available Commands

### Makefile Commands

| Command | Description |
|---------|-------------|
| `make up-dev` | Start development environment with .env.dev |
| `make migrate-dev` | Run database migrations for development |
| `make createsuperuser-dev` | Create admin user for development |
| `make collectstatic-dev` | Collect static files for development |
| `make check-dev` | Validate development configuration |
| `make up-prod` | Start production environment with .env.prod |
| `make migrate-prod` | Run database migrations for production |
| `make createsuperuser-prod` | Create admin user for production |
| `make collectstatic-prod` | Collect static files for production |
| `make check-prod` | Validate production configuration and deployment |
| `make debug-prod` | Debug environment file detection for production |

### Django Commands

| Command | Description |
|---------|-------------|
| `python manage.py runserver` | Django development server |
| `python manage.py migrate` | Apply database migrations |
| `python manage.py collectstatic` | Collect static files |
| `python manage.py createsuperuser` | Create admin user |

## 🔒 Security Features

### Production Security
- SSL/HTTPS enforcement
- Secure session cookies
- CSRF protection
- Secure cookie settings
- HSTS headers (1 year, include subdomains, preload)
- Environment-based secret key management
- Environment file validation

### Development Security
- Debug mode for development
- Localhost-only access
- Console email backend
- Environment file validation

## 📦 Dependencies

### Core Dependencies
- `Django==5.2.5` - Web framework
- `gunicorn==23.0.0` - WSGI server
- `whitenoise==6.9.0` - Static file serving
- `psycopg2-binary==2.9.10` - PostgreSQL adapter
- `python-decouple==3.8` - Environment variable management
- `dj-database-url==3.0.1` - Database URL parsing

## 🌐 Deployment Notes

### Caddy Configuration
- **Development**: Simple reverse proxy to localhost:8000
- **Production**: Domain configuration with static file handling

### Gunicorn Configuration
- **Development**: 3 workers, auto-reload enabled
- **Production**: CPU-optimized worker count, timeout settings

### Static Files
- Development: Served by Django
- Production: Served by Caddy with WhiteNoise fallback

## 📈 Performance

### Production Optimizations
- Multiple Gunicorn workers
- Static file compression and caching
- Database connection pooling
- Optimized static file serving

### Monitoring
- Process management via PID files
- Service status tracking
- Error logging through Gunicorn

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is for personal use. Please respect the code and configuration.

---

**Built with ❤️ using Django, Gunicorn, and Caddy**
