import polib

print("🔧 ADDING ARABIC TRANSLATIONS FOR NEW STRINGS")

po = polib.pofile('locale/ar/LC_MESSAGES/django.po')

# New translations to add
new_translations = [
    # Fix 1: The alternative "95 percent of the image was erased" 
    ("95 percent of the image was erased", "تم مسح 95 في المئة من الصورة"),
    
    # Fix 2: The plywood deck cycles text (without quotes to avoid escaping issues)
    ("On average, Plywood Deck can be used in 50 cycles of cement pouring", "في المتوسط، يمكن استخدام الخشب الرقائقي الدك في 50 دورة من صب الأسمنت")
]

print("Adding new translations:")
for msgid, msgstr in new_translations:
    # Check if it already exists
    exists = False
    for entry in po:
        if entry.msgid == msgid:
            if entry.msgstr != msgstr:
                entry.msgstr = msgstr
                print(f"  ✅ Updated: '{msgid}' -> '{msgstr}'")
            else:
                print(f"  ✅ Already correct: '{msgid}'")
            exists = True
            break
    
    if not exists:
        # Add new entry
        new_entry = polib.POEntry(
            msgid=msgid,
            msgstr=msgstr,
            occurrences=[('templates/products/durability_testing.html', 1)]
        )
        po.append(new_entry)
        print(f"  ✅ Added new: '{msgid}' -> '{msgstr}'")

# Save and compile
po.save('locale/ar/LC_MESSAGES/django.po')
po.save_as_mofile('locale/ar/LC_MESSAGES/django.mo')

print(f"\n💾 Saved and compiled translations")
print(f"📊 Total entries in .po file: {len(po)}")

# Verify in .mo file
mo = polib.mofile('locale/ar/LC_MESSAGES/django.mo')
print(f"📊 Total entries in .mo file: {len(mo)}")

print(f"\n🔍 Verifying new translations in .mo file:")
for msgid, expected_msgstr in new_translations:
    found = False
    for entry in mo:
        if entry.msgid == msgid:
            print(f"  ✅ '{msgid}' -> '{entry.msgstr}'")
            found = True
            break
    if not found:
        print(f"  ❌ Missing: '{msgid}'")

print("\n🔧 Please restart Django to test the new translations")
