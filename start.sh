#!/bin/bash

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Start gunicorn
echo "Starting gunicorn..."
exec gunicorn construction_site.wsgi:application --bind 0.0.0.0:$PORT
