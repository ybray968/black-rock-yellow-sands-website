import requests
import time

time.sleep(3)

try:
    print("🔍 TESTING % SYMBOL THEORY")
    
    # Test Arabic page 
    response = requests.get('http://127.0.0.1:8000/ar/products/durability-testing/')
    content = response.text
    
    print("📊 Testing different versions of the same meaning:")
    
    tests = [
        # Version with % symbol (problematic)
        ("95% of image erased", "❌ BROKEN (% symbol)"),
        
        # Version with word 'percent' (testing)
        ("95 percent of image erased", "🔄 TESTING (word percent)"),
        
        # Arabic translations
        ("تم مسح 95 في المئة من الصورة", "🔄 Arabic with word percent"),
        ("تم مسح 95% من الصورة", "❌ Arabic with % symbol"),
        
        # Working controls
        ("Image mostly erased", "✅ CONTROL (different text)"),
        ("عامل التصحيح f = 0.87", "✅ CONTROL (has = but no %)")
    ]
    
    print(f"1. TRANSLATION RESULTS:")
    for text, description in tests:
        found = text in content
        status = "FOUND" if found else "NOT FOUND"
        print(f"   {description}: {status}")
        if found and "Arabic" in description:
            print(f"      ✅ Arabic translation working!")
    
    # Count specific occurrences 
    print(f"\n2. OCCURRENCE COUNTS:")
    
    # English versions
    percent_symbol_eng = content.count('95% of image erased')
    percent_word_eng = content.count('95 percent of image erased') 
    
    # Arabic versions  
    percent_word_ar = content.count('تم مسح 95 في المئة من الصورة')
    percent_symbol_ar = content.count('تم مسح 95% من الصورة')
    
    print(f"   English '95% of image erased': {percent_symbol_eng}")
    print(f"   English '95 percent of image erased': {percent_word_eng}")
    print(f"   Arabic 'في المئة' (word percent): {percent_word_ar}")
    print(f"   Arabic '95%' (% symbol): {percent_symbol_ar}")
    
    # Check test marker
    test_marker = "(Test percent vs %)"
    marker_found = test_marker in content
    print(f"   Test marker found: {'✅' if marker_found else '❌'}")
    
    print(f"\n3. ANALYSIS:")
    
    if percent_word_ar > 0 and percent_word_eng == 0:
        print("🎉 BREAKTHROUGH! % SYMBOL WAS THE PROBLEM!")
        print("   ✅ 'percent' word version works perfectly")
        print("   💡 Django has issues with % symbol in translation strings")
    elif percent_word_eng > 0 and percent_word_ar == 0:
        print("❌ Still not working - problem is not the % symbol")
        print("   🔍 Issue is deeper than just the % character")
    elif percent_symbol_eng > 0:
        print("⚠️ Still showing % symbol version in English")
        print("   🔍 Need to investigate further")
    else:
        print("❓ Unclear results - need more investigation")
    
    # Final recommendation
    if percent_word_ar > 0:
        print(f"\n🎯 SOLUTION FOUND:")
        print(f"   Replace '95% of image erased' with '95 percent of image erased'")
        print(f"   This maintains the same meaning while avoiding Django translation issues")
        
except Exception as e:
    print(f'❌ Error: {e}')
