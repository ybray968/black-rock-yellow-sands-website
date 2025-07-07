import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Category, Product, ProductSpecification

# Get or create the plywood category
category, created = Category.objects.get_or_create(
    name='Plywood',
    defaults={'slug': 'plywood', 'description': 'High-quality plywood for construction and building needs'}
)

# Get or create the Plywood Deck product
product, created = Product.objects.get_or_create(
    name='Plywood Deck (Construction Use)',
    defaults={
        'slug': slugify('Plywood Deck Construction Use'),
        'description': 'Plywood "Deck" is a brand of ultra-durable birch plywood for construction filmed on both sides with a high-density phenolic paper film. The durable smooth film impregnated with phenol-formaldehyde resin makes birch plywood more resistant to mechanical damage, moisture absorption and sunlight. High wear resistant plywood is perfect for concrete work and box bodies.\n\n<strong>Can be used in 50 cycles of cement work on average.</strong>',
        'price': 45.00,
        'category': category,
        'wood_species': 'birch',
        'wood_type': '',
        'thickness': '6.5, 9, 12, 15, 16, 18, 19, 21, 24, 27, 30, 35, 40 mm',
        'grade': '1/1 (B/B)',
        'finish': 'Smooth/Smooth (F/F)',
        'in_stock': True,
        'stock_quantity': 100,
        'featured': True,
        'meta_description': 'Ultra-durable birch plywood filmed with phenolic paper for construction use. High resistance to mechanical damage and moisture.'
    }
)

# Update the description if the product already exists
if not created:
    product.description = 'Plywood "Deck" is a brand of ultra-durable birch plywood for construction filmed on both sides with a high-density phenolic paper film. The durable smooth film impregnated with phenol-formaldehyde resin makes birch plywood more resistant to mechanical damage, moisture absorption and sunlight. High wear resistant plywood is perfect for concrete work and box bodies.\n\n<strong>Can be used in 50 cycles of cement work on average.</strong>'
    product.save()
    print('Plywood Deck product description updated successfully!')

if created:
    print('Plywood Deck product added successfully!')
    
    # Add detailed specifications
    specifications = [
        ('Sizes, mm', '2440x1220 or 1220x2440; 1250x2500 or 2500x1250; 1525x1525; 1525x3050, cut-to-size'),
        ('Grades', '1/1 (B/B)'),
        ('Type of surface', 'smooth/smooth (F/F)'),
        ('Film density, g/m²', '120/120, 120/220, 220/220'),
        ('Formaldehyde emission (limit value 3.5 mg/h x m²)', '0.1-0.3 mg/h x m²')
    ]
    
    for spec_name, spec_value in specifications:
        ProductSpecification.objects.create(
            product=product,
            name=spec_name,
            value=spec_value
        )
    
    print('Product specifications added successfully!')
else:
    print('Plywood Deck product already exists.')

