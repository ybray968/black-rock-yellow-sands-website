import requests
import time

time.sleep(3)

try:
    print("🔍 TESTING BOTH OLD AND NEW TEXT")
    
    # Test Arabic page 
    response = requests.get('http://127.0.0.1:8000/ar/products/durability-testing/')
    content = response.text
    
    # Check for old text
    old_english = content.count('95% of image erased')
    old_arabic = content.count('تم مسح ٩٥٪ من الصورة')
    
    # Check for new text
    new_english = content.count('95% of the image was erased')
    new_arabic = content.count('تم مسح ٩٥٪ من الصورة')  # Same Arabic translation
    
    print(f"Old text '95% of image erased':")
    print(f"  English: {old_english} occurrences")
    print(f"  Arabic: Can't distinguish (same Arabic translation)")
    
    print(f"\nNew text '95% of the image was erased':")
    print(f"  English: {new_english} occurrences")
    print(f"  Arabic: Can't distinguish (same Arabic translation)")
    
    print(f"\nTotal Arabic occurrences: {old_arabic}")
    print(f"Total English occurrences: {old_english + new_english}")
    
    if old_arabic > 0:
        print("✅ Some Arabic translations are working!")
    else:
        print("❌ No Arabic translations found")
        
    if new_english == 0 and old_english > 0:
        print("🎯 NEW text is translated, OLD text is not!")
    elif new_english > 0 and old_english == 0:
        print("🎯 OLD text is translated, NEW text is not!")
    elif new_english == 0 and old_english == 0:
        print("🎉 BOTH texts are translated!")
    else:
        print("❌ BOTH texts are still in English")
        
except Exception as e:
    print(f'❌ Error: {e}')
