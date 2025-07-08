import polib

print("🔧 RECREATING '95% of image erased' ENTRY FROM SCRATCH")

po = polib.pofile('locale/ar/LC_MESSAGES/django.po')

# Remove existing entry completely
original_count = len(po)
po[:] = [entry for entry in po if entry.msgid != "95% of image erased"]
new_count = len(po)

if original_count != new_count:
    print(f"✅ Removed existing entry (was {original_count}, now {new_count})")
else:
    print("❓ No existing entry found to remove")

# Add a completely fresh entry
fresh_entry = polib.POEntry(
    msgid="95% of image erased",
    msgstr="تم مسح ٩٥٪ من الصورة",
    occurrences=[('templates/products/durability_testing.html', 284)]
)

po.append(fresh_entry)
print(f"✅ Added fresh entry: '{fresh_entry.msgid}' -> '{fresh_entry.msgstr}'")

# Save and compile
po.save('locale/ar/LC_MESSAGES/django.po')
po.save_as_mofile('locale/ar/LC_MESSAGES/django.mo')

print("💾 Saved and compiled with fresh entry")

# Verify the entry is in the .mo file
mo = polib.mofile('locale/ar/LC_MESSAGES/django.mo')
found_in_mo = False
for entry in mo:
    if entry.msgid == "95% of image erased":
        print(f"✅ Verified in .mo file: '{entry.msgid}' -> '{entry.msgstr}'")
        found_in_mo = True
        break

if not found_in_mo:
    print("❌ Fresh entry NOT found in .mo file")

print(f"📊 Final .po entries: {len(po)}")
print(f"📊 Final .mo entries: {len(mo)}")
print("🔧 Please restart Django to test the fresh entry")
