import os
import django
from django.conf import settings
from django.utils import translation
from django.utils.translation import gettext as _

# Setup Django fresh
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

print("🔍 TESTING TRANSLATION IN FRESH DJANGO PROCESS")

# Force Django to reload translation catalogs
from django.utils.translation import trans_real
trans_real._active = {}
trans_real._translations = {}

# Activate Arabic language
translation.activate('ar')
current_lang = translation.get_language()
print(f"Current language: {current_lang}")

# Test the specific translation
test_text = "95% of image erased"
result = _(test_text)

print(f"Input: '{test_text}'")
print(f"Output: '{result}'")

if result == test_text:
    print("❌ Translation NOT working - same as input")
else:
    print("✅ Translation WORKING - output is different")
    
# Test a few more translations
test_cases = [
    "Durability Testing",
    "Products", 
    "Plywood grades",
    "95% of image erased"
]

print(f"\n📋 Testing multiple strings:")
for test_case in test_cases:
    result = _(test_case)
    status = "✅" if result != test_case else "❌"
    print(f"  {status} '{test_case}' -> '{result}'")

# Check if .mo file can be loaded directly
print(f"\n🔍 Checking .mo file loading:")
try:
    import gettext
    catalog = gettext.translation('django', localedir='locale', languages=['ar'])
    direct_result = catalog.gettext("95% of image erased")
    print(f"Direct gettext result: '{direct_result}'")
    
    if direct_result != "95% of image erased":
        print("✅ Direct gettext works")
    else:
        print("❌ Direct gettext fails")
        
except Exception as e:
    print(f"❌ Error loading catalog: {e}")

print("\n🔄 Translation test complete")
