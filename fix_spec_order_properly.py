import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product, ProductSpecification

# Fix the order of specifications for the three products
products_to_fix = {
    'Plywood Deck (Construction Use)': [
        ('Thicknesses', 'السماكات', '6.5, 9, 12, 15, 16, 18, 19, 21, 24, 27, 30, 35, 40 mm', ''),
        ('Sizes, mm', 'الأحجام، مم', '2440x1220 or 1220x2440; 1250x2500 or 2500x1250; 1525x1525; 1525x3050, custom size', ''),
        ('Grades', 'الدرجات', '1/1 (B/B)', ''),
        ('Type of surface', 'نوع السطح', 'smooth/smooth (F/F)', ''),
        ('Film density, g/m²', 'كثافة الفيلم، غ/م²', '120/120, 120/220, 220/220', ''),
        ('Formaldehyde emission (limit value 3.5 mg/h x m²)', 'انبعاث الفورمالديهايد (القيمة الحدية 3.5 مغ/س × م²)', '0.1-0.3 mg/h x m²', ''),
    ],
    'Plywood Interior Birch': [
        ('Thicknesses', 'السماكات', '4, 6, 8, 9, 10, 11, 12, 14, 15, 17, 18, 20, 21, 24, 25, 30 mm', ''),
        ('Sizes, mm', 'الأحجام، مم', '1525x1525, custom size', ''),
        ('Grades', 'الدرجات', '1/2 (B/BB), 2/2 (BB/BB), 2/3 (BB/CP), 2/4 (BB/C), 3/3 (CP/CP), 3/4 (CP/C), 4/4 (C/C)', ''),
        ('Type of surface', 'نوع السطح', 'not sanded (NS) and both sides sanded (S2)', ''),
        ('Formaldehyde emission (limit value 3.5 mg/h x m²)', 'انبعاث الفورمالديهايد (القيمة الحدية 3.5 مغ/س × م²)', '0.1-0.3 mg/h x m²', ''),
        ('Moisture resistance', 'مقاومة الرطوبة', 'MR (Moisture Resistant) - urea-formaldehyde resin', ''),
        ('Application', 'التطبيق', 'Indoor applications - furniture, interior decoration, packaging', ''),
        ('Environmental status', 'الحالة البيئية', 'Environmentally friendly material', ''),
        ('Advantages', 'المزايا', 'High strength and durability, Safe for human health and the environment, Light weight, Wide range of thicknesses and sizes, Beautiful texture of birch wood', ''),
    ],
    'Plywood Exterior Birch (WBP)': [
        ('Thicknesses', 'السماكات', '4, 6, 6.5, 8, 9, 10, 12, 15, 16, 18, 19, 21, 24, 27, 30, 35, 40 mm', ''),
        ('Sizes, mm', 'الأحجام، مم', '2440x1220 or 1220x2440; 1250x2500 or 2500x1250; 1525x1525; 1500x3000; 1525x3050, custom size', ''),
        ('Grades', 'الدرجات', '1/2 (B/BB), 2/2 (BB/BB), 2/3 (BB/CP), 2/4 (BB/C), 3/3 (CP/CP), 3/4 (CP/C)', ''),
        ('Type of surface', 'نوع السطح', 'not sanded (NS) and both sides sanded (S2), overlaid with HPL, fiberglass', ''),
        ('Formaldehyde emission (limit value 3.5 mg/h x m²)', 'انبعاث الفورمالديهايد (القيمة الحدية 3.5 مغ/س × م²)', '0.1-0.3 mg/h x m²', ''),
        ('Water resistance', 'مقاومة الماء', 'WBP (Weather and Boil Proof) - phenol-formaldehyde resin', ''),
        ('CARB status', 'حالة CARB', 'ULEF (Ultra Low Emitting Formaldehyde)', ''),
        ('Advantages', 'المزايا', 'Excellent bonding properties, Resistance to moisture impact, Wide range of thicknesses and sizes, Exceptional durability, Easy to use and process', ''),
    ]
}

print('🔧 FIXING SPECIFICATION ORDER PROPERLY')
print('=' * 60)

for product_name, specifications in products_to_fix.items():
    try:
        product = Product.objects.get(name=product_name)
        print(f'\n📦 Processing: {product.name}')
        
        # Delete all existing specifications
        ProductSpecification.objects.filter(product=product).delete()
        print(f'   🗑️  Deleted all existing specifications')
        
        # Create specifications in correct order
        for name, name_ar, value, value_ar in specifications:
            ProductSpecification.objects.create(
                product=product,
                name=name,
                name_ar=name_ar,
                value=value,
                value_ar=value_ar
            )
        
        print(f'   ✅ Created {len(specifications)} specifications in correct order')
        
        # Verify new order
        specs_updated = ProductSpecification.objects.filter(product=product).order_by('id')
        print(f'   📋 Final order:')
        for i, spec in enumerate(specs_updated, 1):
            print(f'      {i}. {spec.name}: {spec.value}')
        
    except Product.DoesNotExist:
        print(f'   ❌ Product "{product_name}" not found!')

print('\n' + '=' * 60)
print('✅ SPECIFICATION ORDER FIXED PROPERLY FOR ALL PRODUCTS')
