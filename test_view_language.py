import requests
import time

time.sleep(3)

try:
    print("🔍 TESTING VIEW LANGUAGE CONTEXT")
    
    # Test a simple page that we know has working translations
    print("\n1. Testing home page...")
    response = requests.get('http://127.0.0.1:8000/ar/')
    
    # Check if Products is translated on the Arabic home page  
    if 'منتجات' in response.text:  # Arabic for "Products"
        print("✅ Home page Arabic translation working")
    else:
        print("❌ Home page Arabic translation NOT working")
        if 'Products' in response.text:
            print("   Found English 'Products' on Arabic page")
    
    print("\n2. Testing products page...")
    response = requests.get('http://127.0.0.1:8000/ar/products/')
    
    # Check if "Back to Home" is translated 
    if 'العودة إلى الرئيسية' in response.text:  # Arabic for "Back to Home"
        print("✅ Products page Arabic translation working")
    else:
        print("❌ Products page Arabic translation NOT working")
        if 'Back to Home' in response.text:
            print("   Found English 'Back to Home' on Arabic page")
    
    print("\n3. Testing durability testing page...")
    response = requests.get('http://127.0.0.1:8000/ar/products/durability-testing/')
    
    # Check if the page title is translated correctly
    if 'اختبار المتانة' in response.text:  # Arabic for "Durability Testing"
        print("✅ Durability page title Arabic translation working")
    else:
        print("❌ Durability page title Arabic translation NOT working")
        
    # Check for other translations that should work
    if 'منتجات' in response.text:  # Products
        print("✅ Durability page has some Arabic translations working")
    else:
        print("❌ Durability page has NO Arabic translations working")
        
    # Check specifically for our problematic text
    if '95% of image erased' in response.text:
        print("❌ Found untranslated '95% of image erased'")
    
    if 'تم مسح ٩٥٪ من الصورة' in response.text:
        print("✅ Found translated Arabic text")
    else:
        print("❌ Did NOT find translated Arabic text")
        
except Exception as e:
    print(f'❌ Error: {e}')
