import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Category, Product, ProductSpecification

# Find the plywood product
try:
    product = Product.objects.get(name='Plywood Deck (Construction Use)')
    print(f"Found product: {product.name}")
    
    # Find all thickness-related specifications
    thickness_specs = ProductSpecification.objects.filter(
        product=product,
        name__icontains='thick'
    )
    
    print(f"Found {thickness_specs.count()} thickness-related specifications:")
    for spec in thickness_specs:
        print(f"  - {spec.name}: {spec.value}")
    
    # Remove any specifications that contain "thickness" or "Thickness" but don't end with "mm"
    specs_to_remove = ProductSpecification.objects.filter(
        product=product,
        name__icontains='thick'
    ).exclude(name__endswith='mm')
    
    if specs_to_remove.exists():
        print(f"\nRemoving {specs_to_remove.count()} duplicate thickness specifications:")
        for spec in specs_to_remove:
            print(f"  - Removing: {spec.name}: {spec.value}")
            spec.delete()
        print("Duplicate thickness specifications removed successfully!")
    else:
        print("No duplicate thickness specifications found to remove.")
    
    # Also remove any duplicate advantages that might be in specifications
    advantage_specs = ProductSpecification.objects.filter(
        product=product,
        name__in=[
            'Strength and durability',
            'Environmental resistance', 
            'Water resistance',
            'Film variety',
            'Uses'
        ]
    )
    
    if advantage_specs.exists():
        print(f"\nRemoving {advantage_specs.count()} advantage specifications that should not be in specs table:")
        for spec in advantage_specs:
            print(f"  - Removing: {spec.name}: {spec.value}")
            spec.delete()
        print("Advantage specifications removed from specs table!")
    else:
        print("No advantage specifications found in specs table.")
        
    # Show remaining specifications
    remaining_specs = ProductSpecification.objects.filter(product=product)
    print(f"\nRemaining specifications ({remaining_specs.count()}):")
    for spec in remaining_specs:
        print(f"  - {spec.name}: {spec.value}")
        
except Product.DoesNotExist:
    print("Plywood Deck product not found!")
