from products.models import ProductSpecification, Product

product = Product.objects.get(name='Primed Plywood')

# Clear existing specifications
product.specifications.all().delete()

specifications = [
    ("Thicknesses, mm", "6.5, 9, 12, 15, 18, 19, 21, 24, 27, 30, 35, 40", "السماكات، مم", "6.5، 9، 12، 15، 18، 19، 21، 24، 27، 30، 35، 40"),
    ("Sizes, mm", "2440x1220 or 1220x2440; 1250x2500 or 2500x1250; 1525x1525; 1500x3000; 1525x3050, cut-to-size", "الأحجام، مم", "2440x1220 أو 1220x2440؛ 1250x2500 أو 2500x1250؛ 1525x1525؛ 1500x3000؛ 1525x3050، قطع حسب المقاس"),
    ("Grades", "1/1 (B/B)", "الدرجات", "1/1 (B/B)"),
    ("Type of surface", "smooth/smooth (F/F)", "نوع السطح", "ناعم/ناعم (F/F)"),
    ("Film density, g/m²", "140, 220", "كثافة الفيلم، غ/م²", "140، 220"),
    ("The formaldehyde emission (limit value 3.5 mg/h x m²)", "0.1-0.3 mg/h x m²", "انبعاث الفورمالديهايد (القيمة الحدية 3.5 مغ/ساعة × م²)", "0.1-0.3 مغ/ساعة × م²"),
]

for spec_name, spec_value, spec_name_ar, spec_value_ar in specifications:
    ProductSpecification.objects.create(
        product=product,
        name=spec_name,
        value=spec_value,
        name_ar=spec_name_ar,
        value_ar=spec_value_ar
    )
    print(f"Added specification: {spec_name}")

print(f"Successfully added {len(specifications)} specifications to Primed Plywood!")
