"""
Production Security Settings
These settings should be used when deploying to production.
Copy these to your settings.py and adjust as needed.
"""

# ==== PRODUCTION SECURITY SETTINGS ====
# Use these settings when deploying to production

# SECURITY WARNING: Change this secret key in production!
# Generate a new one using: python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
SECRET_KEY = 'CHANGE-THIS-IN-PRODUCTION'

# SECURITY WARNING: Never set DEBUG = True in production!
DEBUG = False

# Add your production domain(s)
ALLOWED_HOSTS = [
    'yourdomain.com',
    'www.yourdomain.com',
    # Add your production IP address if needed
]

# ===== HTTPS & SSL SETTINGS =====
# Force HTTPS in production
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Secure cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# ===== DATABASE SECURITY =====
# Use environment variables for database credentials
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Use PostgreSQL in production
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
        'OPTIONS': {
            'sslmode': 'require',  # Require SSL for database connections
        },
    }
}

# ===== ADMIN SECURITY =====
# Restrict admin access to specific IP addresses
ADMIN_ALLOWED_IPS = [
    '192.168.1.100',  # Your office IP
    '10.0.0.50',      # Your VPN IP
    # Add more IPs as needed
]

# Change admin URL to something non-obvious
ADMIN_URL = 'secure-admin-panel/'  # Change this in your URLs

# ===== FILE UPLOAD SECURITY =====
# Allowed file extensions for uploads
ALLOWED_FILE_EXTENSIONS = [
    '.jpg', '.jpeg', '.png', '.gif', '.pdf', '.doc', '.docx', '.xls', '.xlsx'
]

# Maximum file sizes (in bytes)
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440  # 2.5MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440  # 2.5MB
DATA_UPLOAD_MAX_NUMBER_FIELDS = 50

# ===== STATIC FILES SECURITY =====
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# ===== LOGGING CONFIGURATION =====
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'security_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/django/security.log',
            'maxBytes': 1024*1024*10,  # 10MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/django/error.log',
            'maxBytes': 1024*1024*10,  # 10MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django.security': {
            'handlers': ['security_file', 'console'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['error_file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'security_middleware': {
            'handlers': ['security_file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}

# ===== EMAIL SECURITY =====
# Use SMTP with TLS for email sending
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

# ===== CACHE SECURITY =====
# Use Redis for caching in production
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379/1'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'KEY_PREFIX': 'construction_site',
    }
}

# ===== ADDITIONAL SECURITY HEADERS =====
# Content Security Policy
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'", "https://cdn.jsdelivr.net", "https://cdnjs.cloudflare.com")
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", "https://cdn.jsdelivr.net", "https://fonts.googleapis.com")
CSP_FONT_SRC = ("'self'", "https://fonts.gstatic.com")
CSP_IMG_SRC = ("'self'", "data:")
CSP_CONNECT_SRC = ("'self'",)
CSP_FRAME_ANCESTORS = ("'none'",)

# ===== BACKUP SETTINGS =====
# Regular database backups
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': '/backups/'}

# ===== MONITORING =====
# Add monitoring service configuration
# SENTRY_DSN = os.environ.get('SENTRY_DSN')

# ===== RATE LIMITING =====
# Configure rate limiting for production
RATELIMIT_ENABLE = True
RATELIMIT_USE_CACHE = 'default'

# ===== ENVIRONMENT VARIABLES TEMPLATE =====
"""
Create a .env file with these variables for production:

# Database
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_strong_database_password
DB_HOST=your_database_host
DB_PORT=5432

# Email
EMAIL_HOST=smtp.your-email-provider.com
EMAIL_HOST_USER=your_email@domain.com
EMAIL_HOST_PASSWORD=your_email_password
DEFAULT_FROM_EMAIL=noreply@yourdomain.com

# Security
SECRET_KEY=your_generated_secret_key_here

# Optional
REDIS_URL=redis://localhost:6379/1
SENTRY_DSN=your_sentry_dsn_if_using_sentry
"""
