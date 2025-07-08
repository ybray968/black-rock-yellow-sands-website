#!/usr/bin/env python3
"""
Script to update English specification values and add Arabic translations
"""

import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import ProductSpecification

def update_english_values():
    """Update specific English values as requested"""
    print("Updating English specification values...")
    
    # 1. Change "cut-to-size" to "custom size"
    specs_with_cut_to_size = ProductSpecification.objects.filter(value__icontains='cut-to-size')
    for spec in specs_with_cut_to_size:
        old_value = spec.value
        spec.value = spec.value.replace('cut-to-size', 'custom size')
        spec.save()
        print(f"Updated: {old_value} -> {spec.value}")
    
    # 2. Change "not-sanded" to "not sanded"
    specs_with_not_sanded = ProductSpecification.objects.filter(value__icontains='not-sanded')
    for spec in specs_with_not_sanded:
        old_value = spec.value
        spec.value = spec.value.replace('not-sanded', 'not sanded')
        spec.save()
        print(f"Updated: {old_value} -> {spec.value}")

def add_arabic_translations():
    """Add Arabic translations for specification values"""
    print("\nAdding Arabic translations for specification values...")
    
    # Dictionary of English to Arabic translations
    VALUE_TRANSLATIONS = {
        # 1. Custom size translation
        'custom size': 'مقاس مخصص',
        
        # 2. Not sanded translation
        'not sanded (NS) and both sides sanded (S2)': 'غير مصنفر (NS) وكلا الجانبين مصنفر (S2)',
        'not sanded (NS) and both sides sanded (S2), overlaid with HPL': 'غير مصنفر (NS) وكلا الجانبين مصنفر (S2)، مغطى بـ HPL',
        'not sanded (NS) and both sides sanded (S2), overlaid with HPL, fiberglass': 'غير مصنفر (NS) وكلا الجانبين مصنفر (S2)، مغطى بـ HPL، ألياف زجاجية',
        'not sanded (NS) and both sides sanded (S2), overlaid with HPL, fiberglass, resin coated': 'غير مصنفر (NS) وكلا الجانبين مصنفر (S2)، مغطى بـ HPL، ألياف زجاجية، مطلي بالراتنج',
        
        # 3. ULEF translation
        'ULEF (Ultra Low Emitting Formaldehyde)': 'ULEF (فورمالديهايد منخفض الانبعاث للغاية)',
        
        # 4. Multi-property descriptions
        'Excellent bonding properties, Resistance to moisture impact, Wide range of thicknesses and sizes, Exceptional durability, Easy to use and process': 'خصائص ربط ممتازة، مقاومة تأثير الرطوبة، مجموعة واسعة من السماكات والأحجام، متانة استثنائية، سهل الاستخدام والمعالجة',
        
        # Surface treatments
        'Both sides sanded (S2)': 'كلا الجانبين مصنفر (S2)',
        
        # Surface types
        'smooth/hexagonal (F/H)': 'أملس/سداسي (F/H)',
        'smooth/smooth (F/F)': 'أملس/أملس (F/F)',
        'smooth/wire (F/W)': 'أملس/سلكي (F/W)',
        
        # Applications and descriptions
        'Indoor applications - furniture, interior decoration, packaging': 'التطبيقات الداخلية - الأثاث، الديكور الداخلي، التعبئة والتغليف',
        'Transport industry, interior decoration, construction': 'صناعة النقل، الديكور الداخلي، البناء',
        'Heavy-duty commercial transport floors, construction, packaging': 'أرضيات النقل التجاري الثقيل، البناء، التعبئة والتغليف',
        'Shipbuilding, railcar building, construction': 'بناء السفن، بناء العربات، البناء',
        
        # Material properties
        'High strength and durability, Safe for human health and the environment, Light weight, Wide range of thicknesses and sizes, Beautiful texture of birch wood': 'قوة ومتانة عالية، آمن لصحة الإنسان والبيئة، وزن خفيف، مجموعة واسعة من السماكات والأحجام، ملمس جميل لخشب البتولا',
        'Enhanced strength properties with solid veneer option in inner layers': 'خصائص قوة محسنة مع خيار القشرة الصلبة في الطبقات الداخلية',
        'Improved moisture resistance for flooring applications': 'مقاومة محسنة للرطوبة لتطبيقات الأرضيات',
        'Strict thickness control for parquet manufacturing requirements': 'تحكم صارم في السماكة لمتطلبات تصنيع الباركيه',
        'Comprehensive quality control with detailed defect specifications': 'مراقبة جودة شاملة مع مواصفات مفصلة للعيوب',
        'Consistent color quality for premium appearance': 'جودة لون ثابتة للمظهر المتميز',
        'Environmentally friendly material': 'مادة صديقة للبيئة',
        
        # Technical specifications
        'Fire-resistance properties with flame-retardant compound': 'خصائص مقاومة الحريق مع مركب مثبط للهب',
        'Meets strictest fire safety requirements': 'يلبي أصرم متطلبات السلامة من الحريق',
        'No additional processing required during cutting': 'لا حاجة لمعالجة إضافية أثناء القطع',
        
        # Overlay descriptions
        'Decorative HPL or fiberglass overlay available': 'متوفر طلاء HPL أو ألياف زجاجية ديكوري',
        'Decorative hexagonal surface combining functionality and aesthetics': 'سطح سداسي زخرفي يجمع بين الوظيفة والجماليات',
        'Phenolic film overlay with hexagonal antislip pattern': 'طلاء فيلم فينولي مع نمط سداسي مضاد للانزلاق',
        'Phenolic film overlay with wire-mesh antislip surface': 'طلاء فيلم فينولي مع سطح شبكي سلكي مضاد للانزلاق',
        
        # Sound and weight options
        'Cork layer - lighter weight; Rubber layer - higher noise insulation': 'طبقة فلين - وزن أخف؛ طبقة مطاط - عزل ضوضاء أعلى',
        'Technical cork, rubber, or composite material made of cork and rubber crumbs': 'فلين تقني، مطاط، أو مادة مركبة مصنوعة من فتات الفلين والمطاط',
        
        # Protection and treatments
        'Acrylic paint to prevent moisture absorption': 'طلاء أكريليك لمنع امتصاص الرطوبة',
        
        # Resin types (keep abbreviations but translate descriptions)
        'MR (Moisture Resistant) - urea-formaldehyde resin': 'MR (مقاوم للرطوبة) - راتنج يوريا فورمالديهايد',
        'WBP (Weather and Boil Proof) - phenol-formaldehyde resin': 'WBP (مقاوم للطقس والغليان) - راتنج فينول فورمالديهايد',
        'WBP grade with flame-retardant compound impregnation': 'درجة WBP مع تشريب مركب مثبط للهب',
        'WBP grade with sound-absorbing material layer': 'درجة WBP مع طبقة مادة ماصة للصوت',
    }
    
    updated_count = 0
    
    for spec in ProductSpecification.objects.all():
        # Check for exact matches first
        if spec.value in VALUE_TRANSLATIONS and not spec.value_ar:
            spec.value_ar = VALUE_TRANSLATIONS[spec.value]
            spec.save()
            updated_count += 1
            print(f"Added Arabic: {spec.value[:50]}... -> {spec.value_ar[:50]}...")
        
        # Handle values containing "custom size" 
        elif 'custom size' in spec.value and not spec.value_ar:
            arabic_value = spec.value.replace('custom size', 'مقاس مخصص')
            spec.value_ar = arabic_value
            spec.save()
            updated_count += 1
            print(f"Added Arabic with custom size: {spec.value[:50]}... -> {spec.value_ar[:50]}...")
    
    print(f"\nCompleted! Added Arabic translations for {updated_count} specification values.")

def show_remaining_untranslated():
    """Show values that still need translation (excluding measurements and abbreviations)"""
    print("\nRemaining values that might need translation:")
    print("=" * 60)
    
    untranslated = ProductSpecification.objects.filter(value_ar='')
    unique_untranslated = set()
    
    for spec in untranslated:
        value = spec.value
        # Skip pure measurements, grades, and values with only abbreviations/numbers
        if not (value.replace(' ', '').replace(',', '').replace('mm', '').replace('x', '').replace('/', '').replace('(', '').replace(')', '').replace('-', '').replace('.', '').replace('²', '').replace('m', '').replace('h', '').replace('g', '').isdigit() or 
                len(value) < 10 or
                value.count('/') > 2):
            unique_untranslated.add(value)
    
    for value in sorted(unique_untranslated):
        print(f"- {value}")
    
    print(f"\nTotal unique values still needing translation: {len(unique_untranslated)}")

if __name__ == '__main__':
    update_english_values()
    add_arabic_translations()
    show_remaining_untranslated()
