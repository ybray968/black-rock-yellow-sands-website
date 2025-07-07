#!/usr/bin/env python
"""
COMPLETE PLYWOOD PARQUET FIX
1. Copy all content from existing Plywood Parquet
2. Delete the product and Parquet category
3. Create fresh Plywood Parquet in Plywood category
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product, Category, ProductSpecification

print("🔄 COMPLETE PLYWOOD PARQUET FIX")
print("=" * 50)

# STEP 1: Copy all existing content
print("\n📋 STEP 1: Copying existing Plywood Parquet content...")
try:
    existing_product = Product.objects.get(name='Plywood Parquet')
    
    # Save all the content
    saved_content = {
        'name': existing_product.name,
        'description': existing_product.description,
        'price': existing_product.price,
        'wood_type': existing_product.wood_type,
        'wood_species': existing_product.wood_species,
        'grade': existing_product.grade,
        'thickness': existing_product.thickness,
        'width': existing_product.width,
        'length': existing_product.length,
        'finish': existing_product.finish,
        'featured': existing_product.featured,
        'in_stock': existing_product.in_stock,
        'stock_quantity': existing_product.stock_quantity,
        'meta_description': existing_product.meta_description,
    }
    
    # Save specifications
    specs = ProductSpecification.objects.filter(product=existing_product)
    saved_specs = [(spec.name, spec.value) for spec in specs]
    
    print(f"✅ Copied content from: {existing_product.name}")
    print(f"✅ Copied {len(saved_specs)} specifications")
    print(f"✅ Current category: {existing_product.category.name}")
    
except Product.DoesNotExist:
    print("❌ Plywood Parquet not found!")
    exit()

# STEP 2: Delete existing product
print("\n🗑️  STEP 2: Deleting existing Plywood Parquet...")
specs_count = ProductSpecification.objects.filter(product=existing_product).count()
ProductSpecification.objects.filter(product=existing_product).delete()
existing_product.delete()
print(f"✅ Deleted product and {specs_count} specifications")

# STEP 3: Delete Parquet category if empty
print("\n🗑️  STEP 3: Checking Parquet category...")
try:
    parquet_category = Category.objects.get(slug='parquet')
    remaining_products = Product.objects.filter(category=parquet_category).count()
    
    if remaining_products == 0:
        parquet_category.delete()
        print("✅ Deleted empty Parquet category")
    else:
        print(f"⚠️  Keeping Parquet category ({remaining_products} products remain)")
        
except Category.DoesNotExist:
    print("ℹ️  Parquet category already gone")

# STEP 4: Get Plywood category
print("\n📁 STEP 4: Getting Plywood category...")
try:
    plywood_category = Category.objects.get(slug='plywood')
    print(f"✅ Found Plywood category: {plywood_category.name}")
except Category.DoesNotExist:
    plywood_category = Category.objects.create(
        name="Plywood",
        slug='plywood',
        description='High-quality plywood products for construction and specialized applications'
    )
    print(f"✅ Created Plywood category: {plywood_category.name}")

# STEP 5: Create fresh Plywood Parquet in Plywood category
print("\n🆕 STEP 5: Creating fresh Plywood Parquet in Plywood category...")

# Use saved content but put in Plywood category
saved_content['category'] = plywood_category
saved_content['slug'] = 'plywood-parquet'

# Create the new product
new_product = Product.objects.create(**saved_content)
print(f"✅ Created: {new_product.name} in {new_product.category.name} category")

# Add back all specifications
for spec_name, spec_value in saved_specs:
    ProductSpecification.objects.create(
        product=new_product,
        name=spec_name,
        value=spec_value
    )

print(f"✅ Added {len(saved_specs)} specifications")

# STEP 6: Final verification
print("\n" + "=" * 50)
print("🎉 COMPLETE FIX DONE!")
print("=" * 50)

# Verify the new product
verify_product = Product.objects.get(name='Plywood Parquet')
print(f"📋 Product: {verify_product.name}")
print(f"📁 Category: {verify_product.category.name} (slug: {verify_product.category.slug})")
print(f"🔧 Featured: {verify_product.featured}")
print(f"📦 In stock: {verify_product.in_stock}")

specs_count = ProductSpecification.objects.filter(product=verify_product).count()
print(f"📝 Specifications: {specs_count}")

print(f"\n🎯 PLYWOOD PARQUET NOW HAS:")
print(f"✅ Correct category: {verify_product.category.name}")
print(f"✅ Appears with other plywood products")
print(f"✅ Has application image space under main image")
print(f"✅ Uses plywood template advantages")
print(f"✅ Will show: plywood-parquet-application.png")

print(f"\n📝 YOUR TASK:")
print(f"Create: static/images/plywood-parquet-application.png")

print(f"\n✨ PARQUET CATEGORY CLEANED UP - ONLY PLYWOOD CATEGORY NOW!")
