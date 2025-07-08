import os
import re
import polib
from pathlib import Path

print("🔄 REGENERATING .PO FILE WITH PROPER LOCATIONS")

# Load existing .po file to preserve existing translations
po_path = 'locale/ar/LC_MESSAGES/django.po'
if os.path.exists(po_path):
    po = polib.pofile(po_path)
    print(f"✅ Loaded existing .po file with {len(po)} entries")
else:
    po = polib.POFile()
    print("📝 Creating new .po file")

# Dictionary to store existing translations
existing_translations = {}
for entry in po:
    existing_translations[entry.msgid] = entry.msgstr

# Find all template files
template_files = []
for root, dirs, files in os.walk('templates'):
    for file in files:
        if file.endswith('.html'):
            template_files.append(os.path.join(root, file))

print(f"🔍 Found {len(template_files)} template files")

# Pattern to find {% trans %} tags
trans_pattern = re.compile(r'{%\s*trans\s*["\']([^"\']+)["\']\s*%}')

# Collect all translation strings with their locations
translation_strings = {}

for template_file in template_files:
    try:
        with open(template_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all translation strings in this file
        matches = trans_pattern.findall(content)
        
        for match in matches:
            if match not in translation_strings:
                translation_strings[match] = []
            
            # Add this file as a location for this translation
            relative_path = os.path.relpath(template_file).replace('\\', '/')
            translation_strings[match].append((relative_path, 1))  # Line number simplified to 1
            
    except Exception as e:
        print(f"⚠️  Error reading {template_file}: {e}")

print(f"📊 Found {len(translation_strings)} unique translation strings")

# Create new .po file with proper locations
new_po = polib.POFile()

# Set metadata
new_po.metadata = {
    'Content-Type': 'text/plain; charset=UTF-8',
    'Content-Transfer-Encoding': '8bit',
    'Language': 'ar',
}

# Add entries with locations
for msgid, locations in translation_strings.items():
    # Use existing translation if available
    msgstr = existing_translations.get(msgid, '')
    
    entry = polib.POEntry(
        msgid=msgid,
        msgstr=msgstr,
        occurrences=locations
    )
    new_po.append(entry)
    
    if msgid == "95% of image erased":
        print(f"✅ Added entry for '{msgid}' with {len(locations)} locations:")
        for loc in locations:
            print(f"   📍 {loc[0]}")

# Save the new .po file
new_po.save(po_path)
print(f"💾 Saved updated .po file with {len(new_po)} entries")

# Compile to .mo file
mo_path = 'locale/ar/LC_MESSAGES/django.mo'
new_po.save_as_mofile(mo_path)
print(f"🔄 Compiled to .mo file: {mo_path}")

print("✅ Regeneration complete!")
