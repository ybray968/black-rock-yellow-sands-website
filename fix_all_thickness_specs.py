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

def fix_all_thickness_specs():
    """Ensure all products have thickness specification as first line"""
    
    print("Fixing thickness specifications for all products...")
    
    # Get all products
    products = Product.objects.all()
    
    for product in products:
        print(f"\n--- Processing: {product.name} ---")
        
        # Check if thickness specification exists
        thickness_specs = product.specifications.filter(name__icontains='thickness')
        
        if thickness_specs.exists():
            # Delete existing thickness specifications to recreate them properly
            print(f"Found {thickness_specs.count()} existing thickness spec(s), removing them...")
            thickness_specs.delete()
        
        # Create thickness specification based on product thickness field
        if product.thickness:
            print(f"Product thickness field: {product.thickness}")
            
            # Create new thickness specification as first item
            ProductSpecification.objects.create(
                product=product,
                name='Thicknesses, mm',
                value=product.thickness
            )
            print(f"✓ Added thickness specification: {product.thickness}")
        else:
            # Add default thickness based on product type
            thickness_value = ""
            
            if 'Shield' in product.name:
                thickness_value = "4, 6, 8, 9, 10, 12, 15, 16, 18, 19, 20, 21, 22, 24, 25, 28, 30 mm"
            elif 'Antislip HEX' in product.name or 'Antislip MT' in product.name:
                thickness_value = "6.5, 9, 12, 15, 18, 19, 21, 24, 27, 30, 35, 40 mm"
            elif 'Parquet' in product.name:
                thickness_value = "6, 6.5, 8, 9, 10, 12, 15 mm"
            elif 'Interior Birch' in product.name:
                thickness_value = "4, 6, 8, 9, 10, 11, 12, 14, 15, 17, 18, 20, 21, 24, 25, 30 mm"
            elif 'Exterior Birch' in product.name:
                thickness_value = "6, 8, 9, 10, 12, 15, 18, 19, 21, 24, 25, 30 mm"
            elif 'Deck' in product.name:
                thickness_value = "6.5, 9, 12, 15, 16, 18, 19, 21, 24, 27, 30, 35, 40 mm"
            else:
                thickness_value = "Various thicknesses available"
            
            if thickness_value:
                # Update product thickness field
                product.thickness = thickness_value
                product.save()
                
                # Create thickness specification
                ProductSpecification.objects.create(
                    product=product,
                    name='Thicknesses, mm',
                    value=thickness_value
                )
                print(f"✓ Added default thickness: {thickness_value}")
        
        # Show all specifications in order
        all_specs = product.specifications.all().order_by('id')
        print(f"All specifications for {product.name}:")
        for i, spec in enumerate(all_specs, 1):
            print(f"  {i}. {spec.name}: {spec.value[:50]}{'...' if len(spec.value) > 50 else ''}")

    print(f"\n✅ All products now have thickness specifications!")

if __name__ == '__main__':
    fix_all_thickness_specs()
