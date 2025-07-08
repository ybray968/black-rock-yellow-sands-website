import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product

# Check the three plywood products
product_names = [
    'Plywood Deck (Construction Use)',
    'Plywood Exterior Birch (WBP)', 
    'Plywood Interior Birch'
]

print("🔍 CHECKING THICKNESS VALUES FOR PLYWOOD PRODUCTS")
print("=" * 60)

for name in product_names:
    try:
        product = Product.objects.get(name=name)
        print(f"\n📦 Product: {product.name}")
        print(f"   Thickness: '{product.thickness}'")
        print(f"   Thickness empty: {not product.thickness}")
        print(f"   Thickness length: {len(product.thickness) if product.thickness else 0}")
        
        if product.thickness:
            print(f"   ✅ HAS THICKNESS DATA")
        else:
            print(f"   ❌ MISSING THICKNESS DATA")
            
    except Product.DoesNotExist:
        print(f"\n❌ Product '{name}' not found in database")

print("\n" + "=" * 60)
