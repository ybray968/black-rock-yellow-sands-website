#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product

def fix_product_names():
    print("Fixing product names...")
    
    # Fix Interior Birch description
    try:
        p = Product.objects.get(name='Plywood Interior Birch')
        print(f"Found Interior Birch product: {p.name}")
        print(f"Current description: {p.description[:100]}...")
        
        # Fix the description
        p.description = p.description.replace('Plywood "Birch Interior"', 'Plywood Interior Birch')
        p.save()
        print("✅ Fixed Interior Birch description")
        print(f"New description: {p.description[:100]}...")
        
    except Product.DoesNotExist:
        print("❌ Interior Birch product not found")
    
    print("\n" + "="*50)
    print("Current product list:")
    for product in Product.objects.all().order_by('name'):
        print(f"- {product.name} (slug: {product.slug})")

if __name__ == '__main__':
    fix_product_names()
