import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product, ProductSpecification

# Add thickness specifications to the three products that are missing them
products_to_fix = [
    {
        'name': 'Plywood Deck (Construction Use)',
        'thickness_name': 'Thickness, mm',
        'thickness_name_ar': 'السُمك، مم',
        'thickness_value': '6.5, 9, 12, 15, 16, 18, 19, 21, 24, 27, 30, 35, 40',
        'thickness_value_ar': '6.5, 9, 12, 15, 16, 18, 19, 21, 24, 27, 30, 35, 40'
    },
    {
        'name': 'Plywood Interior Birch',
        'thickness_name': 'Thickness, mm',
        'thickness_name_ar': 'السُمك، مم',
        'thickness_value': '4, 6, 8, 9, 10, 11, 12, 14, 15, 17, 18, 20, 21, 24, 25, 30',
        'thickness_value_ar': '4, 6, 8, 9, 10, 11, 12, 14, 15, 17, 18, 20, 21, 24, 25, 30'
    },
    {
        'name': 'Plywood Exterior Birch (WBP)',
        'thickness_name': 'Thickness, mm',
        'thickness_name_ar': 'السُمك، مم',
        'thickness_value': '4, 6, 6.5, 8, 9, 10, 12, 15, 16, 18, 19, 21, 24, 27, 30, 35, 40',
        'thickness_value_ar': '4, 6, 6.5, 8, 9, 10, 12, 15, 16, 18, 19, 21, 24, 27, 30, 35, 40'
    }
]

print('🔧 ADDING THICKNESS SPECIFICATIONS TO MISSING PRODUCTS')
print('=' * 60)

for product_data in products_to_fix:
    try:
        product = Product.objects.get(name=product_data['name'])
        print(f'\n📦 Processing: {product.name}')
        
        # Check if thickness specification already exists
        existing_thickness = ProductSpecification.objects.filter(
            product=product,
            name__icontains='thickness'
        ).first()
        
        if existing_thickness:
            print(f'   ⚠️  Thickness specification already exists: {existing_thickness.name}')
            print(f'   📝 Updating values...')
            existing_thickness.name = product_data['thickness_name']
            existing_thickness.name_ar = product_data['thickness_name_ar']
            existing_thickness.value = product_data['thickness_value']
            existing_thickness.value_ar = product_data['thickness_value_ar']
            existing_thickness.save()
            print(f'   ✅ Updated thickness specification!')
        else:
            # Create new thickness specification
            ProductSpecification.objects.create(
                product=product,
                name=product_data['thickness_name'],
                name_ar=product_data['thickness_name_ar'],
                value=product_data['thickness_value'],
                value_ar=product_data['thickness_value_ar']
            )
            print(f'   ✅ Created thickness specification!')
        
        # Show all specifications for this product
        all_specs = ProductSpecification.objects.filter(product=product).order_by('id')
        print(f'   📋 All specifications for {product.name}:')
        for spec in all_specs:
            print(f'      - {spec.name} ({spec.name_ar}): {spec.value}')
            
    except Product.DoesNotExist:
        print(f'   ❌ Product "{product_data["name"]}" not found!')

print('\n' + '=' * 60)
print('✅ THICKNESS SPECIFICATIONS ADDED TO ALL PRODUCTS')
