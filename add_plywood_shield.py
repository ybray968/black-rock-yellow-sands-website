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

def add_plywood_shield():
    """Add Plywood Shield product with all specifications from the slide"""
    
    print("Adding Plywood Shield product...")
    
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
    
    # Create Plywood Shield product
    product_data = {
        'name': 'Plywood Shield',
        'slug': 'plywood-shield',
        'category': plywood_category,
        'description': '''Plywood Shield is a special brand of WBP birch plywood that has unique fire-resistance properties. All layers of veneer are impregnated with a special flame-retardant compound, making Plywood Shield a high-tech material. That is why the product meets the strictest fire safety requirements and does not require any additional processing during subsequent cutting. Fire-retardant panels can be overlaid with decorative HPL or fiberglass.''',
        'price': 0.00,  # Price to be determined
        'wood_type': 'hardwood',
        'wood_species': 'birch',
        'grade': '1/2 (B/BB)',
        'thickness': '4, 6, 8, 9, 10, 12, 15, 16, 18, 19, 20, 21, 22, 24, 25, 28, 30 mm',
        'width': 'Various sizes available',
        'length': 'Various sizes available',
        'finish': 'Not-sanded (NS) and both sides sanded (S2), overlaid with HPL, fiberglass, resin coated',
        'featured': True,
        'in_stock': True,
        'stock_quantity': 100,
        'meta_description': 'Plywood Shield - Special fire-resistant WBP birch plywood with flame-retardant compound for shipbuilding, railcar building, and construction applications.'
    }
    
    product, created = Product.objects.get_or_create(
        name='Plywood Shield',
        defaults=product_data
    )
    
    if created:
        print(f"✓ Created product: {product.name}")
        
        # Add detailed specifications from the slide (only technical specs, no advantages)
        specifications = [
            {
                'name': 'Thicknesses',
                'value': '4, 6, 8, 9, 10, 12, 15, 16, 18, 19, 20, 21, 22, 24, 25, 28, 30 mm'
            },
            {
                'name': 'Sizes',
                'value': '1525x1525, 1220x2440, 1250x2500, cut-to-size'
            },
            {
                'name': 'Grades',
                'value': '1/2 (B/BB), 2/2 (BB/BB), 2/3 (BB/CP), 2/4 (BB/C), 3/3 (CP/CP), 3/4 (CP/C), 4/4 (C/C)'
            },
            {
                'name': 'Type of surface',
                'value': 'not-sanded (NS) and both sides sanded (S2), overlaid with HPL, fiberglass, resin coated'
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
                'name': 'Fire resistance',
                'value': 'WBP grade with flame-retardant compound impregnation'
            },
            {
                'name': 'Surface treatment options',
                'value': 'Decorative HPL or fiberglass overlay available'
            },
            {
                'name': 'Processing',
                'value': 'No additional processing required during cutting'
            },
            {
                'name': 'Safety compliance',
                'value': 'Meets strictest fire safety requirements'
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
    
    print(f"\n✅ Plywood Shield product setup complete!")
    print(f"📝 Don't forget to save the product image as 'plywood-shield.png' in static/images/")

if __name__ == '__main__':
    add_plywood_shield()
