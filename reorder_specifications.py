#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product, ProductSpecification

def reorder_specifications():
    """Reorder specifications so thickness appears first for all products"""
    
    print("Reordering specifications to put thickness first...")
    
    # Get all products
    products = Product.objects.all()
    
    for product in products:
        print(f"\n--- Processing: {product.name} ---")
        
        # Get all specifications for this product
        all_specs = list(product.specifications.all())
        
        if not all_specs:
            print("No specifications found")
            continue
        
        # Find thickness specification
        thickness_spec = None
        other_specs = []
        
        for spec in all_specs:
            if 'thickness' in spec.name.lower():
                thickness_spec = spec
            else:
                other_specs.append(spec)
        
        if not thickness_spec:
            print("No thickness specification found")
            continue
        
        print(f"Found thickness spec: {thickness_spec.name}")
        print(f"Found {len(other_specs)} other specifications")
        
        # Delete all specifications
        product.specifications.all().delete()
        
        # Recreate specifications in correct order
        # 1. First, create thickness specification
        new_thickness_spec = ProductSpecification.objects.create(
            product=product,
            name=thickness_spec.name,
            value=thickness_spec.value
        )
        print(f"✓ Created thickness spec first: {new_thickness_spec.name}")
        
        # 2. Then create other specifications in their original order
        for spec in other_specs:
            ProductSpecification.objects.create(
                product=product,
                name=spec.name,
                value=spec.value
            )
        
        # Show final order
        final_specs = product.specifications.all().order_by('id')
        print(f"Final order for {product.name}:")
        for i, spec in enumerate(final_specs, 1):
            print(f"  {i}. {spec.name}: {spec.value[:40]}{'...' if len(spec.value) > 40 else ''}")

    print(f"\n✅ All specifications reordered - thickness now appears first!")

if __name__ == '__main__':
    reorder_specifications()
