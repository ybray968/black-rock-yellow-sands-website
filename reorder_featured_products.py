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

def reorder_featured_products():
    """
    Reorder featured products according to specified order:
    1. Plywood Deck (top seller)
    2. Plywood Exterior Birch  
    3. Plywood Interior Birch
    4. Plywood Parquet
    5. Plywood Antislip MT
    6. Plywood Antislip HEX
    """
    
    # Define the desired order with product names and their priority
    product_order = [
        ("Plywood Deck", 1),
        ("Plywood Exterior Birch", 2), 
        ("Plywood Interior Birch", 3),
        ("Plywood Parquet", 4),
        ("Plywood Antislip MT", 5),
        ("Plywood Antislip HEX", 6),
    ]
    
    print("Reordering featured products...")
    
    # First, make sure all specified products are featured
    for product_name, order in product_order:
        try:
            product = Product.objects.get(name=product_name)
            product.featured = True
            product.save()
            print(f"✓ Set {product_name} as featured")
        except Product.DoesNotExist:
            print(f"✗ Product '{product_name}' not found")
            continue
    
    # Add ordering field if it doesn't exist (we'll use created_at for ordering)
    # Since Django models don't have a built-in ordering field, we'll modify created_at
    # to reflect the desired order
    
    from datetime import datetime, timedelta
    base_date = datetime.now()
    
    for product_name, order in reversed(product_order):  # Reverse to make first item most recent
        try:
            product = Product.objects.get(name=product_name)
            # Set created_at to control ordering (most recent first)
            product.created_at = base_date + timedelta(minutes=order)
            product.save()
            print(f"✓ Set order {order} for {product_name}")
        except Product.DoesNotExist:
            print(f"✗ Product '{product_name}' not found")
            continue
    
    print("\n" + "="*50)
    print("Featured Products Order Updated Successfully!")
    print("="*50)
    
    # Display current featured products in order
    featured_products = Product.objects.filter(featured=True).order_by('-created_at')
    print("\nCurrent Featured Products Order:")
    for i, product in enumerate(featured_products, 1):
        print(f"{i}. {product.name}")
    
    print(f"\nTotal featured products: {featured_products.count()}")

if __name__ == '__main__':
    reorder_featured_products()
