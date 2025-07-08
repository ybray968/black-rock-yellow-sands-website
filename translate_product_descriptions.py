#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

from products.models import Product

def translate_product_descriptions():
    """Add Arabic descriptions to existing products using dedicated Arabic fields"""
    
    print("🔄 Adding Arabic descriptions to products...")
    print("="*60)
    
    # 1. Plywood Deck (Construction Use)
    try:
        deck = Product.objects.get(name='Plywood Deck (Construction Use)')
        arabic_desc = '''Plywood "Deck" هو علامة تجارية من الخشب الرقائقي البتولا فائق المتانة للبناء المغطى من الجانبين بفيلم ورق فينولي عالي الكثافة. الفيلم الأملس المتين المشرب براتنج الفينول-فورمالديهايد يجعل الخشب الرقائقي البتولا أكثر مقاومة للأضرار الميكانيكية وامتصاص الرطوبة وأشعة الشمس. الخشب الرقائقي عالي المقاومة للتآكل مثالي لأعمال الخرسانة وصناديق الهياكل. يمكن استخدامه في 50 دورة من أعمال الأسمنت في المتوسط'''
        deck.description_ar = arabic_desc
        deck.save()
        print("✅ 1. Plywood Deck - Arabic description updated")
    except Exception as e:
        print(f"❌ Error updating Plywood Deck: {e}")
    
    # 2. Plywood Exterior Birch (WBP)
    try:
        exterior = Product.objects.get(name='Plywood Exterior Birch (WBP)')
        arabic_desc = '''Plywood Exterior Birch هو علامة تجارية من الخشب الرقائقي البتولا WBP. لديه مقاومة متزايدة للماء بسبب استخدام صمغ يعتمد على راتنج الفينول-فورمالديهايد. Plywood Exterior Birch مصنوع من 100% قشرة البتولا وبالتالي يتمتع بخصائص مثل القوة العالية والمتانة والوزن المنخفض والأداء العالي. يمكن تغطية الخشب الرقائقي بـ HPL (الصفائح عالية الضغط) أو الألياف الزجاجية.

يمكن استخدام الخشب الرقائقي WBP للعديد من الأغراض بما في ذلك البناء وبناء السفن وأعمال الديكور الخارجية والداخلية وإنتاج المركبات التجارية وبناء العربات والتعبئة والتغليف والأرضيات وتصنيع الباركيه. يمكن تغطيته بطلاء HPL الوقائي والزخرفي أو فيلم فينولي بني داكن أو فيلم فينولي معدل مقاوم للأشعة فوق البنفسجية متوفر بألوان مختلفة.'''
        exterior.description_ar = arabic_desc
        exterior.save()
        print("✅ 2. Plywood Exterior Birch (WBP) - Arabic description updated")
    except Exception as e:
        print(f"❌ Error updating Plywood Exterior Birch: {e}")

    # 3. Plywood Interior Birch
    try:
        interior = Product.objects.get(name='Plywood Interior Birch')
        arabic_desc = '''Plywood Interior Birch هو علامة تجارية من الخشب الرقائقي البتولا MR للتطبيقات الداخلية. إنه منتج صديق للبيئة مع انبعاثات فورمالديهايد منخفضة (CARB ULEF). بسبب قوامه الجميل وسهولة التعامل معه، فإن الخشب الرقائقي البتولا MR مثالي للديكور الداخلي وتصنيع الأثاث.'''
        interior.description_ar = arabic_desc
        interior.save()
        print("✅ 3. Plywood Interior Birch - Arabic description updated")
    except Exception as e:
        print(f"❌ Error updating Plywood Interior Birch: {e}")

    # 4. Plywood Parquet
    try:
        parquet = Product.objects.get(name='Plywood Parquet')
        arabic_desc = '''Plywood "Parquet" هو علامة تجارية من الخشب الرقائقي البتولا لتصنيع الباركيه مع تحمل سماكة صارم. لديها خصائص قوة محسنة بسبب استخدام خيار القشرة الصلبة. Plywood "Parquet" مقاوم لتأثير الرطوبة بسبب استخدام صمغ يعتمد على راتنج اليوريا-فورمالديهايد المقاوم للماء.'''
        parquet.description_ar = arabic_desc
        parquet.save()
        print("✅ 4. Plywood Parquet - Arabic description updated")
    except Exception as e:
        print(f"❌ Error updating Plywood Parquet: {e}")

    # 5. Plywood Shield
    try:
        shield = Product.objects.get(name='Plywood Shield')
        arabic_desc = '''خيار ألواح البتولا "Shield" العالية الجودة يدمج القشور الصلبة، مما تزيد من متانة اللوح. مناسب للاستخدامات التي تتطلب مقاومة الشكل والصلابة. الراتنج الفينولي محصن من الماء والكيماويات.'''
        shield.description_ar = arabic_desc
        shield.save()
        print("✅ 5. Plywood Shield - Arabic description updated")
    except Exception as e:
        print(f"❌ Error updating Plywood Shield: {e}")

    # 6. Plywood Shield Acu
    try:
        shield_acu = Product.objects.get(name='Plywood Shield Acu')
        arabic_desc = '''ويتميز بـ "Shield Acu" للبتولا بخصائص مضادة للانزلاق مع لعل سطح الألواح المميزة لا تعزز البنية فقط، بل توفر الأمان والراحة. يستخدم لأغلفة العربات والأرصفة.'''
        shield_acu.description_ar = arabic_desc
        shield_acu.save()
        print("✅ 6. Plywood Shield Acu - Arabic description updated")
    except Exception as e:
        print(f"❌ Error updating Plywood Shield Acu: {e}")

    # 7. Plywood Antislip HEX
    try:
        antislip_hex = Product.objects.get(name='Plywood Antislip HEX')
        arabic_desc = '''السطح المانعي الجديد من نوع "Antislip HEX" للبتولا يوفر مانع تمرير متفوق لحماية إضافية وعداء مستقر مزود بمقاومة للانزلاق.'''
        antislip_hex.description_ar = arabic_desc
        antislip_hex.save()
        print("✅ 7. Plywood Antislip HEX - Arabic description updated")
    except Exception as e:
        print(f"❌ Error updating Plywood Antislip HEX: {e}")

    # 8. Plywood Deco
    try:
        deco = Product.objects.get(name='Plywood Deco')
        arabic_desc = '''الديكورات الخشبية "Deco" ذات الطابع البتولى للفترة المتطورة لتضمين التصميم النهائي مع ربط خشونة الخروط بحداثة العصرية.'''
        deco.description_ar = arabic_desc
        deco.save()
        print("✅ 8. Plywood Deco - Arabic description updated")
    except Exception as e:
        print(f"❌ Error updating Plywood Deco: {e}")

    # 9. Plywood Antislip MT
    try:
        antislip_mt = Product.objects.get(name='Plywood Antislip MT')
        arabic_desc = '''علامة الأصلي حول "Antislip MT" للبتولا تطرح تطورات امن العمل. يُستخدم لمجموعة متنوعة من التطبيقات التي تحتاج منع الانزلاق للمزيد من الأمان.'''
        antislip_mt.description_ar = arabic_desc
        antislip_mt.save()
        print("✅ 9. Plywood Antislip MT - Arabic description updated")
    except Exception as e:
        print(f"❌ Error updating Plywood Antislip MT: {e}")

if __name__ == '__main__':
    translate_product_descriptions()
