#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product, Category, ProductSpecification

def delete_old_parquet():
    """Delete existing Plywood Parquet product and Parquet category"""
    
    print("Deleting old Plywood Parquet product and Parquet category...")
    
    # Delete Plywood Parquet product if it exists
    try:
        parquet_product = Product.objects.get(name='Plywood Parquet')
        print(f"Found product: {parquet_product.name} in category: {parquet_product.category.name}")
        
        # Delete all specifications first
        specs = ProductSpecification.objects.filter(product=parquet_product)
        specs_count = specs.count()
        specs.delete()
        print(f"Deleted {specs_count} product specifications")
        
        # Delete the product
        parquet_product.delete()
        print("✓ Deleted Plywood Parquet product")
        
    except Product.DoesNotExist:
        print("No Plywood Parquet product found to delete")
    
    # Delete Parquet category if it exists and has no other products
    try:
        parquet_category = Category.objects.get(slug='parquet')
        remaining_products = Product.objects.filter(category=parquet_category).count()
        
        if remaining_products == 0:
            parquet_category.delete()
            print("✓ Deleted empty Parquet category")
        else:
            print(f"Parquet category has {remaining_products} remaining products, not deleting")
            
    except Category.DoesNotExist:
        print("No Parquet category found to delete")
    
    print("\n✅ Cleanup completed!")
    print("Now you can create a fresh Plywood Parquet product in the Plywood category")

if __name__ == '__main__':
    delete_old_parquet()
