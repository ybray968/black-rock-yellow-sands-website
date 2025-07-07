#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import ProductSpecification

def remove_advantage_specifications():
    """Remove advantage specifications from all products"""
    
    print("Removing advantage specifications from database...")
    
    # List of advantage specification names to remove
    advantage_specs = [
        'High strength and durability',
        'Resistance to moisture impact',
        'Complete absence of healthy color changes in B and BB grades',
        'Special thickness tolerances',
        'Extended list of putted defects in CP grade',
        'Strength and durability',
        'Environmental resistance',
        'Water resistance',
        'Film variety'
    ]
    
    removed_count = 0
    
    for spec_name in advantage_specs:
        specs_to_remove = ProductSpecification.objects.filter(name__icontains=spec_name)
        count = specs_to_remove.count()
        if count > 0:
            print(f"Removing {count} specifications with name containing '{spec_name}'")
            specs_to_remove.delete()
            removed_count += count
    
    print(f"\n✅ Total removed: {removed_count} advantage specifications")
    print("Advantages will now only appear in the visual advantage plates, not in specifications.")

if __name__ == '__main__':
    remove_advantage_specifications()
