#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product

def fix_interior_birch_description():
    """Fix the Arabic description for Plywood Interior Birch to remove technical terms"""
    
    try:
        product = Product.objects.get(name='Plywood Interior Birch')
        # Updated Arabic description without technical abbreviations
        arabic_desc = '''الخشب الرقائقي "Interior Birch" هو منتج صديق للبيئة مع انبعاثات فورمالديهايد منخفضة وآمنة. يتميز بنسيجه الجميل وسهولة التعامل معه، مما يجعله مثالياً للديكور الداخلي وتصنيع الأثاث.'''
        
        product.description_ar = arabic_desc
        product.save()
        print("✅ Fixed Arabic description for Plywood Interior Birch")
        print(f"New description: {arabic_desc}")
        
    except Exception as e:
        print(f"❌ Error fixing description: {e}")

if __name__ == '__main__':
    fix_interior_birch_description()
