import polib

print("🔧 MANUALLY FIXING .PO FILE")

# Load the current .po file
po = polib.pofile('locale/ar/LC_MESSAGES/django.po')

# Check if "95% of image erased" already has proper location
found_target = False
for entry in po:
    if entry.msgid == "95% of image erased":
        print(f"Current entry: '{entry.msgid}' -> '{entry.msgstr}'")
        print(f"Locations: {entry.occurrences}")
        
        # Update the location if it's missing
        if not entry.occurrences:
            entry.occurrences = [('templates/products/durability_testing.html', 284)]
            print("✅ Added location to existing entry")
        else:
            print("✅ Entry already has locations")
        found_target = True
        break

if not found_target:
    # Add the entry if it doesn't exist
    entry = polib.POEntry(
        msgid="95% of image erased",
        msgstr="تم مسح ٩٥٪ من الصورة",
        occurrences=[('templates/products/durability_testing.html', 284)]
    )
    po.append(entry)
    print("✅ Added missing entry")

# Also add back "Back to Home" if missing
found_back_home = False
for entry in po:
    if entry.msgid == "Back to Home":
        found_back_home = True
        break

if not found_back_home:
    entry = polib.POEntry(
        msgid="Back to Home",
        msgstr="العودة إلى الرئيسية",
        occurrences=[('templates/main/home.html', 1)]
    )
    po.append(entry)
    print("✅ Added missing 'Back to Home' entry")

# Add "Back to Products" which might be missing
found_back_products = False
for entry in po:
    if entry.msgid == "Back to Products":
        found_back_products = True
        break

if not found_back_products:
    entry = polib.POEntry(
        msgid="Back to Products",
        msgstr="العودة إلى المنتجات",
        occurrences=[('templates/products/durability_testing.html', 126)]
    )
    po.append(entry)
    print("✅ Added missing 'Back to Products' entry")

# Save the updated .po file
po.save('locale/ar/LC_MESSAGES/django.po')
print("💾 Saved updated .po file")

# Compile to .mo file
po.save_as_mofile('locale/ar/LC_MESSAGES/django.mo')
print("🔄 Compiled to .mo file")

print("✅ Manual fixes complete!")

# Show final count
print(f"📊 Final .po file has {len(po)} entries")
