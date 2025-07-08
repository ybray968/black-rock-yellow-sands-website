import polib

print("🔧 ADDING TRANSLATION FOR 'Image mostly erased'")

po = polib.pofile('locale/ar/LC_MESSAGES/django.po')

# Add the new test entry
new_entry = polib.POEntry(
    msgid="Image mostly erased",
    msgstr="تم مسح معظم الصورة",
    occurrences=[('templates/products/durability_testing.html', 342)]
)

po.append(new_entry)
print(f"✅ Added: '{new_entry.msgid}' -> '{new_entry.msgstr}'")

# Save and compile
po.save('locale/ar/LC_MESSAGES/django.po')
po.save_as_mofile('locale/ar/LC_MESSAGES/django.mo')

print("💾 Saved and compiled with new string")
print("🔧 Please restart Django to test the completely different string")

# Verify in .mo file
mo = polib.mofile('locale/ar/LC_MESSAGES/django.mo')
for entry in mo:
    if entry.msgid == "Image mostly erased":
        print(f"✅ Verified in .mo: '{entry.msgid}' -> '{entry.msgstr}'")
        break
else:
    print("❌ New string not found in .mo file")
