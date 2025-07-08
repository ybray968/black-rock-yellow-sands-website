import polib
import re

print("🔍 CHECKING .PO FILE FOR ISSUES")

po = polib.pofile('locale/ar/LC_MESSAGES/django.po')

# Check for our specific entry
target_text = "95% of image erased"
found_entries = []

for entry in po:
    if target_text in entry.msgid:
        found_entries.append(entry)

print(f"\n📊 Found {len(found_entries)} entries containing '{target_text}'")

for i, entry in enumerate(found_entries):
    print(f"\nEntry #{i+1}:")
    print(f"  msgid: '{entry.msgid}'")
    print(f"  msgstr: '{entry.msgstr}'")
    print(f"  locations: {entry.occurrences}")
    print(f"  flags: {entry.flags}")
    print(f"  fuzzy: {entry.fuzzy}")
    
    # Check if msgstr is empty
    if not entry.msgstr:
        print("  ❌ ISSUE: Empty translation (msgstr)")
    
    # Check if entry is fuzzy (needs review)
    if entry.fuzzy:
        print("  ❌ ISSUE: Entry is marked as fuzzy")
        
    # Check for any special characters that might cause issues
    if '\n' in entry.msgstr:
        print("  ⚠️  WARNING: Translation contains newlines")

# Check for other potential issues
print("\n🔍 CHECKING FOR OTHER ISSUES...")

# Count total entries
total_entries = len(po)
empty_translations = sum(1 for entry in po if entry.msgid and not entry.msgstr)
fuzzy_entries = sum(1 for entry in po if entry.fuzzy)

print(f"Total entries: {total_entries}")
print(f"Empty translations: {empty_translations}")
print(f"Fuzzy entries: {fuzzy_entries}")

# Check if there are any compilation issues
try:
    po.save_as_mofile('test_temp.mo')
    print("✅ .po file can be compiled to .mo")
    import os
    os.remove('test_temp.mo')
except Exception as e:
    print(f"❌ Compilation error: {e}")

# Look for other translations that work to compare
working_translations = []
for entry in po:
    if entry.msgid in ["Products", "Durability Testing", "Back to Home"]:
        working_translations.append(entry)

print(f"\n📋 Working translations for comparison:")
for entry in working_translations:
    print(f"  '{entry.msgid}' -> '{entry.msgstr}' (Empty: {not bool(entry.msgstr)})")
