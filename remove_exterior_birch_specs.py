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

def remove_exterior_birch_specs():
    """Remove specific specifications from Plywood Exterior Birch product"""
    
    print("Removing specific specifications from Plywood Exterior Birch...")
    
    # Find the Exterior Birch product
    try:
        exterior_birch = Product.objects.get(name__icontains="Exterior Birch")
        print(f"Found product: {exterior_birch.name}")
    except Product.DoesNotExist:
        print("Exterior Birch product not found")
        return
    except Product.MultipleObjectsReturned:
        # Get the first one if multiple exist
        exterior_birch = Product.objects.filter(name__icontains="Exterior Birch").first()
        print(f"Found multiple products, using: {exterior_birch.name}")
    
    # List of specification names to remove
    specs_to_remove = [
        'CARB status',
        'ULEF (Ultra Low Emitting Formaldehyde)',
        'Advantages',
        'Excellent bonding properties, Resistance to moisture impact, Wide range of thicknesses and sizes, Exceptional durability, Easy to use and process'
    ]
    
    removed_count = 0
    
    for spec_name in specs_to_remove:
        # Try exact match first
        specs = ProductSpecification.objects.filter(product=exterior_birch, name=spec_name)
        if specs.exists():
            count = specs.count()
            print(f"Removing {count} specification(s) with exact name: '{spec_name}'")
            specs.delete()
            removed_count += count
        else:
            # Try partial match
            specs = ProductSpecification.objects.filter(product=exterior_birch, name__icontains=spec_name)
            if specs.exists():
                count = specs.count()
                print(f"Removing {count} specification(s) containing: '{spec_name}'")
                for spec in specs:
                    print(f"  - Removing: {spec.name}")
                specs.delete()
                removed_count += count
    
    # Also remove any remaining advantage-related specs
    advantage_keywords = [
        'bonding',
        'durability',
        'process',
        'advantage',
        'easy to use'
    ]
    
    for keyword in advantage_keywords:
        specs = ProductSpecification.objects.filter(
            product=exterior_birch, 
            name__icontains=keyword
        )
        if specs.exists():
            count = specs.count()
            print(f"Removing {count} specification(s) containing keyword '{keyword}':")
            for spec in specs:
                print(f"  - Removing: {spec.name}")
            specs.delete()
            removed_count += count
    
    print(f"\n✅ Total removed: {removed_count} specifications from {exterior_birch.name}")
    
    # Show remaining specifications
    remaining_specs = ProductSpecification.objects.filter(product=exterior_birch)
    print(f"\nRemaining specifications ({remaining_specs.count()}):")
    for spec in remaining_specs:
        print(f"  - {spec.name}: {spec.value}")

if __name__ == '__main__':
    remove_exterior_birch_specs()
