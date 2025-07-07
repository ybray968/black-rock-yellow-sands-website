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

def rename_plyterra_to_plywood_antislip_mt():
    """Rename Plyterra Antislip Wire to Plywood Antislip MT and update all references"""
    
    print("Renaming Plyterra Antislip Wire to Plywood Antislip MT...")
    
    # Find the Plyterra product
    try:
        plyterra_product = Product.objects.get(name__icontains="Plyterra Antislip Wire")
        print(f"Found product: {plyterra_product.name}")
    except Product.DoesNotExist:
        print("Plyterra Antislip Wire product not found")
        return
    except Product.MultipleObjectsReturned:
        plyterra_product = Product.objects.filter(name__icontains="Plyterra").first()
        print(f"Found multiple products, using: {plyterra_product.name}")
    
    # Update product name and slug
    old_name = plyterra_product.name
    plyterra_product.name = "Plywood Antislip MT"
    plyterra_product.slug = "plywood-antislip-mt"
    
    # Update description to replace Plyterra with Plywood
    old_description = plyterra_product.description
    new_description = old_description.replace("Plyterra Antislip Wire", "Plywood Antislip MT")
    new_description = new_description.replace("Plyterra", "Plywood")
    plyterra_product.description = new_description
    
    # Update finish field
    old_finish = plyterra_product.finish
    new_finish = old_finish.replace("Plyterra", "Plywood") if old_finish else ""
    plyterra_product.finish = new_finish
    
    # Update meta description
    old_meta = plyterra_product.meta_description
    new_meta = old_meta.replace("Plyterra Antislip Wire", "Plywood Antislip MT")
    new_meta = new_meta.replace("Plyterra", "Plywood")
    plyterra_product.meta_description = new_meta
    
    # Save the product
    plyterra_product.save()
    print(f"✓ Updated product name from '{old_name}' to '{plyterra_product.name}'")
    print(f"✓ Updated slug to: {plyterra_product.slug}")
    
    # Update any specifications that mention Plyterra
    specifications = ProductSpecification.objects.filter(product=plyterra_product)
    updated_specs = 0
    
    for spec in specifications:
        old_spec_name = spec.name
        old_spec_value = spec.value
        
        # Update name if it contains Plyterra
        if "Plyterra" in spec.name:
            spec.name = spec.name.replace("Plyterra", "Plywood")
            updated_specs += 1
        
        # Update value if it contains Plyterra
        if "Plyterra" in spec.value:
            spec.value = spec.value.replace("Plyterra", "Plywood")
            updated_specs += 1
        
        # Save if any changes were made
        if spec.name != old_spec_name or spec.value != old_spec_value:
            spec.save()
            print(f"  - Updated specification: {old_spec_name} -> {spec.name}")
    
    if updated_specs > 0:
        print(f"✓ Updated {updated_specs} specification references")
    else:
        print("✓ No specification updates needed")
    
    print(f"\n✅ Product successfully renamed!")
    print(f"New Product Details:")
    print(f"Name: {plyterra_product.name}")
    print(f"Slug: {plyterra_product.slug}")
    print(f"Description: {plyterra_product.description[:100]}...")
    print(f"Finish: {plyterra_product.finish}")
    
    # Show remaining specifications
    remaining_specs = ProductSpecification.objects.filter(product=plyterra_product)
    print(f"\nSpecifications ({remaining_specs.count()}):")
    for spec in remaining_specs:
        print(f"  - {spec.name}: {spec.value[:50]}...")

if __name__ == '__main__':
    rename_plyterra_to_plywood_antislip_mt()
