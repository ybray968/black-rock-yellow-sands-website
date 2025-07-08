import polib

print("🔍 CHECKING PROBLEM ENTRIES IN DETAIL")

po = polib.pofile('locale/ar/LC_MESSAGES/django.po')

# Check for "Plywood grades" specifically
target_entries = ["Plywood grades", "95% of image erased"]

for target in target_entries:
    print(f"\n🔍 Searching for '{target}':")
    
    found = False
    for entry in po:
        if target in entry.msgid:
            print(f"  ✅ Found: '{entry.msgid}'")
            print(f"     Translation: '{entry.msgstr}'")
            print(f"     Has translation: {bool(entry.msgstr)}")
            print(f"     Fuzzy: {entry.fuzzy}")
            print(f"     Locations: {entry.occurrences}")
            found = True
            break
    
    if not found:
        print(f"  ❌ '{target}' not found in .po file")
        # Search for partial matches
        print("  🔍 Searching for partial matches:")
        for entry in po:
            if target.lower() in entry.msgid.lower():
                print(f"    Partial: '{entry.msgid}' -> '{entry.msgstr}'")

# Let's also check the template to see exactly what text is used
print(f"\n🔍 Checking template file for exact text...")

template_path = 'templates/products/durability_testing.html'
try:
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Search for plywood grades text
    import re
    trans_pattern = re.compile(r'{%\s*trans\s*["\']([^"\']*[Pp]lywood[^"\']*grades[^"\']*)["\']')
    matches = trans_pattern.findall(content)
    
    if matches:
        print("  Found in template:")
        for match in matches:
            print(f"    {{% trans \"{match}\" %}}")
    else:
        print("  ❌ No 'plywood grades' translation found in template")
        
        # Search for the literal text
        if 'plywood grades' in content.lower():
            print("  ❓ Found literal 'plywood grades' text (not in {% trans %} tags)")
        else:
            print("  ❓ No 'plywood grades' text found at all")
            
except Exception as e:
    print(f"  ❌ Error reading template: {e}")

print(f"\n📊 Total .po entries: {len(po)}")
translated_count = sum(1 for entry in po if entry.msgid and entry.msgstr)
print(f"📊 Translated entries: {translated_count}")
print(f"📊 Untranslated entries: {len(po) - translated_count}")
