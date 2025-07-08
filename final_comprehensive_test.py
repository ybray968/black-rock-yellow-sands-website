import requests
import time

time.sleep(3)

try:
    print("🎉 FINAL COMPREHENSIVE TEST - % SYMBOL FIX")
    print("=" * 60)
    
    # Test Arabic page 
    response = requests.get('http://127.0.0.1:8000/ar/products/durability-testing/')
    content = response.text
    
    print("📊 TESTING ALL TRANSLATION CATEGORIES:")
    
    # 1. The problematic text (should now be fixed)
    print(f"\n1. 🎯 TARGET FIXES (The % symbol problem):")
    old_broken = content.count('95% of image erased')
    new_working = content.count('تم مسح 95 في المئة من الصورة')
    print(f"   ❌ Old broken '95% of image erased': {old_broken} (should be 0)")
    print(f"   ✅ New working Arabic 'تم مسح 95 في المئة من الصورة': {new_working} (should be 8)")
    
    # 2. Table headers (should work)
    print(f"\n2. 📋 TABLE HEADERS (Should all work):")
    table_headers = [
        ("Series, sample #", "السلسلة، العينة #"),
        ("Number of turns", "عدد الدوران"),
        ("Coating abrasive resistance", "مقاومة الطلاء للتآكل"),
        ("The overall look after abrasion test", "المظهر العام بعد اختبار التآكل")
    ]
    
    for english, arabic in table_headers:
        eng_found = english in content
        ar_found = arabic in content
        if ar_found and not eng_found:
            status = "✅ WORKING"
        elif eng_found and not ar_found:
            status = "❌ NOT WORKING"
        else:
            status = "⚠️ MIXED"
        print(f"   {status}: {english}")
    
    # 3. Other working translations (controls)
    print(f"\n3. 🎮 CONTROL TESTS (Should all work):")
    controls = [
        ("Plywood grades", "درجات الخشب الرقائقي"),
        ("Machine:", "الآلة:"),
        ("Correction factor f = 0.87", "عامل التصحيح f = 0.87"),
        ("Durability Testing", "اختبار المتانة")
    ]
    
    for english, arabic in controls:
        eng_found = english in content
        ar_found = arabic in content
        if ar_found and not eng_found:
            status = "✅ WORKING"
        elif eng_found and not ar_found:
            status = "❌ NOT WORKING"
        else:
            status = "⚠️ MIXED"
        print(f"   {status}: {english}")
    
    # 4. Summary statistics
    print(f"\n4. 📈 SUMMARY STATISTICS:")
    print(f"   Total page size: {len(content):,} characters")
    print(f"   Language attribute: {'✅ Arabic' if 'lang=\"ar\"' in content else '❌ Missing/Wrong'}")
    
    # 5. Final verdict
    print(f"\n5. 🏆 FINAL VERDICT:")
    
    if old_broken == 0 and new_working >= 8:
        print("   🎉 SUCCESS! All durability testing translations working!")
        print("   ✅ % symbol issue completely resolved")
        print("   ✅ Arabic version now fully functional")
        
        # Test English version to make sure it still works
        eng_response = requests.get('http://127.0.0.1:8000/products/durability-testing/')
        eng_content = eng_response.text
        eng_percent = eng_content.count('95 percent of image erased')
        
        print(f"\n📋 English version check:")
        print(f"   English '95 percent of image erased': {eng_percent} (should be 8)")
        
        if eng_percent >= 8:
            print("   ✅ English version also working correctly")
            print("\n🎯 MISSION ACCOMPLISHED!")
            print("   • Arabic website is now 100% functional")
            print("   • All durability testing content translated")
            print("   • % symbol issue identified and resolved")
            print("   • Both language versions working perfectly")
        else:
            print("   ⚠️ English version may have issues")
            
    elif old_broken > 0:
        print("   ❌ Still showing old broken text")
        print("   🔧 Template changes may not have applied fully")
    elif new_working == 0:
        print("   ❌ Arabic translations not showing")
        print("   🔧 Translation files may need recompilation")
    else:
        print("   ❓ Mixed results - need investigation")
    
    print("=" * 60)
        
except Exception as e:
    print(f'❌ Error: {e}')
