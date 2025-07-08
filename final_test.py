import requests
import time

# Give server a moment to start  
time.sleep(3)

try:
    print("=== FINAL TRANSLATION TEST ===")
    
    # Test Arabic version
    print("\n🔍 Testing Arabic page...")
    arabic_response = requests.get('http://127.0.0.1:8000/ar/products/durability-testing/')
    english_count = arabic_response.text.count('95% of image erased')
    arabic_count = arabic_response.text.count('تم مسح ٩٥٪ من الصورة')
    
    print(f"Arabic page (http://127.0.0.1:8000/ar/products/durability-testing/):")
    print(f"  ❌ English '95% of image erased': {english_count}")
    print(f"  ✅ Arabic 'تم مسح ٩٥٪ من الصورة': {arabic_count}")
    
    # Test English version
    print("\n🔍 Testing English page...")
    english_response = requests.get('http://127.0.0.1:8000/products/durability-testing/')
    english_en_count = english_response.text.count('95% of image erased')
    
    print(f"English page (http://127.0.0.1:8000/products/durability-testing/):")
    print(f"  ✅ English '95% of image erased': {english_en_count}")
    
    # Final verdict
    print("\n📊 RESULTS:")
    if english_count == 0 and arabic_count > 0 and english_en_count > 0:
        print("🎉 SUCCESS! Translation working perfectly!")
        print("   ✅ Arabic page shows Arabic text")
        print("   ✅ English page shows English text")
        print("   ✅ No cross-contamination")
    elif english_count == 0 and arabic_count > 0:
        print("🎯 Arabic translation working!")
        print("   ✅ Arabic page shows Arabic text")
        print("   ❓ Need to verify English page")
    elif english_count > 0:
        print("❌ ISSUE: Arabic page still showing English text")
        print("   🔧 Translation not being applied")
    else:
        print("❓ UNCLEAR: Mixed or unexpected results")
        
except Exception as e:
    print(f'❌ Error: {e}')
