web: python manage.py collectstatic --noinput && python manage.py migrate && gunicorn construction_site.wsgi:application --bind 0.0.0.0:$PORT --timeout 120 --workers 2
