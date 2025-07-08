#!/usr/bin/env python3
"""
Script to help translate product specification values to Arabic
This script shows existing values that need translation
"""

import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import ProductSpecification

def show_values_needing_translation():
    """Show specification values that need Arabic translation"""
    print("Specification values that might need Arabic translation:")
    print("=" * 60)
    
    # Get unique values that don't have Arabic translations
    specs_without_arabic = ProductSpecification.objects.filter(value_ar='')
    
    unique_values = set()
    for spec in specs_without_arabic:
        if spec.value not in unique_values:
            unique_values.add(spec.value)
            print(f"Value: {spec.value}")
            print(f"Used in: {spec.name}")
            print("-" * 40)
    
    print(f"\nTotal unique values needing translation: {len(unique_values)}")

def translate_specific_values():
    """Translate specific common values to Arabic"""
    # Common translations for measurement units and common values
    VALUE_TRANSLATIONS = {
        # Add specific value translations here as needed
        # Example:
        # "18 mm": "18 مم",
        # "B/BB": "ب/ب ب",
        # "Phenol Formaldehyde": "فينول فورمالديهايد",
        # Add more as needed...
    }
    
    updated_count = 0
    for spec in ProductSpecification.objects.filter(value_ar=''):
        if spec.value in VALUE_TRANSLATIONS:
            spec.value_ar = VALUE_TRANSLATIONS[spec.value]
            spec.save()
            updated_count += 1
            print(f"Updated value: {spec.value} -> {spec.value_ar}")
    
    print(f"\nUpdated {updated_count} specification values with Arabic translations.")

if __name__ == '__main__':
    show_values_needing_translation()
    # Uncomment the line below to apply translations
    # translate_specific_values()
