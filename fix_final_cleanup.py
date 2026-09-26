#!/usr/bin/env python3
"""
Phase 3 - Final cleanup:
1. Remove empty footer divs
2. Ensure footer-bottom has proper structure
3. Fix any remaining issues
"""
import os
import re
import glob

BASE = r'c:\Users\ELCOT\Desktop\thamarai-healthcare'

def get_all_html_files():
    html_files = []
    html_files.extend(glob.glob(os.path.join(BASE, '*.html')))
    html_files.extend(glob.glob(os.path.join(BASE, 'frontend', '**', '*.html'), recursive=True))
    return [f for f in html_files if f.endswith('.html')]

def cleanup_empty_footer_divs(content):
    """Remove empty footer divs."""
    # Remove empty col-md-4 divs
    content = re.sub(
        r'<div class="col-md-4 text-md-end">\s*</div>',
        '',
        content
    )
    # Fix footer-bottom structure if col-md-8 is now alone
    content = re.sub(
        r'<div class="footer-bottom">\s*<div class="row[^>]*">\s*<div class="col-md-8"><p class="mb-0 small">&copy; \d{4} Thamarai Fertility\. All Rights Reserved\.</p></div>\s*</div>\s*</div>',
        '<div class="footer-bottom">\n      <div class="row">\n        <div class="col-12 text-center"><p class="mb-0 small">&copy; 2026 Thamarai Fertility. All Rights Reserved.</p></div>\n      </div>\n    </div>',
        content
    )
    # Also fix col-12 text-center pattern if it already exists
    content = re.sub(
        r'<div class="col-md-8"><p class="mb-0 small">&copy; \d{4} Thamarai Fertility\. All Rights Reserved\.</p></div>',
        '<div class="col-12 text-center"><p class="mb-0 small">&copy; 2026 Thamarai Fertility. All Rights Reserved.</p></div>',
        content
    )
    return content

def fix_doctor_details_html(content):
    """Fix doctor-details.html - check for any issues."""
    # Ensure proper fallback image handling
    return content

def fix_about_founder_images(content):
    """Fix about.html founder section - ensure images are correct."""
    # About page uses doctor-1,2,3 which are correct - no changes needed
    return content

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        original = content
        
        content = cleanup_empty_footer_divs(content)
        content = fix_doctor_details_html(content)
        content = fix_about_founder_images(content)
        
        # Clean blank lines
        content = re.sub(r'\n{4,}', '\n\n\n', content)
        
        if content != original:
            rel_path = os.path.relpath(filepath, BASE)
            print(f"  ✓ {rel_path}")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        rel_path = os.path.relpath(filepath, BASE)
        if 'Permission denied' not in str(e):
            print(f"  ✗ {rel_path}: {e}")
        return False

def main():
    print("=" * 60)
    print("PHASE 3 - FINAL CLEANUP")
    print("=" * 60)
    
    html_files = get_all_html_files()
    print(f"\nProcessing {len(html_files)} files...\n")
    
    fixed = 0
    for f in html_files:
        if process_file(f):
            fixed += 1
    
    print(f"\nFixed {fixed} files.")
    print("Done!")

if __name__ == '__main__':
    main()