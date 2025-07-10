#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translation Management Utility
Helps maintain Arabic translations and fix encoding issues
"""

import os
import sys
from pathlib import Path

def check_translations():
    """Check if translations are working correctly"""
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_site.settings')
        
        import django
        django.setup()
        
        from django.utils.translation import gettext as _
        from django.utils import translation
        
        # Test English
        translation.activate('en')
        test_en = _("Home")
        print(f"English: {test_en}")
        
        # Test Arabic
        translation.activate('ar')
        test_ar = _("Home")
        print(f"Arabic: {test_ar}")
        
        # Reset to default
        translation.activate('en')
        
        return True
        
    except Exception as e:
        print(f"Translation test failed: {e}")
        return False

def compile_translations():
    """Compile translation files"""
    try:
        import polib
        
        po_file = Path("locale/ar/LC_MESSAGES/django.po")
        mo_file = Path("locale/ar/LC_MESSAGES/django.mo")
        
        if po_file.exists():
            # Load and compile
            po = polib.pofile(str(po_file))
            po.save_as_mofile(str(mo_file))
            print(f"✅ Compiled translations: {mo_file}")
            return True
        else:
            print(f"❌ Translation file not found: {po_file}")
            return False
            
    except ImportError:
        print("❌ polib not installed. Install with: pip install polib")
        return False
    except Exception as e:
        print(f"❌ Compilation error: {e}")
        return False

def main():
    """Main function"""
    print("🔧 Translation Management Utility")
    print("=" * 40)
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "compile":
            compile_translations()
        elif command == "check":
            check_translations()
        else:
            print("Usage: python manage_translations.py [compile|check]")
    else:
        print("Available commands:")
        print("  compile - Compile translation files")
        print("  check   - Test translation functionality")
        print()
        print("Usage: python manage_translations.py [command]")

if __name__ == "__main__":
    main()
