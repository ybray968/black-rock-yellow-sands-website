import gettext
import os

# Check if .mo file exists
mo_path = 'locale/ar/LC_MESSAGES/django.mo'
if os.path.exists(mo_path):
    print(f"✅ .mo file exists at {mo_path}")
    
    # Load the translations
    try:
        translation = gettext.translation('django', localedir='locale', languages=['ar'])
        _ = translation.gettext
        
        # Test the specific translation
        result = _('95% of image erased')
        print(f'Translation result: "{result}"')
        
        if result == '95% of image erased':
            print("❌ Translation NOT working - returning original text")
        else:
            print("✅ Translation working!")
            
    except Exception as e:
        print(f"❌ Error loading translation: {e}")
else:
    print(f"❌ .mo file does not exist at {mo_path}")
