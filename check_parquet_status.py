#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product, Category

print("🔍 CHECKING PLYWOOD PARQUET STATUS")
print("=" * 40)

try:
    parquet = Product.objects.get(name='Plywood Parquet')
    print(f"✅ Found: {parquet.name}")
    print(f"📁 Category: {parquet.category.name}")
    print(f"🏷️  Category slug: {parquet.category.slug}")
    print(f"🔧 Featured: {parquet.featured}")
    print(f"📦 In stock: {parquet.in_stock}")
    
    if parquet.category.slug == 'plywood':
        print("\n🎉 SUCCESS: Plywood Parquet is in PLYWOOD category!")
        print("✅ Will appear with other plywood products")
        print("✅ Will have application image space")
        print("✅ Template will work correctly")
    else:
        print(f"\n❌ PROBLEM: Still in '{parquet.category.slug}' category")
        print("❌ Won't appear with plywood products")
        print("❌ No application image space")
        
except Product.DoesNotExist:
    print("❌ Plywood Parquet product not found!")

print("\n🔍 CHECKING ALL CATEGORIES:")
categories = Category.objects.all()
for cat in categories:
    count = Product.objects.filter(category=cat).count()
    print(f"📁 {cat.name} (slug: {cat.slug}) - {count} products")
