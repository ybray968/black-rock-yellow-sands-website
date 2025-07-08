#!/usr/bin/env python3
"""
Script to translate product specification names to Arabic
"""

import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import ProductSpecification

# Dictionary mapping English specification names to Arabic
SPEC_TRANSLATIONS = {
    'Advantages': 'المزايا',
    'Application': 'التطبيق',
    'CARB status': 'حالة CARB',
    'Complete absence of healthy color changes in B and BB grades': 'الغياب الكامل لتغيرات الألوان الصحية في درجات B و BB',
    'Design features': 'خصائص التصميم',
    'Edge sealing': 'إغلاق الحواف',
    'Environmental status': 'الحالة البيئية',
    'Extended list of putted defects in CP grade': 'قائمة مطولة بالعيوب المسموحة في درجة CP',
    'Film density': 'كثافة الفيلم',
    'Film density, g/m²': 'كثافة الفيلم، غ/م²',
    'Fire resistance': 'مقاومة الحريق',
    'Formaldehyde emission (limit value 3.5 mg/h x m²)': 'انبعاث الفورمالديهايد (القيمة الحدية 3.5 مغ/س × م²)',
    'Grades': 'الدرجات',
    'High strength and durability': 'قوة ومتانة عالية',
    'Moisture resistance': 'مقاومة الرطوبة',
    'Processing': 'المعالجة',
    'Resistance to moisture impact': 'مقاومة تأثير الرطوبة',
    'Safety compliance': 'الامتثال للسلامة',
    'Sizes': 'الأحجام',
    'Sizes, mm': 'الأحجام، مم',
    'Sound insulation': 'العزل الصوتي',
    'Sound-absorbing materials': 'المواد الماصة للصوت',
    'Special thickness tolerances': 'تفاوتات السماكة الخاصة',
    'Surface treatment': 'معالجة السطح',
    'Surface treatment options': 'خيارات معالجة السطح',
    'The formaldehyde emission (limit value 3.5 mg/h x m²)': 'انبعاث الفورمالديهايد (القيمة الحدية 3.5 مغ/س × م²)',
    'Thickness, mm': 'السماكة، مم',
    'Thicknesses': 'السماكات',
    'Thicknesses, mm': 'السماكات، مم',
    'Type of surface': 'نوع السطح',
    'Water resistance': 'مقاومة الماء',
    'Weight options': 'خيارات الوزن'
}

def translate_spec_names():
    """Translate specification names to Arabic"""
    print("Translating specification names to Arabic...")
    
    updated_count = 0
    
    for spec in ProductSpecification.objects.all():
        if spec.name in SPEC_TRANSLATIONS and not spec.name_ar:
            spec.name_ar = SPEC_TRANSLATIONS[spec.name]
            spec.save()
            updated_count += 1
            print(f"Updated: {spec.name} -> {spec.name_ar}")
    
    print(f"\nCompleted! Updated {updated_count} specification names.")
    
    # Show any untranslated specs
    untranslated = ProductSpecification.objects.filter(name_ar='')
    if untranslated.exists():
        print(f"\nSpecs still needing translation:")
        for spec in untranslated:
            print(f"- {spec.name}")

if __name__ == '__main__':
    translate_spec_names()
