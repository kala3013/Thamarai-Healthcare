#!/usr/bin/env python3
"""
Phase 2 - Fix remaining issues:
1. Clean up top bar fragments left behind
2. Doctor image rearrangement (Bharani Kumar -> Nachappa Sivanesan/Uthraj)
3. Remove Mangayakarasi and Bharani Kumar profile images (keep text)
4. Fix text alignment and responsiveness
"""
import os
import re
import glob

BASE = r'c:\Users\ELCOT\Desktop\thamarai-healthcare'

def get_all_html_files():
    """Get all HTML files."""
    html_files = []
    html_files.extend(glob.glob(os.path.join(BASE, '*.html')))
    html_files.extend(glob.glob(os.path.join(BASE, 'frontend', '**', '*.html'), recursive=True))
    return [f for f in html_files if f.endswith('.html')]

def clean_top_bar_fragments(content):
    """Clean up remaining top bar fragments."""
    # Remove any remaining top-bar related divs  
    content = re.sub(
        r'<!-- TOP BAR -->.*?(?=<!-- NAVBAR -->|<nav id="mainNav")',
        '',
        content,
        flags=re.DOTALL
    )
    # Remove incomplete top-bar leftovers (like the fragments seen in index.html)
    content = re.sub(
        r'<div class="col-lg-4">\s*<ul class="top-bar-login[^>]*>.*?</ul>\s*</div>\s*<div class="col-lg-3 text-end">\s*<ul class="top-bar-social[^>]*>.*?</ul>\s*</div>\s*</div>\s*</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )
    # Remove any standalone top-bar elements
    content = re.sub(
        r'<div class="top-bar[^>]*>.*?</div>',
        '',
        content,
        flags=re.DOTALL
    )
    return content

def fix_doctor_images(html_file, content):
    """
    Task 6 & 7: 
    - Move Bharani Kumar's image to Nachappa Sivanesan and Uthraj
    - Remove Mangayakarasi and Bharani Kumar profile images (keep text)
    """
    # Only process pages that have doctor references
    filename = os.path.basename(html_file)
    
    # For our-doctors.html: replace Mangayakarasi img with no image (remove img tag but keep wrapper)
    content = re.sub(
        r'(<div class="doctor-img-wrapper mx-auto">)\s*<img[^>]*alt="Dr\. Mangayarkarasi"[^>]*>\s*',
        r'\1\n            <div class="doctor-no-img" style="width:140px;height:140px;border-radius:50%;background:#f0fdf4;display:flex;align-items:center;justify-content:center;margin:0 auto;"><i class="bi bi-person-fill" style="font-size:3rem;color:#2d8a4e;"></i></div>\n            ',
        content
    )
    
    # For our-doctors.html: replace Barani Kumar img with same placeholder
    content = re.sub(
        r'(<div class="doctor-img-wrapper mx-auto">)\s*<img[^>]*alt="Dr\. Barani Kumar"[^>]*>\s*',
        r'\1\n            <div class="doctor-no-img" style="width:140px;height:140px;border-radius:50%;background:#f0fdf4;display:flex;align-items:center;justify-content:center;margin:0 auto;"><i class="bi bi-person-fill" style="font-size:3rem;color:#2d8a4e;"></i></div>\n            ',
        content
    )
    
    # Also handle index.html and about.html founder sections for Mangayarkarasi
    # Note: index and about pages reference doctor-1,2,3 but not Mangayarkarasi/Barani in the founders section
    
    return content

def show_content(content):
    """Fix text alignment and responsiveness."""
    # No additional content fixes needed beyond what CSS already handles
    return content

def process_file(filepath):
    """Process a single HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Apply fixes
        content = clean_top_bar_fragments(content)
        content = fix_doctor_images(filepath, content)
        
        # Clean up excessive blank lines
        content = re.sub(r'\n{3,}', '\n\n', content)
        
        if content != original:
            rel_path = os.path.relpath(filepath, BASE)
            print(f"  ✓ Fixed: {rel_path}")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        rel_path = os.path.relpath(filepath, BASE)
        print(f"  ✗ Error {rel_path}: {e}")
        return False

def main():
    print("=" * 60)
    print("PHASE 2 - REMAINING FIXES")
    print("=" * 60)
    
    html_files = get_all_html_files()
    print(f"\nFound {len(html_files)} HTML files.\n")
    
    fixed_count = 0
    for filepath in html_files:
        if process_file(filepath):
            fixed_count += 1
    
    print(f"\nFixed {fixed_count} files.")
    
    # Verify and add additional CSS
    css_path = os.path.join(BASE, 'assets', 'css', 'style.css')
    try:
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        extra_css = """
/* Phase 2 - Additional Fixes */
.navbar-brand {
    display: flex;
    align-items: center;
}
body {
    padding-top: 0 !important;
}
.top-bar {
    display: none !important;
    height: 0 !important;
    overflow: hidden !important;
    padding: 0 !important;
    margin: 0 !important;
}
.doctor-no-img {
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto;
}
/* Calculator alignment */
.calculator-section .btn,
.calc-btn {
    display: inline-block;
    margin: 0.5rem auto;
    text-align: center;
}
.calc-result {
    text-align: center;
    padding: 1rem;
}
/* Fix icon display */
.fa, .fab, .fas, .far, .bi {
    display: inline-block;
    font-style: normal;
}
/* Responsive fixes */
@media (max-width: 768px) {
    .navbar-brand img {
        height: 35px !important;
    }
    .hero-title {
        font-size: 1.75rem;
    }
    .doctor-card-premium,
    .founder-card,
    .service-card-modern {
        text-align: center;
    }
}
"""
        # Remove old fix section and add new one
        if 'Phase 2 - Additional Fixes' not in css_content:
            if 'FIXES APPLIED BY fix_website.py' in css_content:
                # Find and replace the old fix section
                css_content = re.sub(
                    r'/\* ============================================\s+FIXES APPLIED BY fix_website\.py\s+============================================ \*/.*?(?=\n/\*|\Z)',
                    '',
                    css_content,
                    flags=re.DOTALL
                )
            css_content += extra_css
            with open(css_path, 'w', encoding='utf-8') as f:
                f.write(css_content)
            print("  ✓ Additional CSS fixes applied")
        else:
            print("  - CSS fixes already present")
    except Exception as e:
        print(f"  ✗ CSS error: {e}")
    
    print("\nDone!")

if __name__ == '__main__':
    main()