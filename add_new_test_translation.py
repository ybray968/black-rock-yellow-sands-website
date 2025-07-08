import polib

print("🔧 ADDING TRANSLATION FOR NEW TEST TEXT")

po = polib.pofile('locale/ar/LC_MESSAGES/django.po')

# Add the new entry
new_entry = polib.POEntry(
    msgid="95% of the image was erased",
    msgstr="تم مسح ٩٥٪ من الصورة",
    occurrences=[('templates/products/durability_testing.html', 284)]
)

po.append(new_entry)
print(f"✅ Added: '{new_entry.msgid}' -> '{new_entry.msgstr}'")

# Save and compile
po.save('locale/ar/LC_MESSAGES/django.po')
po.save_as_mofile('locale/ar/LC_MESSAGES/django.mo')

print("💾 Saved and compiled with new test translation")
print("🔧 Please restart Django to test")
