import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product

try:
    # Find the existing product with the old name
    product = Product.objects.get(name='Plywood Birch Exterior (WBP)')
    
    # Update the name and slug
    product.name = 'Plywood Exterior Birch (WBP)'
    product.slug = slugify('Plywood Exterior Birch WBP')
    
    # Update the description to replace "Plyterra Birch Exterior" with "Plywood Exterior Birch"
    product.description = product.description.replace('Plywood Birch Exterior', 'Plywood Exterior Birch')
    
    product.save()
    
    print('Product name and description updated successfully!')
    print(f'Old name: Plywood Birch Exterior (WBP)')
    print(f'New name: {product.name}')
    print(f'Description updated: {product.description[:100]}...')
    
except Product.DoesNotExist:
    print('Product "Plywood Birch Exterior (WBP)" not found.')
    print('Please check if the product exists in the database.')
