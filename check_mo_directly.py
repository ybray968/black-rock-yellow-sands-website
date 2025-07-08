import polib

print("🔍 CHECKING .MO FILE DIRECTLY")

# Load the .mo file and check what's actually in it
mo = polib.mofile('locale/ar/LC_MESSAGES/django.mo')

print(f"Total entries in .mo file: {len(mo)}")

# Check for our specific entry
target_text = "95% of image erased"
found = False

for entry in mo:
    if entry.msgid == target_text:
        print(f"✅ Found in .mo file: '{entry.msgid}' -> '{entry.msgstr}'")
        found = True
        break

if not found:
    print(f"❌ '{target_text}' NOT found in .mo file")

# Check a few other entries that we know work vs don't work
test_entries = [
    "Durability Testing",  # Works
    "Products",           # Works 
    "Machine:",           # Works
    "Plywood grades",     # Doesn't work
    "95% of image erased" # Doesn't work
]

print(f"\n📋 Checking specific entries in .mo file:")
for entry_text in test_entries:
    found = False
    for entry in mo:
        if entry.msgid == entry_text:
            print(f"  ✅ '{entry_text}' -> '{entry.msgstr}'")
            found = True
            break
    
    if not found:
        print(f"  ❌ '{entry_text}' NOT FOUND")

# Also check if there are empty entries
empty_count = sum(1 for entry in mo if entry.msgid and not entry.msgstr)
print(f"\n📊 Empty translations in .mo file: {empty_count}")

# Compare with .po file
po = polib.pofile('locale/ar/LC_MESSAGES/django.po')
print(f"📊 Total entries in .po file: {len(po)}")
print(f"📊 Difference (.po - .mo): {len(po) - len(mo)}")

if len(po) != len(mo):
    print("⚠️  WARNING: .po and .mo files have different numbers of entries!")
    print("   This suggests the .mo file wasn't compiled correctly from the .po file")
