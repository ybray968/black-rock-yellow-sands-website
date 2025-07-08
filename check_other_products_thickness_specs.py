import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product, ProductSpecification

# Check what thickness specifications the OTHER products have
other_products = Product.objects.exclude(name__in=['Plywood Deck (Construction Use)', 'Plywood Exterior Birch (WBP)', 'Plywood Interior Birch'])

print('OTHER PRODUCTS THICKNESS SPECIFICATIONS:')
print('=' * 60)

for product in other_products:
    thickness_specs = ProductSpecification.objects.filter(product=product, name__icontains='thickness')
    if thickness_specs.exists():
        print(f'\n📦 {product.name}:')
        for spec in thickness_specs:
            print(f'   Name: "{spec.name}"')
            print(f'   Name_ar: "{spec.name_ar}"')
            print(f'   Value: "{spec.value}"')
            print(f'   Value_ar: "{spec.value_ar}"')
            print('   ---')
