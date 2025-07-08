import requests
import time

time.sleep(3)

print("🔍 TESTING WITH CACHE-BUSTING HEADERS")

# Headers to prevent any caching
headers = {
    'Cache-Control': 'no-cache, no-store, must-revalidate',
    'Pragma': 'no-cache',
    'Expires': '0',
    'User-Agent': 'FreshTestClient/1.0'
}

try:
    # Test Arabic page with cache-busting headers
    url = 'http://127.0.0.1:8000/ar/products/durability-testing/'
    print(f"Testing URL: {url}")
    
    response = requests.get(url, headers=headers)
    content = response.text
    
    print(f"Response status: {response.status_code}")
    print(f"Content length: {len(content)} characters")
    
    # Check for target translations
    english_count = content.count('95% of image erased')
    arabic_count = content.count('تم مسح ٩٥٪ من الصورة')
    
    print(f"\nContent analysis:")
    print(f"  English '95% of image erased': {english_count} occurrences")
    print(f"  Arabic  'تم مسح ٩٥٪ من الصورة': {arabic_count} occurrences")
    
    # Check other working translations to ensure it's Arabic page
    if 'اختبار المتانة' in content:  # Durability Testing
        print(f"  ✅ Page has Arabic title translation")
    else:
        print(f"  ❌ Page missing Arabic title translation")
    
    if 'lang="ar"' in content:
        print(f"  ✅ Page has Arabic lang attribute")
    else:
        print(f"  ❌ Page missing Arabic lang attribute")
    
    # Check for Django debug info (if any)
    if 'djDebug' in content or 'django-debug' in content:
        print(f"  ⚠️  Django debug mode detected")
    
    # Final verdict
    if arabic_count > 0:
        print(f"\n🎉 SUCCESS! Arabic translation working!")
    elif english_count > 0:
        print(f"\n❌ ISSUE: Still showing English text")
    else:
        print(f"\n❓ UNCLEAR: Neither English nor Arabic text found")
        
except Exception as e:
    print(f'❌ Error: {e}')
    
print(f"\n🔄 Test complete")
