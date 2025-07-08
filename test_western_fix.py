import requests
import time

time.sleep(3)

try:
    print("🔍 TESTING IF WESTERN NUMERALS FIX THE PROBLEM")
    
    # Test Arabic page 
    response = requests.get('http://127.0.0.1:8000/ar/products/durability-testing/')
    content = response.text
    
    print("📊 Testing specific problematic translations:")
    
    tests = [
        # Our target translations with Western numerals
        ("95% of image erased", "تم مسح 95% من الصورة", "Table body with Western numerals"),
        ("95% of the image was erased", "تم مسح 95% من الصورة", "Modified table body with Western numerals"),
        ("Correction factor f = 0.87", "عامل التصحيح f = 0.87", "Footer with Western numerals"),
        
        # Control group that should still work
        ("Machine:", "الآلة:", "Control - should still work"),
        ("Plywood grades", "درجات الخشب الرقائقي", "Control - should still work")
    ]
    
    for english, arabic, description in tests:
        english_found = english in content
        arabic_found = arabic in content
        
        if arabic_found and not english_found:
            status = "🎉 SUCCESS - TRANSLATED!"
        elif english_found and not arabic_found:
            status = "❌ STILL NOT WORKING"
        elif english_found and arabic_found:
            status = "⚠️ BOTH VERSIONS FOUND"
        else:
            status = "❓ NEITHER FOUND"
            
        print(f"  {status}: {description}")
        print(f"    English: {'Found' if english_found else 'Not found'}")
        print(f"    Arabic:  {'Found' if arabic_found else 'Not found'}")
        print()
    
    # Count total occurrences
    total_95_english = content.count('95% of image erased') + content.count('95% of the image was erased')
    total_95_arabic = content.count('تم مسح 95% من الصورة')
    
    print(f"📊 Summary:")
    print(f"  Total English '95%' text: {total_95_english}")
    print(f"  Total Arabic '95%' text (Western numerals): {total_95_arabic}")
    
    if total_95_arabic > 0 and total_95_english == 0:
        print("🎉 BREAKTHROUGH! Western numerals fixed the problem!")
    elif total_95_arabic > 0 and total_95_english > 0:
        print("🔄 PARTIAL SUCCESS! Some translations working but not all")
    elif total_95_english > 0 and total_95_arabic == 0:
        print("❌ No improvement - still showing English")
    else:
        print("❓ Unclear result - need to investigate further")
        
except Exception as e:
    print(f'❌ Error: {e}')
