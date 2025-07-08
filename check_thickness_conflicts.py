import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product, ProductSpecification

# Check all products for thickness data
products = Product.objects.all()
print('🔍 CHECKING ALL PRODUCTS FOR THICKNESS DATA')
print('=' * 60)

for product in products:
    print(f'\n📦 Product: {product.name}')
    print(f'   Product.thickness field: "{product.thickness}"')
    
    # Check if there are thickness specifications
    thickness_specs = ProductSpecification.objects.filter(
        product=product, 
        name__icontains='thickness'
    )
    
    if thickness_specs.exists():
        print(f'   📋 Thickness specifications found:')
        for spec in thickness_specs:
            print(f'      - {spec.name}: {spec.value}')
    else:
        print(f'   📋 No thickness specifications found')
    
    # Check if both exist (duplicate)
    if product.thickness and thickness_specs.exists():
        print(f'   ⚠️  DUPLICATE: Both product.thickness and specifications exist!')
    elif product.thickness:
        print(f'   ✅ Only product.thickness exists')
    elif thickness_specs.exists():
        print(f'   ✅ Only specifications exist')
    else:
        print(f'   ❌ No thickness data at all')

print('\n' + '=' * 60)
