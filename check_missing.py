import polib

print("🔍 CHECKING WHAT ENTRIES ARE MISSING")

po = polib.pofile('locale/ar/LC_MESSAGES/django.po')

# Check specific entries we know should exist
test_entries = [
    "Products",
    "Durability Testing", 
    "Back to Home",
    "95% of image erased"
]

for entry_text in test_entries:
    found = False
    for entry in po:
        if entry.msgid == entry_text:
            print(f"✅ Found '{entry_text}' -> '{entry.msgstr}'")
            found = True
            break
    
    if not found:
        print(f"❌ Missing '{entry_text}'")

# Count entries with empty translations
empty_count = sum(1 for entry in po if entry.msgid and not entry.msgstr)
total_count = len(po)

print(f"\n📊 Total entries: {total_count}")
print(f"📊 Empty translations: {empty_count}")
print(f"📊 Complete translations: {total_count - empty_count}")

# Show a few entries to see the pattern
print(f"\n📋 Sample entries:")
for i, entry in enumerate(po[:10]):
    if entry.msgid:  # Skip empty msgid entries
        status = "✅" if entry.msgstr else "❌"
        print(f"  {status} '{entry.msgid}' -> '{entry.msgstr}'")
