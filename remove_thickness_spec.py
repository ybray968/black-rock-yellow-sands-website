import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product, ProductSpecification

# Find the plywood product
try:
    product = Product.objects.get(name='Plywood Deck (Construction Use)')
    print(f"Found product: {product.name}")
    print(f"Product thickness field: {product.thickness}")
    
    # Remove the "Thicknesses, mm" specification since thickness should come from product.thickness field
    thickness_spec = ProductSpecification.objects.filter(
        product=product,
        name='Thicknesses, mm'
    )
    
    if thickness_spec.exists():
        print(f"\nRemoving duplicate 'Thicknesses, mm' specification...")
        for spec in thickness_spec:
            print(f"  - Removing: {spec.name}: {spec.value}")
            spec.delete()
        print("Duplicate 'Thicknesses, mm' specification removed!")
    else:
        print("No 'Thicknesses, mm' specification found in specs table.")
    
    # Show all remaining specifications
    remaining_specs = ProductSpecification.objects.filter(product=product)
    print(f"\nFinal specifications in database ({remaining_specs.count()}):")
    for spec in remaining_specs:
        print(f"  - {spec.name}: {spec.value}")
    
    print(f"\nThickness will be displayed from product.thickness field: {product.thickness}")
        
except Product.DoesNotExist:
    print("Plywood Deck product not found!")
