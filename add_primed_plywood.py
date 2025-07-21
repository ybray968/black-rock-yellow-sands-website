#!/usr/bin/env python
"""
Add Primed Plywood product to the database
Based on the product slide information
"""

import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

from products.models import Product, Category, Specification

def add_primed_plywood():
    """Add Primed Plywood product with specifications and advantages"""
    
    # Get or create category
    plywood_category, created = Category.objects.get_or_create(
        name='Plywood',
        defaults={
            'slug': 'plywood',
            'description': 'High-quality plywood products'
        }
    )
    
    # Product description based on the slide
    product_description = """Primed Plywood is a brand of birch plywood overlaid with paper-based melamine film that makes a surface prepared for painting. Primed Plywood is suitable for indoor and outdoor use, provided that the coating materials meet the environmental conditions. The neutral grey film serves as an excellent base for the application of any color. That is why, plywood with the surface prepared for painting is the perfect solution for bright individual projects."""
    
    # Arabic description - keeping product name in English as requested
    product_description_ar = """Primed Plywood هو علامة تجارية من الخشب الرقائقي البتولا المغطى بفيلم الميلامين الورقي الذي يجعل السطح معد للطلاء. Primed Plywood مناسب للاستخدام الداخلي والخارجي، بشرط أن تلبي مواد الطلاء الظروف البيئية. الفيلم الرمادي المحايد يعمل كقاعدة ممتازة لتطبيق أي لون. لهذا السبب، الخشب الرقائقي مع السطح المعد للطلاء هو الحل المثالي للمشاريع الفردية المشرقة."""
    
    # Create or update the product
    product, created = Product.objects.get_or_create(
        name='Primed Plywood',
        defaults={
            'category': plywood_category,
            'description': product_description,
            'description_ar': product_description_ar,
            'wood_species': 'birch',
            'wood_type': 'film_faced',
            'in_stock': True,
            'featured': True
        }
    )
    
    if not created:
        # Update existing product
        product.description = product_description
        product.description_ar = product_description_ar
        product.wood_species = 'birch'
        product.wood_type = 'film_faced'
        product.in_stock = True
        product.featured = True
        product.save()
        print(f"Updated existing product: {product.name}")
    else:
        print(f"Created new product: {product.name}")
    
    # Clear existing specifications for this product
    product.specifications.all().delete()
    
    # Add specifications based on the slide
    specifications = [
        ("Thicknesses, mm", "6.5, 9, 12, 15, 18, 19, 21, 24, 27, 30, 35, 40", "السماكات، مم", "6.5، 9، 12، 15، 18، 19، 21، 24، 27، 30، 35، 40"),
        ("Sizes, mm", "2440x1220 or 1220x2440; 1250x2500 or 2500x1250; 1525x1525; 1500x3000; 1525x3050, cut-to-size", "الأحجام، مم", "2440x1220 أو 1220x2440؛ 1250x2500 أو 2500x1250؛ 1525x1525؛ 1500x3000؛ 1525x3050، قطع حسب المقاس"),
        ("Grades", "1/1 (B/B)", "الدرجات", "1/1 (B/B)"),
        ("Type of surface", "smooth/smooth (F/F)", "نوع السطح", "ناعم/ناعم (F/F)"),
        ("Film density, g/m²", "140, 220", "كثافة الفيلم، غ/م²", "140، 220"),
        ("The formaldehyde emission (limit value 3.5 mg/h x m²)", "0.1-0.3 mg/h x m²", "انبعاث الفورمالديهايد (القيمة الحدية 3.5 مغ/ساعة × م²)", "0.1-0.3 مغ/ساعة × م²"),
    ]
    
    for spec_name, spec_value, spec_name_ar, spec_value_ar in specifications:
        Specification.objects.create(
            product=product,
            name=spec_name,
            value=spec_value,
            name_ar=spec_name_ar,
            value_ar=spec_value_ar
        )
        print(f"Added specification: {spec_name}")
    
    print(f"\nSuccessfully added Primed Plywood product with {len(specifications)} specifications!")
    return product

if __name__ == "__main__":
    add_primed_plywood()
