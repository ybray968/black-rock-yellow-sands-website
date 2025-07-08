import os
import django
from django.conf import settings
from django.utils import translation
from django.utils.translation import gettext

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
django.setup()

print("🔍 DJANGO TRANSLATION SYSTEM CHECK")
print(f"USE_I18N: {settings.USE_I18N}")
print(f"USE_L10N: {settings.USE_L10N}")
print(f"LANGUAGE_CODE: {settings.LANGUAGE_CODE}")
print(f"LANGUAGES: {settings.LANGUAGES}")
print(f"LOCALE_PATHS: {settings.LOCALE_PATHS}")

# Check if locale directory exists
for locale_path in settings.LOCALE_PATHS:
    print(f"\nLocale path: {locale_path}")
    print(f"Exists: {os.path.exists(locale_path)}")
    
    ar_path = locale_path / 'ar' / 'LC_MESSAGES'
    print(f"Arabic locale path: {ar_path}")
    print(f"Exists: {os.path.exists(ar_path)}")
    
    po_file = ar_path / 'django.po'
    mo_file = ar_path / 'django.mo'
    print(f"PO file exists: {os.path.exists(po_file)}")
    print(f"MO file exists: {os.path.exists(mo_file)}")

# Test translation activation
print("\n🔄 Testing translation activation...")

# Activate Arabic
translation.activate('ar')
current_lang = translation.get_language()
print(f"Current language after activate('ar'): {current_lang}")

# Test direct translation
test_text = "95% of image erased"
translated = gettext(test_text)
print(f"Translation of '{test_text}': '{translated}'")

if translated == test_text:
    print("❌ Translation not working - getting original text back")
else:
    print("✅ Translation working!")

# Check available languages
from django.utils.translation import get_available_languages
available = get_available_languages()
print(f"Available languages: {available}")

# Test with underscore gettext
from django.utils.translation import ugettext as _
translated_underscore = _(test_text)
print(f"Using _() translation: '{translated_underscore}'")
