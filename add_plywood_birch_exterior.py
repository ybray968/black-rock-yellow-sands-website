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

# Get or create the Plywood Birch Exterior product
product, created = Product.objects.get_or_create(
        name="Plywood Exterior Birch (WBP)",
    defaults={
        'slug': slugify('Plywood Birch Exterior WBP'),
        'description': 'Plywood "Birch Exterior" is a brand of WBP birch plywood. It has increased water resistance due to the usage of a glue based on phenol-formaldehyde resin. Plywood Birch Exterior is made of 100% birch veneer and thus has such properties as high strength, durability, low weight and high performance. The plywood can be overlaid with HPL (high-pressure laminate) or fiberglass.\n\nWBP plywood can be used for many purposes including construction, shipbuilding, exterior and interior decoration works, commercial vehicles production, carriage building, packaging, sheathing, flooring, parquet manufacturing. Can be overlaid with protective and decorative HPL coating, dark brown phenolic film or modified UV resistant phenolic film available in different colors.',
        'price': 55.00,
        'category': category,
        'wood_species': 'birch',
        'wood_type': '',
        'thickness': '4, 6, 6.5, 8, 9, 10, 12, 15, 16, 18, 19, 21, 24, 27, 30, 35, 40 mm',
        'grade': '1/2 (B/BB), 2/2 (BB/BB), 2/3 (BB/CP), 2/4 (BB/C), 3/3 (CP/CP), 3/4 (CP/C)',
        'finish': 'Not-sanded (NS) and both sides sanded (S2), overlaid with HPL, fiberglass',
        'in_stock': True,
        'stock_quantity': 150,
        'featured': True,
        'meta_description': 'WBP birch plywood with increased water resistance and CARB ULEF status. Safe formaldehyde emission levels for construction use.'
    }
)

# Update the description if the product already exists
if not created:
    product.description = 'Plywood "Birch Exterior" is a brand of WBP birch plywood. It has increased water resistance due to the usage of a glue based on phenol-formaldehyde resin. Plywood Birch Exterior is made of 100% birch veneer and thus has such properties as high strength, durability, low weight and high performance. The plywood can be overlaid with HPL (high-pressure laminate) or fiberglass.\n\nWBP plywood can be used for many purposes including construction, shipbuilding, exterior and interior decoration works, commercial vehicles production, carriage building, packaging, sheathing, flooring, parquet manufacturing. Can be overlaid with protective and decorative HPL coating, dark brown phenolic film or modified UV resistant phenolic film available in different colors.'
    product.save()
    print('Plywood Birch Exterior product description updated successfully!')

if created:
    print('Plywood Birch Exterior product added successfully!')
    
    # Add detailed specifications (thickness first)
    specifications = [
        ('Thicknesses', 'السماكات', '4, 6, 6.5, 8, 9, 10, 12, 15, 16, 18, 19, 21, 24, 27, 30, 35, 40 mm', ''),
        ('Sizes, mm', 'الأحجام، مم', '2440x1220 or 1220x2440; 1250x2500 or 2500x1250; 1525x1525; 1500x3000; 1525x3050, cut-to-size', ''),
        ('Grades', 'الدرجات', '1/2 (B/BB), 2/2 (BB/BB), 2/3 (BB/CP), 2/4 (BB/C), 3/3 (CP/CP), 3/4 (CP/C)', ''),
        ('Type of surface', 'نوع السطح', 'not-sanded (NS) and both sides sanded (S2), overlaid with HPL, fiberglass', ''),
        ('Formaldehyde emission (limit value 3.5 mg/h x m²)', 'انبعاث الفورمالديهايد (القيمة الحدية 3.5 مغ/س × م²)', '0.1-0.3 mg/h x m²', ''),
        ('Water resistance', 'مقاومة الماء', 'WBP (Weather and Boil Proof) - phenol-formaldehyde resin', ''),
        ('CARB status', 'حالة CARB', 'ULEF (Ultra Low Emitting Formaldehyde)', ''),
        ('Advantages', 'المزايا', 'Excellent bonding properties, Resistance to moisture impact, Wide range of thicknesses and sizes, Exceptional durability, Easy to use and process', '')
    ]
    
    for spec_name, spec_name_ar, spec_value, spec_value_ar in specifications:
        ProductSpecification.objects.create(
            product=product,
            name=spec_name,
            name_ar=spec_name_ar,
            value=spec_value,
            value_ar=spec_value_ar
        )
    
    print('Product specifications added successfully!')
else:
    print('Plywood Birch Exterior product already exists.')
