import os
from .settings import *

# Production settings
DEBUG = False
ALLOWED_HOSTS = ['*']

# Database configuration for Railway PostgreSQL
if os.environ.get('DATABASE_URL'):
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
elif all(os.environ.get(key) for key in ['PGDATABASE', 'PGUSER', 'PGPASSWORD', 'PGHOST', 'PGPORT']):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('PGDATABASE'),
            'USER': os.environ.get('PGUSER'),
            'PASSWORD': os.environ.get('PGPASSWORD'),
            'HOST': os.environ.get('PGHOST'),
            'PORT': os.environ.get('PGPORT', '5432'),
        }
    }
else:
    # Fallback to SQLite for local development
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# WhiteNoise for serving static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# CSRF settings for Railway and other hosting platforms
CSRF_TRUSTED_ORIGINS = [
    'https://*.railway.app',
    'https://*.up.railway.app',
    'https://*.render.com',
    'https://*.vercel.app',
    'https://*.herokuapp.com',
    'https://*.pythonanywhere.com',
    'https://*.netlify.app',
    'https://*.onrender.com',
    'https://*.fly.dev',
    'https://*.digitalocean.app',
    'https://www.braysint.com',
    'https://braysint.com',
    'http://www.braysint.com',  # In case HTTP is used
    'http://braysint.com',
]

# CSRF Protection - Production settings for HTTPS
CSRF_COOKIE_SECURE = True  # Your site uses HTTPS
CSRF_COOKIE_HTTPONLY = False  # Allow JS access for compatibility
CSRF_COOKIE_SAMESITE = 'Lax'  # Changed from Strict for language switching
CSRF_USE_SESSIONS = False  # Use cookies for better compatibility with hosting
CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'
CSRF_COOKIE_AGE = 3600  # 1 hour (shorter for security)

# Additional CSRF settings for compatibility
CSRF_COOKIE_NAME = 'csrftoken'
CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'

# Session settings for production
SESSION_COOKIE_SECURE = True  # Your site uses HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

# Static files storage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Logging already configured in base settings (console only)
# No additional logging configuration needed
