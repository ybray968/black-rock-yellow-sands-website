import requests
import time

time.sleep(3)

try:
    print("🔍 DETAILED HTML INSPECTION")
    
    # Get Arabic page content
    response = requests.get('http://127.0.0.1:8000/ar/products/durability-testing/')
    html_content = response.text
    
    # Find the first table row with the problematic text
    lines = html_content.split('\n')
    for i, line in enumerate(lines):
        if '95% of image erased' in line:
            print(f"\nFound at line {i+1}:")
            print(f"Content: {line.strip()}")
            
            # Show a few lines around it for context
            start = max(0, i-2)
            end = min(len(lines), i+3)
            print("\nContext:")
            for j in range(start, end):
                marker = " >>> " if j == i else "     "
                print(f"{marker}Line {j+1}: {lines[j].strip()}")
            break
    
    # Check if the {% trans %} tags are in the served HTML
    if '{% trans' in html_content:
        print("\n❌ PROBLEM: {% trans %} tags found in served HTML!")
        print("This means the template tags are not being processed.")
        # Find instances
        for i, line in enumerate(lines):
            if '{% trans' in line:
                print(f"Unprocessed tag at line {i+1}: {line.strip()}")
                break
    else:
        print("\n✅ Template tags are being processed correctly")
    
    # Check language detection in HTML
    if 'lang="ar"' in html_content:
        print("✅ HTML has Arabic language attribute")
    elif 'lang="en"' in html_content:
        print("❌ HTML has English language attribute (should be Arabic)")
    else:
        print("❓ No language attribute found in HTML")
        
except Exception as e:
    print(f'❌ Error: {e}')
