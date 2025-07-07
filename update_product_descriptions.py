import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product

# Update Plywood Exterior Birch description
try:
    exterior_product = Product.objects.get(name='Plywood Exterior Birch (WBP)')
    
    # Replace "Birch Exterior" with "Exterior Birch" in description
    exterior_product.description = exterior_product.description.replace('"Birch Exterior"', '"Exterior Birch"')
    exterior_product.save()
    
    print('Exterior Birch product description updated successfully!')
    print(f'Updated description preview: {exterior_product.description[:100]}...')
    
except Product.DoesNotExist:
    print('Plywood Exterior Birch (WBP) product not found.')

# Update Plywood Interior Birch description
try:
    interior_product = Product.objects.get(name='Plywood Interior Birch')
    
    # Replace "Birch Interior" with "Interior Birch" in description
    interior_product.description = interior_product.description.replace('"Birch Interior"', '"Interior Birch"')
    interior_product.save()
    
    print('Interior Birch product description updated successfully!')
    print(f'Updated description preview: {interior_product.description[:100]}...')
    
except Product.DoesNotExist:
    print('Plywood Interior Birch product not found.')

print('All product descriptions updated successfully!')
