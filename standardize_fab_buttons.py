import os
import re

# Find all HTML files
html_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

# Patterns to standardize
patterns = [
    # Fix WhatsApp button - add 'fab' class if missing
    (r'<a href="https://wa\.me/919965524788" target="_blank"([^>]*?)class="fab-whatsapp"', 
     r'<a href="https://wa.me/919965524788" target="_blank"\1class="fab fab-whatsapp"'),
    
    # Fix Call button - add 'fab' class if missing  
    (r'<a href="tel:04222626999"([^>]*?)class="fab-call"',
     r'<a href="tel:04222626999"\1class="fab fab-call"'),
]

updated_count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Apply all patterns
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    # Only write if changes were made
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")
        updated_count += 1

print(f"\nTotal files updated: {updated_count}")