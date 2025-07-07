#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product, Category, ProductImage, ProductSpecification

def add_plywood_antislip_mt():
    """Add Plywood Antislip MT product with all specifications from the slide"""
    
    print("Adding Plywood Antislip MT product...")
    
    # Get or create plywood category (since this is a specialized plywood product)
    plywood_category, created = Category.objects.get_or_create(
        name="Plywood",
        defaults={
            'slug': 'plywood',
            'description': 'High-quality plywood products for construction and specialized applications'
        }
    )
    
    if created:
        print(f"Created new category: {plywood_category.name}")
    else:
        print(f"Using existing category: {plywood_category.name}")
    
    # Create Plywood Antislip MT product
    product_data = {
        'name': 'Plywood Antislip MT',
        'slug': 'plywood-antislip-mt',
        'category': plywood_category,
        'description': '''Plywood Antislip MT is a brand of wear-resistant film-faced birch plywood with antislip surface. Both sides of plywood are overlaid with phenolic film. One side has slip-resistant wire-mesh surface. Plywood Antislip MT is perfect for the manufacturing of wear-resistant surfaces such as heavy-duty commercial transport floors. The films of various colors and densities are available. The edges of film-faced plywood are covered with acrylic paint to prevent moisture absorption.''',
        'price': 0.00,  # Price to be determined
        'wood_type': 'hardwood',
        'wood_species': 'birch',
        'grade': '1/1 (B/B)',
        'thickness': '6.5, 9, 12, 15, 18, 19, 21, 24, 27, 30, 35, 40 mm',
        'width': 'Various sizes available',
        'length': 'Various sizes available',
        'finish': 'Smooth/wire (F/W) - phenolic film with wire-mesh antislip surface',
        'featured': True,
        'in_stock': True,
        'stock_quantity': 100,
        'meta_description': 'Plywood Antislip MT - Premium film-faced birch plywood with antislip wire-mesh surface for heavy-duty commercial transport floors and wear-resistant applications.'
    }
    
    product, created = Product.objects.get_or_create(
        name='Plywood Antislip MT',
        defaults=product_data
    )
    
    if created:
        print(f"✓ Created product: {product.name}")
        
        # Add detailed specifications from the slide (only technical specs, no advantages)
        specifications = [
            {
                'name': 'Thicknesses',
                'value': '6.5, 9, 12, 15, 18, 19, 21, 24, 27, 30, 35, 40 mm'
            },
            {
                'name': 'Sizes',
                'value': '2440x1220 or 1220x2440; 1250x2500 or 2500x1250; 1525x1525; 1500x3000; 1525x3050, cut-to-size'
            },
            {
                'name': 'Grades',
                'value': '1/1 (B/B)'
            },
            {
                'name': 'Type of surface',
                'value': 'smooth/wire (F/W)'
            },
            {
                'name': 'Film density',
                'value': '120/130, 120/220, 220/220 g/m²'
            },
            {
                'name': 'Formaldehyde emission (limit value 3.5 mg/h x m²)',
                'value': '0.1-0.3 mg/h x m²'
            },
            {
                'name': 'Application',
                'value': 'Heavy-duty commercial transport floors, construction, packaging'
            },
            {
                'name': 'Surface treatment',
                'value': 'Phenolic film overlay with wire-mesh antislip surface'
            },
            {
                'name': 'Edge sealing',
                'value': 'Acrylic paint to prevent moisture absorption'
            }
        ]
        
        for spec_data in specifications:
            ProductSpecification.objects.create(
                product=product,
                **spec_data
            )
        
        print(f"✓ Added {len(specifications)} technical specifications")
        
    else:
        print(f"Product '{product.name}' already exists")
    
    print(f"\nProduct Details:")
    print(f"Name: {product.name}")
    print(f"Category: {product.category.name}")
    print(f"Wood Type: {product.get_wood_type_display()}")
    print(f"Wood Species: {product.get_wood_species_display()}")
    print(f"Grade: {product.grade}")
    print(f"Thickness: {product.thickness}")
    print(f"Finish: {product.finish}")
    print(f"Featured: {product.featured}")
    print(f"In Stock: {product.in_stock}")
    
    # Show specifications count
    specs_count = ProductSpecification.objects.filter(product=product).count()
    print(f"Technical Specifications: {specs_count}")
    
    print(f"\n✅ Plywood Antislip MT product setup complete!")
    print(f"📝 Don't forget to save the product image as 'plywood-antislip-mt.png' in static/images/")

if __name__ == '__main__':
    add_plywood_antislip_mt()
