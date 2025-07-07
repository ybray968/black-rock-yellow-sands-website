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

def add_plywood_shield_acu():
    """Add Plywood Shield Acu product with all specifications from the slide"""
    
    print("Adding Plywood Shield Acu product...")
    
    # Get or create plywood category
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
    
    # Create Plywood Shield Acu product
    product_data = {
        'name': 'Plywood Shield Acu',
        'slug': 'plywood-shield-acu',
        'category': plywood_category,
        'description': '''Plywood Shield Acu is a special brand of WBP birch plywood that has unique sound-insulation and fire-resistance properties. In addition to birch veneer, the panel structure includes a layer of sound-absorbing material, the function of which can be performed by a technical cork, rubber or a composite material made of cork and rubber crumbs. The choice of sound-absorbing material depends on the preferences of the customer and the scope of product application: plywood with a layer of technical cork has a lighter weight compared to standard plywood, while the rubber layer absorbs vibration and provides a higher level of noise insulation.''',
        'price': 0.00,  # Price to be determined
        'wood_type': 'hardwood',
        'wood_species': 'birch',
        'grade': '1/2 (B/BB)',
        'thickness': '11, 13, 15, 17, 19, 21, 23 mm',
        'width': 'Various sizes available',
        'length': 'Various sizes available',
        'finish': 'Not-sanded (NS) and both sides sanded (S2), overlaid with HPL',
        'featured': True,
        'in_stock': True,
        'stock_quantity': 100,
        'meta_description': 'Plywood Shield Acu - Special WBP birch plywood with unique sound-insulation and fire-resistance properties for shipbuilding, railcar building, and construction applications.'
    }
    
    product, created = Product.objects.get_or_create(
        name='Plywood Shield Acu',
        defaults=product_data
    )
    
    if created:
        print(f"✓ Created product: {product.name}")
        
        # Add detailed specifications from the slide (only technical specs, no advantages)
        specifications = [
            {
                'name': 'Thicknesses, mm',
                'value': '11, 13, 15, 17, 19, 21, 23'
            },
            {
                'name': 'Sizes, mm',
                'value': '1500x1500, 1220x2440, 1450x2950 cut-to-size'
            },
            {
                'name': 'Grades',
                'value': '1/2 (B/BB), 2/2 (BB/BB), 2/3 (BB/CP), 2/4 (BB/C), 3/3 (CP/CP), 3/4 (CP/C), 4/4 (C/C)'
            },
            {
                'name': 'Type of surface',
                'value': 'not-sanded (NS) and both sides sanded (S2), overlaid with HPL'
            },
            {
                'name': 'Formaldehyde emission (limit value 3.5 mg/h x m²)',
                'value': '0.1-0.3 mg/h x m²'
            },
            {
                'name': 'Application',
                'value': 'Shipbuilding, railcar building, construction'
            },
            {
                'name': 'Sound insulation',
                'value': 'WBP grade with sound-absorbing material layer'
            },
            {
                'name': 'Fire resistance',
                'value': 'Fire-resistance properties with flame-retardant compound'
            },
            {
                'name': 'Sound-absorbing materials',
                'value': 'Technical cork, rubber, or composite material made of cork and rubber crumbs'
            },
            {
                'name': 'Weight options',
                'value': 'Cork layer - lighter weight; Rubber layer - higher noise insulation'
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
    
    print(f"\n✅ Plywood Shield Acu product setup complete!")
    print(f"📝 Don't forget to save the product image as 'plywood-shield-acu.png' in static/images/")
    print(f"📝 NOTE: I did NOT modify the template. You'll need to add the advantages section manually or let me know if you want me to add it to the template.")

if __name__ == '__main__':
    add_plywood_shield_acu()
