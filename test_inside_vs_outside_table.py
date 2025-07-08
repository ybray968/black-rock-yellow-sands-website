import requests
import time

time.sleep(3)

try:
    print("🔍 TESTING TRANSLATION INSIDE VS OUTSIDE TABLE")
    
    # Test Arabic page 
    response = requests.get('http://127.0.0.1:8000/ar/products/durability-testing/')
    content = response.text
    
    # Look for our test text outside the table
    outside_table_text = "(Test outside table)"
    
    print("📊 Testing identical translation in different contexts:")
    
    # Check for translation outside table
    if outside_table_text in content:
        print("✅ Found test marker '(Test outside table)'")
        
        # Extract the context around it
        index = content.find(outside_table_text)
        start = max(0, index - 100)
        end = min(len(content), index + 50)
        context = content[start:end]
        
        print(f"Context: '{context}'")
        
        if "95% of image erased" in context:
            print("❌ Translation FAILED outside table - showing English")
        elif "تم مسح 95% من الصورة" in context:
            print("✅ Translation WORKED outside table - showing Arabic with Western numerals")
        elif "تم مسح ٩٥٪ من الصورة" in context:
            print("✅ Translation WORKED outside table - showing Arabic with Arabic numerals")
        else:
            print("❓ Unclear - neither English nor expected Arabic found")
    else:
        print("❌ Test marker not found - template change may not have applied")
    
    # Count occurrences in different contexts
    print(f"\n📊 Occurrence counts:")
    
    # Total English occurrences 
    english_95_total = content.count('95% of image erased') + content.count('95% of the image was erased')
    print(f"  Total English '95%' text: {english_95_total}")
    
    # Total Arabic occurrences (both numeral types)
    arabic_95_western = content.count('تم مسح 95% من الصورة')
    arabic_95_arabic = content.count('تم مسح ٩٥٪ من الصورة')
    print(f"  Arabic with Western numerals: {arabic_95_western}")
    print(f"  Arabic with Arabic numerals: {arabic_95_arabic}")
    
    # Check for table structure
    if '<tbody>' in content and '</tbody>' in content:
        print(f"\n✅ HTML table structure confirmed")
        
        # Try to isolate what's inside the table body
        tbody_start = content.find('<tbody>')
        tbody_end = content.find('</tbody>') + len('</tbody>')
        tbody_content = content[tbody_start:tbody_end]
        
        # Count occurrences specifically within table body
        tbody_english = tbody_content.count('95% of image erased') + tbody_content.count('95% of the image was erased')
        tbody_arabic_western = tbody_content.count('تم مسح 95% من الصورة')
        tbody_arabic_arabic = tbody_content.count('تم مسح ٩٥٪ من الصورة')
        
        print(f"📊 Within <tbody> specifically:")
        print(f"  English: {tbody_english}")
        print(f"  Arabic (Western numerals): {tbody_arabic_western}")
        print(f"  Arabic (Arabic numerals): {tbody_arabic_arabic}")
        
        if tbody_english > 0 and tbody_arabic_western == 0 and tbody_arabic_arabic == 0:
            print("❌ CONFIRMED: Table body translations not working")
        elif tbody_arabic_western > 0 or tbody_arabic_arabic > 0:
            print("✅ BREAKTHROUGH: Table body translations ARE working!")
    else:
        print("❌ Table structure not found")
        
except Exception as e:
    print(f'❌ Error: {e}')
