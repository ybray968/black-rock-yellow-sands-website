import requests
import time

time.sleep(3)

try:
    print("🔍 TESTING SIMPLE TRANSLATION")
    
    # Test Arabic durability testing page
    response = requests.get('http://127.0.0.1:8000/ar/products/durability-testing/')
    content = response.text
    
    # Test some translations that should definitely work
    tests = [
        ("Durability Testing", "اختبار المتانة", "Page title"),
        ("Products", "منتجات", "Products menu"), 
        ("Machine:", "الآلة:", "Test info"),
        ("Plywood grades", "درجات الخشب الرقائقي", "Section header"),
        ("95% of image erased", "تم مسح ٩٥٪ من الصورة", "Target translation")
    ]
    
    print(f"Content length: {len(content)} characters")
    print("Translation test results:")
    
    for english, arabic, description in tests:
        english_found = english in content
        arabic_found = arabic in content
        
        if arabic_found:
            status = "✅ WORKING"
        elif english_found:
            status = "❌ NOT TRANSLATED"
        else:
            status = "❓ NOT FOUND"
            
        print(f"  {status}: {description}")
        print(f"    English '{english}': {'Found' if english_found else 'Not found'}")
        print(f"    Arabic  '{arabic}': {'Found' if arabic_found else 'Not found'}")
        print()
    
    # Check language attribute
    if 'lang="ar"' in content:
        print("✅ Page has correct Arabic lang attribute")
    else:
        print("❌ Page missing Arabic lang attribute")
        
    # Check if templates are cached
    if 'Template cache' in content:
        print("⚠️  Template caching detected")
    
except Exception as e:
    print(f'❌ Error: {e}')
