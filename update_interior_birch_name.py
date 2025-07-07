import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product

try:
    # Find the existing product with the old name
    product = Product.objects.get(name='Plywood Birch Interior (MR)')
    
    # Update the name and slug
    product.name = 'Plywood Interior Birch'
    product.slug = slugify('Plywood Interior Birch')
    product.save()
    
    print('Product name updated successfully!')
    print(f'Old name: Plywood Birch Interior (MR)')
    print(f'New name: {product.name}')
    
except Product.DoesNotExist:
    print('Product "Plywood Birch Interior (MR)" not found. Creating new product...')
    
    # Run the creation script instead
    from products.models import Category, ProductSpecification
    
    # Get or create the plywood category
    category, created = Category.objects.get_or_create(
        name='Plywood',
        defaults={'slug': 'plywood', 'description': 'High-quality plywood for construction and building needs'}
    )
    
    # Create the new product
    product = Product.objects.create(
        name='Plywood Interior Birch',
        slug=slugify('Plywood Interior Birch'),
        description='Plywood "Birch Interior" is a brand of MR birch plywood for indoor applications. It is an environmentally friendly material due to the usage of a glue based on urea-formaldehyde resin. The alternation of cross and long grain veneer eliminates the chances of the plywood deformation and cracking.',
        price=40.00,
        category=category,
        wood_species='birch',
        wood_type='',
        thickness='4, 6, 8, 9, 10, 11, 12, 14, 15, 17, 18, 20, 21, 24, 25, 30 mm',
        grade='1/2 (B/BB), 2/2 (BB/BB), 2/3 (BB/CP), 2/4 (BB/C), 3/3 (CP/CP), 3/4 (CP/C), 4/4 (C/C)',
        finish='Not-sanded (NS) and both sides sanded (S2)',
        in_stock=True,
        stock_quantity=200,
        featured=True,
        meta_description='MR birch plywood for indoor applications. Environmentally friendly with urea-formaldehyde resin. Perfect for furniture and interior use.'
    )
    
    # Add specifications
    specifications = [
        ('Sizes, mm', '1525x1525, cut-to-size'),
        ('Grades', '1/2 (B/BB), 2/2 (BB/BB), 2/3 (BB/CP), 2/4 (BB/C), 3/3 (CP/CP), 3/4 (CP/C), 4/4 (C/C)'),
        ('Type of surface', 'not-sanded (NS) and both sides sanded (S2)'),
        ('Formaldehyde emission (limit value 3.5 mg/h x m²)', '0.1-0.3 mg/h x m²'),
        ('Moisture resistance', 'MR (Moisture Resistant) - urea-formaldehyde resin'),
        ('Application', 'Indoor applications - furniture, interior decoration, packaging'),
        ('Environmental status', 'Environmentally friendly material'),
        ('Advantages', 'High strength and durability, Safe for human health and the environment, Light weight, Wide range of thicknesses and sizes, Beautiful texture of birch wood')
    ]
    
    for spec_name, spec_value in specifications:
        ProductSpecification.objects.create(
            product=product,
            name=spec_name,
            value=spec_value
        )
    
    print('New product created successfully!')
    print(f'Product name: {product.name}')
