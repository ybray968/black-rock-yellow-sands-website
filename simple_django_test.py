import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

print("🔍 SIMPLE DJANGO TRANSLATION TEST")

from django.utils import translation
from django.utils.translation import gettext as _

# Activate Arabic language
translation.activate('ar')
current_lang = translation.get_language()
print(f"Current language: {current_lang}")

# Test the translation
test_text = "95% of image erased"
result = _(test_text)

print(f"Translation test:")
print(f"  Input:  '{test_text}'")
print(f"  Output: '{result}'")

if result == test_text:
    print(f"  Status: ❌ NOT TRANSLATED")
else:
    print(f"  Status: ✅ TRANSLATED")

# Test some other translations for comparison
other_tests = ["Products", "Durability Testing"]
for test in other_tests:
    result = _(test)
    status = "✅" if result != test else "❌"
    print(f"  {status} '{test}' -> '{result}'")
