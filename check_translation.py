import polib

po = polib.pofile('locale/ar/LC_MESSAGES/django.po')
found = False
for entry in po:
    if '95% of image erased' in entry.msgid:
        print(f'Found: "{entry.msgid}" -> "{entry.msgstr}"')
        found = True
        
if not found:
    print("Translation for '95% of image erased' NOT found in .po file")
    # Let's search for any related entries
    for entry in po:
        if 'image' in entry.msgid.lower() or 'erased' in entry.msgid.lower():
            print(f'Related: "{entry.msgid}" -> "{entry.msgstr}"')
