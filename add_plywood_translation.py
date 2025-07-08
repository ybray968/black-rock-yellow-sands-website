import polib

print("🔧 ADDING MISSING PLYWOOD GRADES TRANSLATION")

po = polib.pofile('locale/ar/LC_MESSAGES/django.po')

# Find and update "Plywood grades" entry
found = False
for entry in po:
    if entry.msgid == "Plywood grades":
        entry.msgstr = "درجات الخشب الرقائقي"
        print(f"✅ Updated: '{entry.msgid}' -> '{entry.msgstr}'")
        found = True
        break

if not found:
    # Add the entry if it doesn't exist
    entry = polib.POEntry(
        msgid="Plywood grades",
        msgstr="درجات الخشب الرقائقي",
        occurrences=[('templates/products/durability_testing.html', 135)]
    )
    po.append(entry)
    print("✅ Added new entry for 'Plywood grades'")

# Save and compile
po.save('locale/ar/LC_MESSAGES/django.po')
po.save_as_mofile('locale/ar/LC_MESSAGES/django.mo')

print("💾 Saved and compiled translations")
print("🔧 Please restart Django to test")
