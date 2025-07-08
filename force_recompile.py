import polib
import os

print("🔄 Force recompiling translations...")

# Remove existing .mo file
mo_path = 'locale/ar/LC_MESSAGES/django.mo'
if os.path.exists(mo_path):
    os.remove(mo_path)
    print(f"✅ Deleted existing .mo file: {mo_path}")

# Load and save .po file to .mo
po_path = 'locale/ar/LC_MESSAGES/django.po'
po = polib.pofile(po_path)

# Save as .mo
po.save_as_mofile(mo_path)
print(f"✅ Created new .mo file: {mo_path}")

# Verify the translation exists
for entry in po:
    if entry.msgid == '95% of image erased':
        print(f"✅ Verified translation: '{entry.msgid}' -> '{entry.msgstr}'")
        break
else:
    print("❌ Translation not found in .po file")

print("🔄 Compilation complete!")
