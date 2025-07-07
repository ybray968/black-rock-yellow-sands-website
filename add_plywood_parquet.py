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

def add_plywood_parquet():
    """Add Plywood Parquet product with all specifications from the slide"""
    
    print("Adding Plywood Parquet product...")
    
    # Get or create plywood category (since this is a plywood product)
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
    
    # Create Plywood Parquet product
    product_data = {
        'name': 'Plywood Parquet',
        'slug': 'plywood-parquet',
        'category': plywood_category,
        'description': '''Plywood "Parquet" is a brand of birch plywood for parquet manufacturing with strict thickness tolerances and improved surface quality. It has been developed to meet specific requirements of engineered wood flooring manufacturers and is widely used by them all over the world. It is possible to manufacture non-standard sizes and to use solid veneer in the inner layers to enhance the strength properties.''',
        'price': 0.00,  # Price to be determined
        'wood_type': 'hardwood',
        'wood_species': 'birch',
        'grade': 'B/BB',
        'thickness': '6, 6.5, 8, 9, 10, 12, 15 mm',
        'width': 'Various sizes available',
        'length': 'Various sizes available',
        'finish': 'Both sides sanded (S2)',
        'featured': True,
        'in_stock': True,
        'stock_quantity': 100,
        'meta_description': 'Premium Plywood Parquet - Birch plywood specifically designed for parquet manufacturing with strict thickness tolerances and enhanced surface quality.'
    }
    
    product, created = Product.objects.get_or_create(
        name='Plywood Parquet',
        defaults=product_data
    )
    
    if created:
        print(f"✓ Created product: {product.name}")
        
        # Add detailed specifications from the slide
        specifications = [
            {
                'name': 'Thicknesses',
                'value': '6, 6.5, 8, 9, 10, 12, 15 mm'
            },
            {
                'name': 'Sizes',
                'value': '2440x1220 or 1220x2440; 1250x2500 or 2500x1250; 1525x1525; 1500x3000; 1525x3050, cut-to-size'
            },
            {
                'name': 'Grades',
                'value': '1/2 (B/BB), 2/2 (BB/BB), 2/3 (BB/CP), 2/4 (BB/C), 3/3 (CP/CP), 3/4 (CP/C)'
            },
            {
                'name': 'Type of surface',
                'value': 'Both sides sanded (S2)'
            },
            {
                'name': 'Formaldehyde emission (limit value 3.5 mg/h x m²)',
                'value': '0.1-0.3 mg/h x m²'
            },
            {
                'name': 'High strength and durability',
                'value': 'Enhanced strength properties with solid veneer option in inner layers'
            },
            {
                'name': 'Resistance to moisture impact',
                'value': 'Improved moisture resistance for flooring applications'
            },
            {
                'name': 'Complete absence of healthy color changes in B and BB grades',
                'value': 'Consistent color quality for premium appearance'
            },
            {
                'name': 'Special thickness tolerances',
                'value': 'Strict thickness control for parquet manufacturing requirements'
            },
            {
                'name': 'Extended list of putted defects in CP grade',
                'value': 'Comprehensive quality control with detailed defect specifications'
            }
        ]
        
        for spec_data in specifications:
            ProductSpecification.objects.create(
                product=product,
                **spec_data
            )
        
        print(f"✓ Added {len(specifications)} specifications")
        
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
    print(f"Specifications: {specs_count}")
    
    print(f"\n✅ Plywood Parquet product setup complete!")

if __name__ == '__main__':
    add_plywood_parquet()
