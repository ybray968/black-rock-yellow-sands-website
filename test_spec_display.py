import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product, ProductSpecification

# Test what specifications would be displayed for the three products
product_names = [
    'Plywood Deck (Construction Use)',
    'Plywood Exterior Birch (WBP)', 
    'Plywood Interior Birch'
]

# These are the filter conditions from the template
filter_conditions = [
    'Strength and durability',
    'Environmental resistance',
    'Water resistance',
    'Film variety',
    'High strength and durability',
    'Resistance to moisture impact',
    'Complete absence of healthy color changes',
    'Extended list of putted defects'
]

print('🧪 TESTING SPECIFICATION DISPLAY FOR THE THREE PRODUCTS')
print('=' * 60)

for name in product_names:
    try:
        product = Product.objects.get(name=name)
        print(f'\n📦 Product: {product.name}')
        
        specs = ProductSpecification.objects.filter(product=product)
        print(f'   Total specifications: {specs.count()}')
        
        displayed_specs = []
        filtered_specs = []
        
        for spec in specs:
            should_filter = False
            for condition in filter_conditions:
                if condition in spec.name:
                    should_filter = True
                    filtered_specs.append(f'{spec.name} (filtered by: {condition})')
                    break
            
            if not should_filter:
                displayed_specs.append(f'{spec.name}: {spec.value}')
        
        print(f'   ✅ DISPLAYED specifications ({len(displayed_specs)}):')
        for spec in displayed_specs:
            print(f'      - {spec}')
            
        if filtered_specs:
            print(f'   ❌ FILTERED OUT specifications ({len(filtered_specs)}):')
            for spec in filtered_specs:
                print(f'      - {spec}')
            
    except Product.DoesNotExist:
        print(f'\n❌ Product "{name}" not found!')

print('\n' + '=' * 60)
