#!/usr/bin/env python3
"""Remove 'Thamarai Fertility' text next to logo in footer across all pages."""
import os
import re
import glob

BASE = r'c:\Users\ELCOT\Desktop\thamarai-healthcare'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Remove the footer-brand span that says "Thamarai Fertility" next to the logo
    content = re.sub(
        r'\s*<span class="footer-brand[^>]*>Thamarai\s*<span[^>]*>Fertility</span>\s*</span>',
        '',
        content
    )
    
    # Also remove any standalone "Thamarai Fertility" text that appears right after logo img in footer
    content = re.sub(
        r'(<img[^>]*src=["\']assets/images/logo-1\.png["\'][^>]*>)\s*Thamarai\s*Fertility',
        r'\1',
        content
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("Removing 'Thamarai Fertility' text next to logo from all pages...")
    
    html_files = glob.glob(os.path.join(BASE, '*.html'))
    html_files.extend(glob.glob(os.path.join(BASE, 'frontend', '**', '*.html'), recursive=True))
    
    fixed_count = 0
    for filepath in html_files:
        if not os.path.exists(filepath):
            continue
        try:
            if process_file(filepath):
                rel = os.path.relpath(filepath, BASE)
                print(f"  [FIXED] {rel}")
                fixed_count += 1
        except Exception as e:
            rel = os.path.relpath(filepath, BASE)
            print(f"  [ERROR] {rel}: {e}")
    
    print(f"\nTotal pages updated: {fixed_count}")
    print("Done! 'Thamarai Fertility' text removed from footer logos.")

if __name__ == '__main__':
    main()