#!/usr/bin/env python3
"""Fix broken image and icon references across all HTML pages."""
import os
import re
import glob

BASE = r'c:\Users\ELCOT\Desktop\thamarai-healthcare'

def fix_all():
    html_files = glob.glob(os.path.join(BASE, '*.html'))
    html_files.extend(glob.glob(os.path.join(BASE, 'frontend', '**', '*.html'), recursive=True))
    
    for filepath in html_files:
        if not os.path.exists(filepath):
            continue
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            
            # Fix broken loading="lazy" before src
            content = re.sub(r'loading="lazy"\s+src=', 'src=', content)
            
            # Fix src=" loading="lazy" broken pattern
            content = re.sub(r'src="\s+loading="lazy"\s+', 'src="', content)
            
            # Fix "fab fab" double class  
            content = content.replace('class="fab fab', 'class="fab')
            
            # Fix triple icon classes
            content = content.replace('fab fa-facebook-f-f', 'fab fa-facebook-f')
            content = content.replace('fab fa-linkedin-in-in', 'fab fa-linkedin-in')
            
            # Fix fa-whatsapp (should be fab fa-whatsapp)
            content = content.replace('class="fab fa-whatsapp"', 'class="fab fa-whatsapp"')
            
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                rel = os.path.relpath(filepath, BASE)
                print(f"  [FIXED] {rel}")
        except Exception as e:
            rel = os.path.relpath(filepath, BASE)
            print(f"  [ERROR] {rel}: {e}")

if __name__ == '__main__':
    print("Fixing broken references across all pages...")
    fix_all()
    print("\nDone!")