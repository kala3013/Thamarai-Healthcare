import os
import re

# Find all HTML files
html_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

# Pattern to match the fab-appointment line (handle both class formats)
pattern = r'<a href="[^"]*" class="fab-appointment" aria-label="Book Appointment">\s*<i class="bi bi-calendar-plus-fill"></i>\s*<span class="tooltip-text">Book Appointment</span>\s*</a>\n'

removed_count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if the pattern exists
    if re.search(pattern, content):
        # Remove the line
        new_content = re.sub(pattern, '', content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed from: {filepath}")
        removed_count += 1

print(f"\nTotal files updated: {removed_count}")