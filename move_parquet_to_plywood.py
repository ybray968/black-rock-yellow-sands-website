#!/usr/bin/env python
"""
SIMPLE FIX: Move Plywood Parquet to Plywood category
NO OTHER PRODUCTS OR TEMPLATES TOUCHED
"""
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product, Category

print("🔧 MOVING PLYWOOD PARQUET TO PLYWOOD CATEGORY")
print("=" * 50)

try:
    # Find the Plywood Parquet product
    parquet = Product.objects.get(name='Plywood Parquet')
    print(f"Found: {parquet.name}")
    print(f"Current category: {parquet.category.name} (slug: {parquet.category.slug})")
    
    # Get the Plywood category
    plywood_cat = Category.objects.get(slug='plywood')
    print(f"Target category: {plywood_cat.name}")
    
    # Simply change the category
    parquet.category = plywood_cat
    parquet.save()
    
    print(f"✅ SUCCESS: Moved to {plywood_cat.name} category")
    
    # Verify
    check = Product.objects.get(name='Plywood Parquet')
    print(f"✅ VERIFIED: Now in {check.category.name} category")
    
    print("\n🎯 PLYWOOD PARQUET NOW HAS:")
    print("✅ Application image space under main image")
    print("✅ Plywood template advantages")
    print("✅ Appears with other plywood products")
    print("\n📝 CREATE: static/images/plywood-parquet-application.png")

except Product.DoesNotExist:
    print("❌ Plywood Parquet not found!")
except Category.DoesNotExist:
    print("❌ Plywood category not found!")
except Exception as e:
    print(f"❌ Error: {e}")

print("\n✅ DONE - NO OTHER PRODUCTS TOUCHED")
