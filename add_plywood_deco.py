#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product, ProductSpecification, Category

def add_plywood_deco():
    # Create or get the category
    category, created = Category.objects.get_or_create(name="Plywood")
    if created:
        print(f"Created category: {category.name}")
    else:
        print(f"Category already exists: {category.name}")

    # Create or get the product
    product, created = Product.objects.get_or_create(
        name="Plywood Deco",
        defaults={
            'description': 'Plywood Deco is a brand of film-faced birch plywood that comprises the beauty of peeled birch veneer and advantages of melamine film. The transparent film significantly improves the performance of the surface. Moreover, the film does not crack or deform during the mechanical processing of the panels: during the installation of fasteners, assembly, cutting to size, bonding, CNC processing.',
            'category': category,
            'price': 0.00,
            'wood_type': 'hardwood',
            'wood_species': 'birch',
            'grade': 'B/B',
            'thickness': '6.5, 9, 12, 15, 18, 21, 24, 27, 30, 35, 40',
            'finish': 'Film-faced (F/F)',
            'featured': True,
            'in_stock': True
        }
    )
    
    if created:
        print(f"Created product: {product.name}")
    else:
        print(f"Product already exists: {product.name}")
    
    # Add specifications
    specifications = [
        ("Thickness, mm", "6.5, 9, 12, 15, 18, 21, 24, 27, 30, 35, 40"),
        ("Sizes, mm", "2440x1220 or 1220x2440; 1250x2500 or 2500x1250; 2500x1525; 1525x3050, cut-to-size"),
        ("Grades", "1/1 (B/B)"),
        ("Type of surface", "smooth/smooth (F/F)"),
        ("Film density, g/m²", "120/120"),
        ("The formaldehyde emission (limit value 3.5 mg/h x m²)", "0,1-0,3 mg/h x m²"),
    ]
    
    for spec_name, spec_value in specifications:
        spec, created = ProductSpecification.objects.get_or_create(
            product=product,
            name=spec_name,
            defaults={'value': spec_value}
        )
        if created:
            print(f"  Added specification: {spec_name}")
        else:
            print(f"  Specification already exists: {spec_name}")

if __name__ == '__main__':
    add_plywood_deco()
    print("Plywood Deco product has been added successfully!")
