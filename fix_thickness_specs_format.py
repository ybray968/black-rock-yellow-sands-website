import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product, ProductSpecification

# Fix the thickness specifications for the three products to match other products
products_to_fix = [
    {
        'name': 'Plywood Deck (Construction Use)',
        'thickness_name': 'Thicknesses',
        'thickness_name_ar': 'السماكات',
        'thickness_value': '6.5, 9, 12, 15, 16, 18, 19, 21, 24, 27, 30, 35, 40 mm',
        'thickness_value_ar': ''
    },
    {
        'name': 'Plywood Interior Birch',
        'thickness_name': 'Thicknesses',
        'thickness_name_ar': 'السماكات',
        'thickness_value': '4, 6, 8, 9, 10, 11, 12, 14, 15, 17, 18, 20, 21, 24, 25, 30 mm',
        'thickness_value_ar': ''
    },
    {
        'name': 'Plywood Exterior Birch (WBP)',
        'thickness_name': 'Thicknesses',
        'thickness_name_ar': 'السماكات',
        'thickness_value': '4, 6, 6.5, 8, 9, 10, 12, 15, 16, 18, 19, 21, 24, 27, 30, 35, 40 mm',
        'thickness_value_ar': ''
    }
]

print('🔧 FIXING THICKNESS SPECIFICATIONS TO MATCH OTHER PRODUCTS')
print('=' * 60)

for product_data in products_to_fix:
    try:
        product = Product.objects.get(name=product_data['name'])
        print(f'\n📦 Processing: {product.name}')
        
        # Delete existing thickness specifications
        existing_thickness = ProductSpecification.objects.filter(
            product=product,
            name__icontains='thickness'
        )
        
        if existing_thickness.exists():
            print(f'   🗑️  Deleting old thickness specifications...')
            for spec in existing_thickness:
                print(f'      - Deleting: {spec.name}')
                spec.delete()
        
        # Create new thickness specification with correct format
        new_spec = ProductSpecification.objects.create(
            product=product,
            name=product_data['thickness_name'],
            name_ar=product_data['thickness_name_ar'],
            value=product_data['thickness_value'],
            value_ar=product_data['thickness_value_ar']
        )
        print(f'   ✅ Created new thickness specification!')
        print(f'      - Name: "{new_spec.name}"')
        print(f'      - Name_ar: "{new_spec.name_ar}"')
        print(f'      - Value: "{new_spec.value}"')
        
    except Product.DoesNotExist:
        print(f'   ❌ Product "{product_data["name"]}" not found!')

print('\n' + '=' * 60)
print('✅ THICKNESS SPECIFICATIONS FIXED TO MATCH OTHER PRODUCTS')
