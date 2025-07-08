import polib

print("🔍 CHECKING WHICH TRANSLATIONS EXIST IN .PO FILE")

po = polib.pofile('locale/ar/LC_MESSAGES/django.po')

# Test all the strings we just checked
test_strings = [
    # Table headers that should work
    "Series, sample #",
    "Number of turns", 
    "Coating abrasive resistance",
    "The overall look after abrasion test",
    
    # Table body that doesn't work
    "95% of image erased",
    "95% of the image was erased",
    "Correction factor f = 0.87",
    
    # Control group
    "Machine:",
    "Plywood grades",
    "Durability Testing"
]

print("📋 Translation file contents:")
for test_string in test_strings:
    found = False
    for entry in po:
        if entry.msgid == test_string:
            status = "✅" if entry.msgstr else "⚠️ EMPTY"
            print(f"  {status}: '{test_string}' -> '{entry.msgstr}'")
            found = True
            break
    
    if not found:
        print(f"  ❌ MISSING: '{test_string}'")

print(f"\n📊 Total entries in .po file: {len(po)}")

# Let's also look for partial matches for missing entries
print(f"\n🔍 Looking for partial matches:")
for test_string in ["Series, sample", "Number of turns", "Correction factor"]:
    print(f"\nSearching for '{test_string}':")
    matches = []
    for entry in po:
        if test_string.lower() in entry.msgid.lower():
            matches.append(f"  '{entry.msgid}' -> '{entry.msgstr}'")
    
    if matches:
        for match in matches:
            print(match)
    else:
        print(f"  No matches found")

# Check the template again to see exactly what strings are being used
print(f"\n🔍 Let me check the template for exact strings...")

template_path = 'templates/products/durability_testing.html'
try:
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    import re
    # Find all {% trans %} patterns
    trans_pattern = re.compile(r'{%\s*trans\s*["\']([^"\']+)["\']\s*%}')
    all_trans_strings = trans_pattern.findall(content)
    
    print(f"Found {len(all_trans_strings)} translation strings in template")
    
    # Show strings that aren't in our .po file
    missing_from_po = []
    for trans_string in all_trans_strings:
        found = any(entry.msgid == trans_string for entry in po)
        if not found:
            missing_from_po.append(trans_string)
    
    if missing_from_po:
        print(f"\n❌ Strings in template but NOT in .po file:")
        for missing in missing_from_po:
            print(f"  '{missing}'")
    else:
        print(f"\n✅ All template strings are in .po file")
            
except Exception as e:
    print(f"❌ Error reading template: {e}")
