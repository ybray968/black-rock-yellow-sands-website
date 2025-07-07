#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product, Category

def fix_plywood_parquet_category():
    """Move Plywood Parquet from Parquet category to Plywood category"""
    
    print("Fixing Plywood Parquet category...")
    
    try:
        # Find the Plywood Parquet product
        parquet_product = Product.objects.get(name='Plywood Parquet')
        print(f"Found product: {parquet_product.name}")
        print(f"Current category: {parquet_product.category.name}")
        
        # Get the Plywood category
        plywood_category = Category.objects.get(slug='plywood')
        print(f"Target category: {plywood_category.name}")
        
        # Update the product's category
        parquet_product.category = plywood_category
        parquet_product.save()
        
        print(f"✅ Successfully moved '{parquet_product.name}' to '{plywood_category.name}' category")
        
        # Verify the change
        updated_product = Product.objects.get(name='Plywood Parquet')
        print(f"Verification: Product is now in '{updated_product.category.name}' category")
        
    except Product.DoesNotExist:
        print("❌ Plywood Parquet product not found")
        print("You may need to run the add_plywood_parquet.py script first")
        
    except Category.DoesNotExist:
        print("❌ Plywood category not found")
        print("Please ensure the Plywood category exists")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    fix_plywood_parquet_category()
