import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from django.template.defaultfilters import slugify

products = [
    'Plywood Birch Exterior (WBP)',
    'Plywood Interior Birch', 
    'Plywood Deck (Construction Use)',
    'Plywood Shield',
    'Plywood Antislip HEX',
    'Plywood Deco',
    'Plywood Parquet',
    'Plywood Shield Acu',
    'Plywood Antislip MT'
]

print('Expected PNG application image names:')
for product in products:
    slugified = slugify(product.lower())
    print(f'{product} -> {slugified}-application.png')
