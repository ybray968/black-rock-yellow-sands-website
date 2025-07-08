import polib

print("🔧 TESTING % SYMBOL THEORY - Adding 'percent' version")

po = polib.pofile('locale/ar/LC_MESSAGES/django.po')

# Add the version without % symbol
new_entry = polib.POEntry(
    msgid="95 percent of image erased",
    msgstr="تم مسح 95 في المئة من الصورة",  # Using "في المئة" (percent) instead of %
    occurrences=[('templates/products/durability_testing.html', 342)]
)

po.append(new_entry)
print(f"✅ Added: '{new_entry.msgid}' -> '{new_entry.msgstr}'")

# Save and compile
po.save('locale/ar/LC_MESSAGES/django.po')
po.save_as_mofile('locale/ar/LC_MESSAGES/django.mo')

print("💾 Saved and compiled with 'percent' version")
print("🔧 Please restart Django to test if % symbol was the problem")

# Show comparison
print(f"\n📊 COMPARISON:")
print(f"  ❌ BROKEN: '95% of image erased' (with % symbol)")
print(f"  🔄 TESTING: '95 percent of image erased' (word 'percent')")
print(f"  ✅ WORKING: 'Image mostly erased' (no numbers)")
print(f"  ✅ WORKING: 'Correction factor f = 0.87' (no % symbol)")

# Verify in .mo file
mo = polib.mofile('locale/ar/LC_MESSAGES/django.mo')
for entry in mo:
    if entry.msgid == "95 percent of image erased":
        print(f"\n✅ Verified in .mo: '{entry.msgid}' -> '{entry.msgstr}'")
        break
else:
    print(f"\n❌ New 'percent' version not found in .mo file")
