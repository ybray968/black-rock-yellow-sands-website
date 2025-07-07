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

def add_deck_thickness_spec():
    """Add thickness specification for Plywood Deck based on slide"""
    
    print("Adding thickness specification for Plywood Deck...")
    
    # Find the Deck product
    try:
        deck_product = Product.objects.get(name__icontains="Deck")
        print(f"Found product: {deck_product.name}")
    except Product.DoesNotExist:
        print("Deck product not found")
        return
    except Product.MultipleObjectsReturned:
        deck_product = Product.objects.filter(name__icontains="Deck").first()
        print(f"Found multiple products, using: {deck_product.name}")
    
    # Check if thickness specification already exists
    thickness_spec = deck_product.specifications.filter(name__icontains='thickness').first()
    if thickness_spec:
        print(f"Thickness specification already exists: {thickness_spec.value}")
        # Update it with the correct value from slide
        old_value = thickness_spec.value
        thickness_spec.value = "6.5, 9, 12, 15, 16, 18, 19, 21, 24, 27, 30, 35, 40 mm"
        thickness_spec.save()
        print(f"Updated thickness specification from '{old_value}' to '{thickness_spec.value}'")
    else:
        # Create new thickness specification
        ProductSpecification.objects.create(
            product=deck_product,
            name='Thicknesses',
            value='6.5, 9, 12, 15, 16, 18, 19, 21, 24, 27, 30, 35, 40 mm'
        )
        print("✓ Added new thickness specification for Plywood Deck")
    
    # Also update the product thickness field to match
    old_thickness = deck_product.thickness
    deck_product.thickness = "6.5, 9, 12, 15, 16, 18, 19, 21, 24, 27, 30, 35, 40 mm"
    deck_product.save()
    print(f"Updated product thickness field from '{old_thickness}' to '{deck_product.thickness}'")
    
    print(f"\n✅ Plywood Deck thickness specification updated successfully!")
    
    # Show all specifications for the deck product
    print(f"\nAll specifications for {deck_product.name}:")
    for spec in deck_product.specifications.all():
        print(f"  - {spec.name}: {spec.value}")

if __name__ == '__main__':
    add_deck_thickness_spec()
