#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product

def update_product_thickness():
    """Update products with proper thickness information based on their specifications"""
    
    print("Updating product thickness information...")
    
    # Get all products
    products = Product.objects.all()
    updated_count = 0
    
    for product in products:
        print(f"\nChecking product: {product.name}")
        print(f"Current thickness: {product.thickness}")
        
        # Find thickness specification
        thickness_spec = product.specifications.filter(name__icontains='thickness').first()
        if thickness_spec:
            print(f"Found thickness spec: {thickness_spec.value}")
            
            # Update the product thickness field
            old_thickness = product.thickness
            product.thickness = thickness_spec.value
            product.save()
            
            print(f"Updated thickness from '{old_thickness}' to '{product.thickness}'")
            updated_count += 1
        else:
            print("No thickness specification found")
            
            # For products without thickness spec, add proper thickness based on product type
            if 'Interior Birch' in product.name:
                product.thickness = '4, 6, 8, 9, 10, 11, 12, 14, 15, 17, 18, 20, 21, 24, 25, 30 mm'
                product.save()
                print(f"Added standard Interior Birch thickness: {product.thickness}")
                updated_count += 1
            elif 'Exterior Birch' in product.name:
                product.thickness = '6, 8, 9, 10, 12, 15, 18, 19, 21, 24, 25, 30 mm'
                product.save()
                print(f"Added standard Exterior Birch thickness: {product.thickness}")
                updated_count += 1
            elif 'Deck' in product.name:
                product.thickness = '15, 18, 21, 24, 27, 30 mm'
                product.save()
                print(f"Added standard Deck thickness: {product.thickness}")
                updated_count += 1
    
    print(f"\n✅ Updated {updated_count} products with thickness information")

if __name__ == '__main__':
    update_product_thickness()
