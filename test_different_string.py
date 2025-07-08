import requests
import time

time.sleep(3)

try:
    print("🔍 TESTING COMPLETELY DIFFERENT STRING")
    
    # Test Arabic page 
    response = requests.get('http://127.0.0.1:8000/ar/products/durability-testing/')
    content = response.text
    
    print("📊 Testing new string vs. problematic old string:")
    
    # Test our new string
    new_english = "Image mostly erased"
    new_arabic = "تم مسح معظم الصورة"
    
    # Test the old problematic string
    old_english = "95% of image erased"
    old_arabic = "تم مسح 95% من الصورة"  # Western numerals version
    
    print(f"1. NEW STRING TEST:")
    new_eng_found = new_english in content
    new_ar_found = new_arabic in content
    
    if new_ar_found and not new_eng_found:
        print(f"   🎉 SUCCESS: '{new_english}' is translated!")
    elif new_eng_found and not new_ar_found:
        print(f"   ❌ FAILED: '{new_english}' not translated")
    elif new_eng_found and new_ar_found:
        print(f"   ⚠️ MIXED: Both versions found")
    else:
        print(f"   ❓ UNCLEAR: Neither version found")
    
    print(f"2. OLD STRING TEST:")
    old_eng_found = old_english in content
    old_ar_found = old_arabic in content
    
    if old_ar_found and not old_eng_found:
        print(f"   🎉 SUCCESS: '{old_english}' is translated!")
    elif old_eng_found and not old_ar_found:
        print(f"   ❌ FAILED: '{old_english}' not translated")
    elif old_eng_found and old_ar_found:
        print(f"   ⚠️ MIXED: Both versions found")
    else:
        print(f"   ❓ UNCLEAR: Neither version found")
    
    # Check working control 
    print(f"3. CONTROL TEST (known working):")
    correction_eng = "Correction factor f = 0.87"
    correction_ar = "عامل التصحيح f = 0.87"
    
    corr_eng_found = correction_eng in content
    corr_ar_found = correction_ar in content
    
    if corr_ar_found and not corr_eng_found:
        print(f"   ✅ CONTROL WORKING: '{correction_eng}' is translated!")
    else:
        print(f"   ❌ CONTROL PROBLEM: '{correction_eng}' not working as expected")
    
    print(f"\n📊 SUMMARY:")
    print(f"  Test marker found: {'✅' if '(Test outside table)' in content else '❌'}")
    
    if new_ar_found and not old_ar_found:
        print(f"  🎯 BREAKTHROUGH: New string works, old string doesn't!")
        print(f"  💡 This confirms the issue is specific to '95% of image erased' string")
    elif new_ar_found and old_ar_found:
        print(f"  🎉 AMAZING: Both strings work now!")
        print(f"  💡 Problem might be completely resolved")
    elif not new_ar_found and not old_ar_found:
        print(f"  ❌ CONCERNING: Neither string works")
        print(f"  💡 Problem is broader than just specific strings")
    else:
        print(f"  ❓ UNCLEAR: Mixed results need investigation")
        
except Exception as e:
    print(f'❌ Error: {e}')
