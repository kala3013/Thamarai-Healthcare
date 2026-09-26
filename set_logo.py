#!/usr/bin/env python3
"""Replace all logo references with logo-1.png across the entire website."""
import os
import re
import glob

BASE = r'c:\Users\ELCOT\Desktop\thamarai-healthcare'

def process_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Replace all SVG logo references with logo-1.png
    content = content.replace('src="assets/images/thamarai-logo.svg"', 'src="assets/images/logo-1.png"')
    content = content.replace("src='assets/images/thamarai-logo.svg'", "src='assets/images/logo-1.png'")
    content = content.replace('src="assets/images/logo.svg"', 'src="assets/images/logo-1.png"')
    content = content.replace("src='assets/images/logo.svg'", "src='assets/images/logo-1.png'")
    
    # Update favicon references
    content = content.replace('href="assets/images/logo.svg"', 'href="assets/images/logo-1.png"')
    content = content.replace("href='assets/images/logo.svg'", "href='assets/images/logo-1.png'")
    
    # Update Open Graph image references
    content = content.replace('content="assets/images/logo.svg"', 'content="assets/images/logo-1.png"')
    content = content.replace("content='assets/images/logo.svg'", "content='assets/images/logo-1.png'")
    content = content.replace('content="assets/images/thamarai-logo.svg"', 'content="assets/images/logo-1.png"')
    content = content.replace("content='assets/images/thamarai-logo.svg'", "content='assets/images/logo-1.png'")
    
    # Update schema.org logo
    content = content.replace('"logo": "https://thamaraihealthcare.com/assets/images/logo.svg"', '"logo": "https://thamaraihealthcare.com/assets/images/logo-1.png"')
    
    # Add proper alt text for logo-1.png if missing
    content = re.sub(
        r'(<img[^>]*src=["\']assets/images/logo-1\.png["\'][^>]*)(alt="[^"]*")?([^>]*>)',
        lambda m: m.group(1) + (' alt="Thamarai Fertility Logo"' if not m.group(2) else m.group(2)) + m.group(3),
        content
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def process_css(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Replace SVG logo references in CSS
    content = content.replace('thamarai-logo.svg', 'logo-1.png')
    content = content.replace('logo.svg', 'logo-1.png')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("=" * 60)
    print("SETTING LOGO-1.PNG AS WEBSITE LOGO")
    print("=" * 60)
    
    # Process all HTML files
    html_files = glob.glob(os.path.join(BASE, '*.html'))
    html_files.extend(glob.glob(os.path.join(BASE, 'frontend', '**', '*.html'), recursive=True))
    
    fixed_count = 0
    for filepath in html_files:
        if not os.path.exists(filepath):
            continue
        try:
            if process_html(filepath):
                rel = os.path.relpath(filepath, BASE)
                print(f"  [FIXED] {rel}")
                fixed_count += 1
        except Exception as e:
            rel = os.path.relpath(filepath, BASE)
            print(f"  [ERROR] {rel}: {e}")
    
    # Process CSS files
    css_files = glob.glob(os.path.join(BASE, 'assets', 'css', '*.css'))
    for filepath in css_files:
        if not os.path.exists(filepath):
            continue
        try:
            if process_css(filepath):
                rel = os.path.relpath(filepath, BASE)
                print(f"  [FIXED CSS] {rel}")
                fixed_count += 1
        except Exception as e:
            pass
    
    print(f"\nTotal files updated: {fixed_count}")
    print("Logo replacement complete! logo-1.png is now used everywhere.")

if __name__ == '__main__':
    main()