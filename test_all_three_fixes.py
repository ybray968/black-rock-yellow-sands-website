import requests
import time

time.sleep(3)

try:
    print("🔧 TESTING ALL THREE FIXES")
    print("=" * 60)
    
    # Test Arabic page 
    response = requests.get('http://127.0.0.1:8000/ar/products/durability-testing/')
    content = response.text
    
    print("📊 TESTING EACH FIX:")
    
    # Fix 1: "95% of the image was erased" -> "95 percent of the image was erased"
    print(f"\n1. 🎯 FIX 1: Alternative percent version")
    old_percent_broken = content.count('95% of the image was erased')
    new_percent_working = content.count('95 percent of the image was erased')
    arabic_percent_alt = content.count('تم مسح 95 في المئة من الصورة')
    
    print(f"   ❌ Old broken '95% of the image was erased': {old_percent_broken} (should be 0)")
    print(f"   ✅ New English '95 percent of the image was erased': {new_percent_working} (should be 0 on Arabic page)")
    print(f"   ✅ Arabic translation: {arabic_percent_alt} (should be >0)")
    
    if old_percent_broken == 0 and arabic_percent_alt > 0:
        print("   🎉 FIX 1 SUCCESS!")
    else:
        print("   ❌ FIX 1 NEEDS WORK")
    
    # Fix 2: Plywood Deck cycles text
    print(f"\n2. 🎯 FIX 2: Plywood Deck cycles translation")
    deck_eng = content.count('On average, Plywood Deck can be used in 50 cycles of cement pouring')
    deck_ar = content.count('في المتوسط، يمكن استخدام الخشب الرقائقي الدك في 50 دورة من صب الأسمنت')
    
    print(f"   ❌ English version: {deck_eng} (should be 0 on Arabic page)")
    print(f"   ✅ Arabic version: {deck_ar} (should be 1)")
    
    if deck_eng == 0 and deck_ar == 1:
        print("   🎉 FIX 2 SUCCESS!")
    else:
        print("   ❌ FIX 2 NEEDS WORK")
    
    # Fix 3: Test text removal
    print(f"\n3. 🎯 FIX 3: Test text removal")
    test_marker = "(Test percent vs %)"
    marker_found = test_marker in content
    
    print(f"   Test marker '(Test percent vs %)': {'FOUND' if marker_found else 'NOT FOUND'}")
    
    if not marker_found:
        print("   🎉 FIX 3 SUCCESS! Test text removed")
    else:
        print("   ❌ FIX 3 NEEDS WORK - test text still present")
    
    # Overall table check
    print(f"\n4. 📋 OVERALL TABLE CHECK:")
    total_old_broken = content.count('95% of image erased') + content.count('95% of the image was erased')
    total_new_working = content.count('تم مسح 95 في المئة من الصورة')
    
    print(f"   Total broken % symbol text: {total_old_broken} (should be 0)")
    print(f"   Total working Arabic text: {total_new_working} (should be 8)")
    
    # Test English version to make sure it's not broken
    print(f"\n5. 🎮 ENGLISH VERSION CHECK:")
    eng_response = requests.get('http://127.0.0.1:8000/products/durability-testing/')
    eng_content = eng_response.text
    
    eng_percent_count = eng_content.count('95 percent of image erased') + eng_content.count('95 percent of the image was erased')
    eng_deck_count = eng_content.count('On average, Plywood Deck can be used in 50 cycles of cement pouring')
    
    print(f"   English 'percent' versions: {eng_percent_count} (should be 8)")
    print(f"   English deck text: {eng_deck_count} (should be 1)")
    
    # Final verdict
    print(f"\n6. 🏆 FINAL VERDICT:")
    
    all_fixes_working = (
        old_percent_broken == 0 and arabic_percent_alt > 0 and  # Fix 1
        deck_eng == 0 and deck_ar == 1 and                     # Fix 2 
        not marker_found and                                    # Fix 3
        total_old_broken == 0 and total_new_working >= 8 and   # Overall
        eng_percent_count >= 8 and eng_deck_count == 1         # English check
    )
    
    if all_fixes_working:
        print("   🎉 ALL FIXES SUCCESSFUL!")
        print("   ✅ % symbol issue completely resolved")
        print("   ✅ All translations working in Arabic")
        print("   ✅ English version preserved")
        print("   ✅ Test content cleaned up")
        print("\n🎯 DURABILITY TESTING PAGE IS 100% COMPLETE!")
    else:
        print("   ⚠️ Some fixes may need attention")
        print("   🔧 Review individual fix results above")
    
    print("=" * 60)
        
except Exception as e:
    print(f'❌ Error: {e}')
