import polib
import os

print("🔄 FORCE COMPLETE RECOMPILATION")

# Load the .po file
po_path = 'locale/ar/LC_MESSAGES/django.po'
mo_path = 'locale/ar/LC_MESSAGES/django.mo'

print(f"Loading .po file: {po_path}")
po = polib.pofile(po_path)

print(f"Original .po file entries: {len(po)}")

# Count non-empty entries
non_empty = sum(1 for entry in po if entry.msgid and entry.msgstr)
empty = sum(1 for entry in po if entry.msgid and not entry.msgstr)

print(f"Entries with translations: {non_empty}")
print(f"Entries without translations: {empty}")

# Remove existing .mo file to ensure clean compilation
if os.path.exists(mo_path):
    os.remove(mo_path)
    print(f"✅ Deleted existing .mo file")

# Force save as .mo file (this should include all entries)
try:
    po.save_as_mofile(mo_path)
    print(f"✅ Successfully compiled to .mo file")
    
    # Verify the new .mo file
    new_mo = polib.mofile(mo_path)
    print(f"New .mo file entries: {len(new_mo)}")
    
    # Check if our target entries are in the new .mo file
    test_entries = ["95% of image erased", "Plywood grades"]
    
    for entry_text in test_entries:
        found = False
        for entry in new_mo:
            if entry.msgid == entry_text:
                print(f"✅ Found in new .mo: '{entry_text}' -> '{entry.msgstr}'")
                found = True
                break
        
        if not found:
            print(f"❌ Missing from new .mo: '{entry_text}'")
            
except Exception as e:
    print(f"❌ Error compiling .mo file: {e}")

print("🔄 Recompilation complete!")
print("🔧 Please restart Django server to pick up changes")
