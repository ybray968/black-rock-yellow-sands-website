import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product
from django.template.defaultfilters import slugify

plywood_products = Product.objects.filter(category__slug='plywood')

print('Plywood products and their expected application image names:')
print('=' * 60)

for product in plywood_products:
    expected_image = f"{slugify(product.name.lower())}-application.png"
    print(f'Product: {product.name}')
    print(f'Expected image: {expected_image}')
    print('-' * 40)

print(f'\nTotal plywood products: {plywood_products.count()}')
