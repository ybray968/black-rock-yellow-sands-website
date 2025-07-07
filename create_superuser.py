import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from django.contrib.auth.models import User

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'almuaddib1337@gmail.com', 'BUHu8ho&6et&h73_mNTTG*18D$jwe47Y@9z1')
    print("Superuser created successfully!")
else:
    print("Superuser already exists!")
