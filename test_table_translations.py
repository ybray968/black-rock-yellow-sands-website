import requests
import time

time.sleep(3)

try:
    print("🔍 TESTING TABLE TRANSLATION PATTERNS")
    
    # Test Arabic page 
    response = requests.get('http://127.0.0.1:8000/ar/products/durability-testing/')
    content = response.text
    
    print("📊 Table header translations (SHOULD work):")
    header_tests = [
        ("Series, sample #", "رقم السلسلة والعينة"),
        ("Number of turns", "عدد الدورات"),
        ("Coating abrasive resistance", "مقاومة الطلاء للتآكل"),
        ("The overall look after abrasion test", "المظهر العام بعد اختبار التآكل")
    ]
    
    for english, arabic in header_tests:
        english_found = english in content
        arabic_found = arabic in content
        
        if arabic_found and not english_found:
            status = "✅ TRANSLATED"
        elif english_found and not arabic_found:
            status = "❌ NOT TRANSLATED"
        elif english_found and arabic_found:
            status = "⚠️ BOTH FOUND"
        else:
            status = "❓ NEITHER FOUND"
            
        print(f"  {status}: '{english}'")
    
    print("\n📊 Table body translations (PROBLEM AREA):")
    body_tests = [
        ("95% of image erased", "تم مسح ٩٥٪ من الصورة"),
        ("95% of the image was erased", "تم مسح ٩٥٪ من الصورة"),
        ("Correction factor f = 0.87", "عامل التصحيح f = 0.87")
    ]
    
    for english, arabic in body_tests:
        english_found = english in content
        arabic_found = arabic in content
        
        if arabic_found and not english_found:
            status = "✅ TRANSLATED"
        elif english_found and not arabic_found:
            status = "❌ NOT TRANSLATED"
        elif english_found and arabic_found:
            status = "⚠️ BOTH FOUND"
        else:
            status = "❓ NEITHER FOUND"
            
        print(f"  {status}: '{english}'")
        
    print("\n📊 Other page translations (CONTROL GROUP):")
    other_tests = [
        ("Machine:", "الآلة:"),
        ("Plywood grades", "درجات الخشب الرقائقي"),
        ("Durability Testing", "اختبار المتانة")
    ]
    
    for english, arabic in other_tests:
        english_found = english in content
        arabic_found = arabic in content
        
        if arabic_found and not english_found:
            status = "✅ TRANSLATED"
        elif english_found and not arabic_found:
            status = "❌ NOT TRANSLATED"
        elif english_found and arabic_found:
            status = "⚠️ BOTH FOUND"
        else:
            status = "❓ NEITHER FOUND"
            
        print(f"  {status}: '{english}'")
    
    print(f"\n🔍 Looking for patterns in HTML structure...")
    
    # Look for the table structure specifically
    if '<table' in content and '<tbody>' in content:
        print("✅ HTML table structure found")
    else:
        print("❌ HTML table structure missing")
        
    # Check if there are any JavaScript table manipulations
    if 'table' in content.lower() and 'script' in content.lower():
        print("⚠️ JavaScript and table elements both present - possible dynamic manipulation")
    
        
except Exception as e:
    print(f'❌ Error: {e}')
