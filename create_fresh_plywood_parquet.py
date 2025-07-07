#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product, Category, ProductSpecification

def create_fresh_plywood_parquet():
    """Create fresh Plywood Parquet product in Plywood category with all saved content"""
    
    print("Creating fresh Plywood Parquet product in Plywood category...")
    
    # Get the plywood category (should already exist)
    try:
        plywood_category = Category.objects.get(slug='plywood')
        print(f"Using existing Plywood category: {plywood_category.name}")
    except Category.DoesNotExist:
        # Create if it doesn't exist
        plywood_category = Category.objects.create(
            name="Plywood",
            slug='plywood',
            description='High-quality plywood products for construction and specialized applications'
        )
        print(f"Created new Plywood category: {plywood_category.name}")
    
    # Create Plywood Parquet product with saved content
    product_data = {
        'name': 'Plywood Parquet',
        'slug': 'plywood-parquet',
        'category': plywood_category,  # This is the key - putting it in Plywood category
        'description': '''Plywood "Parquet" is a brand of birch plywood for parquet manufacturing with strict thickness tolerances and improved surface quality. It has been developed to meet specific requirements of engineered wood flooring manufacturers and is widely used by them all over the world. It is possible to manufacture non-standard sizes and to use solid veneer in the inner layers to enhance the strength properties.''',
        'price': 0.00,
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
    
    # Create the product
    product = Product.objects.create(**product_data)
    print(f"✓ Created product: {product.name} in {product.category.name} category")
    
    # Add detailed specifications (saved content)
    specifications = [
        ('Sizes, mm', '2440x1220 or 1220x2440; 1250x2500 or 2500x1250; 1525x1525; 1500x3000; 1525x3050, cut-to-size'),
        ('Grades', '1/2 (B/BB), 2/2 (BB/BB), 2/3 (BB/CP), 2/4 (BB/C), 3/3 (CP/CP), 3/4 (CP/C)'),
        ('Type of surface', 'Both sides sanded (S2)'),
        ('Formaldehyde emission (limit value 3.5 mg/h x m²)', '0.1-0.3 mg/h x m²'),
        ('Application', 'Parquet manufacturing, engineered wood flooring, premium interior applications'),
        ('Thickness tolerances', 'Strict thickness control for parquet manufacturing requirements'),
        ('Surface quality', 'Enhanced surface quality with consistent color in B and BB grades'),
        ('Solid veneer option', 'Solid veneer available in inner layers for enhanced strength properties')
    ]
    
    for spec_name, spec_value in specifications:
        ProductSpecification.objects.create(
            product=product,
            name=spec_name,
            value=spec_value
        )
    
    print(f"✓ Added {len(specifications)} specifications")
    
    print(f"\n✅ Fresh Plywood Parquet product created successfully!")
    print(f"📋 Product Details:")
    print(f"   Name: {product.name}")
    print(f"   Category: {product.category.name} (slug: {product.category.slug})")
    print(f"   Wood Species: {product.get_wood_species_display()}")
    print(f"   Grade: {product.grade}")
    print(f"   Thickness: {product.thickness}")
    print(f"   Featured: {product.featured}")
    print(f"   In Stock: {product.in_stock}")
    
    print(f"\n🎯 Now Plywood Parquet will:")
    print(f"   ✅ Appear with other plywood products")
    print(f"   ✅ Use plywood template advantages (Parquet-specific)")
    print(f"   ✅ Show main image: plywood-parquet.png")
    print(f"   ✅ Show application image: plywood-parquet-application.png")
    print(f"   ✅ Have application image space under main image")
    
    print(f"\n📝 Next step: Create the application image file:")
    print(f"   plywood-parquet-application.png")

if __name__ == '__main__':
    create_fresh_plywood_parquet()
