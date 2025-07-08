import polib

print("🔧 TESTING WITH WESTERN NUMERALS INSTEAD OF ARABIC NUMERALS")

po = polib.pofile('locale/ar/LC_MESSAGES/django.po')

# Update problematic entries to use Western numerals
updates = [
    ("95% of image erased", "تم مسح 95% من الصورة"),  # ٩٥٪ → 95%
    ("95% of the image was erased", "تم مسح 95% من الصورة"),  # ٩٥٪ → 95%
    ("Correction factor f = 0.87", "عامل التصحيح f = 0.87")  # ٠.٨٧ → 0.87
]

print("🔄 Updating translations to use Western numerals:")
for msgid, new_msgstr in updates:
    for entry in po:
        if entry.msgid == msgid:
            old_msgstr = entry.msgstr
            entry.msgstr = new_msgstr
            print(f"  ✅ '{msgid}':")
            print(f"     OLD: '{old_msgstr}'")
            print(f"     NEW: '{new_msgstr}'")
            break

# Save and compile
po.save('locale/ar/LC_MESSAGES/django.po')
po.save_as_mofile('locale/ar/LC_MESSAGES/django.mo')

print("\n💾 Saved and compiled with Western numerals")
print("🔧 Please restart Django server to test if Western numerals work")

# Verify the changes are in the .mo file
mo = polib.mofile('locale/ar/LC_MESSAGES/django.mo')
print("\n🔍 Verifying in .mo file:")
for msgid, new_msgstr in updates:
    for entry in mo:
        if entry.msgid == msgid:
            print(f"  ✅ '{msgid}' -> '{entry.msgstr}'")
            break
