import polib
import gettext
import os

# Recompile fresh mo file
po_file = 'locale/ar/LC_MESSAGES/django.po'
mo_file = 'locale/ar/LC_MESSAGES/django.mo'

po = polib.pofile(po_file)
po.save_as_mofile(mo_file)
print(f'Fresh compilation complete: {len(po)} entries')

# Verify our specific translation
target_found = False
for entry in po:
    if entry.msgid == '95% of image erased':
        print(f'Target translation: "{entry.msgstr}"')
        target_found = True
        break

if not target_found:
    print('Target translation not found!')

# Test if we can load the mo file and get the translation
if os.path.exists(mo_file):
    with open(mo_file, 'rb') as f:
        catalog = gettext.GNUTranslations(f)
        translation = catalog.gettext('95% of image erased')
        print(f'Direct .mo file test: "{translation}"')
        
        if translation == '95% of image erased':
            print('✗ Translation not found in .mo file')
        else:
            print('✓ Translation found in .mo file')
else:
    print('✗ .mo file not found')
