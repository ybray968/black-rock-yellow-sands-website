import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product, ProductSpecification

# Fix the order of specifications for the three products
products_to_fix = [
    'Plywood Deck (Construction Use)',
    'Plywood Interior Birch',
    'Plywood Exterior Birch (WBP)'
]

print('🔧 FIXING SPECIFICATION ORDER TO MATCH OTHER PRODUCTS')
print('=' * 60)

for name in products_to_fix:
    try:
        product = Product.objects.get(name=name)
        print(f'\n📦 Processing: {product.name}')
        
        # Get all specifications, ordered incorrectly
        specs = ProductSpecification.objects.filter(
            product=product
        ).order_by('id')
        
        print(f'   BEFORE order:')
        for spec in specs:
            print(f'   - {spec.name}: {spec.value}')
        
        # Re-order thickness specification to be first
        thickness_spec = specs.filter(name__icontains='thickness').first()
        if thickness_spec:
            print(f'   ⭐ Moving {thickness_spec.name} to the top...')
            all_except_thickness = list(specs.exclude(id=thickness_spec.id))
            # Remove existing thickness
            thickness_spec.delete()
            # Re-add thickness first
            ProductSpecification.objects.create(
                product=product,
                name=thickness_spec.name,
                name_ar=thickness_spec.name_ar,
                value=thickness_spec.value
            )
            
            # Re-add remaining in original order
            for spec in all_except_thickness:
                ProductSpecification.objects.create(
                    product=product,
                    name=spec.name,
                    name_ar=spec.name_ar,
                    value=spec.value,
                    value_ar=spec.value_ar
                )
        
        # Verify new order
        specs_updated = ProductSpecification.objects.filter(
            product=product
        ).order_by('id')
        
        print(f'   AFTER order:')
        for spec in specs_updated:
            print(f'   - {spec.name}: {spec.value}')
        
    except Product.DoesNotExist:
        print(f'   ❌ Product "{name}" not found!')

print('\n' + '=' * 60)
print('✅ SPECIFICATION ORDER FIXED FOR ALL PRODUCTS')
