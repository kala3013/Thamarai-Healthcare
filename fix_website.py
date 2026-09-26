#!/usr/bin/env python3
"""
Thamarai Healthcare - Complete Website Fix Script
Applies all requested changes across ALL HTML pages.
"""
import os
import re
import glob

BASE = r'c:\Users\ELCOT\Desktop\thamarai-healthcare'

def get_all_html_files():
    """Get all HTML files in the base directory and subdirectories."""
    html_files = []
    # Main directory
    html_files.extend(glob.glob(os.path.join(BASE, '*.html')))
    # Frontend subdirectories
    html_files.extend(glob.glob(os.path.join(BASE, 'frontend', '**', '*.html'), recursive=True))
    # Filter out any non-HTML files
    return [f for f in html_files if f.endswith('.html')]

def fix_top_bar(content):
    """Remove the first/top tab row (TOP BAR)."""
    # Remove the top bar section - the complete div with class "top-bar"
    # Pattern 1: Standard top bar
    pattern1 = r'<!-- TOP BAR -->\s*<div class="top-bar[^>]*>.*?</div>\s*'
    content = re.sub(pattern1, '', content, flags=re.DOTALL)
    # Pattern 2: Alternative comment format
    pattern2 = r'<!-- TOP BAR .*?-->\s*<div class="top-bar[^>]*>.*?</div>\s*'
    content = re.sub(pattern2, '', content, flags=re.DOTALL)
    # Pattern 3: Any top-bar without comment
    pattern3 = r'<div class="top-bar[^>]*>.*?</div>\s*'
    content = re.sub(pattern3, '', content, flags=re.DOTALL)
    return content

def fix_navbar_logo(content):
    """Place logo before 'Home' menu item and ensure proper navbar structure."""
    # In pages that have the navbar but missing the logo/brand
    # Pattern: Find <a class="navbar-brand" ...> and ensure it exists
    if '<a class="navbar-brand"' not in content:
        # Find the nav with id="mainNav" and add logo before the first nav-item
        # This handles pages that might have the navbar-toggler before the brand
        content = re.sub(
            r'(<nav id="mainNav"[^>]*>\s*<div class="container">)',
            r'\1\n    <a class="navbar-brand" href="index.html">\n      <img src="assets/images/logo.svg" alt="Thamarai Fertility" height="45">\n    </a>',
            content
        )
    # Ensure logo has proper height attribute
    content = re.sub(
        r'(<img src="assets/images/logo\.svg" alt="[^"]*")\s*(?:height="[^"]*")?\s*/?>',
        r'\1 height="45">',
        content
    )
    return content

def fix_mindmade(content):
    """Remove 'Mindmade Technologies' from footer."""
    # Remove the entire line/paragraph containing Mindmade Technologies
    content = re.sub(
        r'<p class="mb-0 small">Design:\s*<a href="https://mindmade\.in"[^>]*>Mindmade Technologies</a></p>',
        '',
        content
    )
    # Also handle cases where it might be on same line as copyright
    content = re.sub(
        r'<div class="col-md-4 text-md-end"><p class="mb-0 small">Design:\s*<a href="https://mindmade\.in"[^>]*>Mindmade Technologies</a></p></div>',
        '',
        content
    )
    # Handle inline format
    content = re.sub(
        r'Design:\s*<a href="https://mindmade\.in"[^>]*>Mindmade Technologies</a>',
        '',
        content
    )
    # Remove any leftover empty footer-bottom rows
    content = re.sub(
        r'<div class="col-md-4 text-md-end"><p class="mb-0 small">\s*</p></div>',
        '',
        content
    )
    # Fix the footer bottom row if only copyright remains
    content = re.sub(
        r'<div class="footer-bottom">\s*<div class="row align-items-center">\s*<div class="col-md-8"><p class="mb-0 small">&copy; \d{4} Thamarai Fertility\. All Rights Reserved\.</p></div>\s*</div>\s*</div>',
        '<div class="footer-bottom">\n      <div class="row">\n        <div class="col-md-12 text-center"><p class="mb-0 small">&copy; 2026 Thamarai Fertility. All Rights Reserved.</p></div>\n      </div>\n    </div>',
        content
    )
    return content

def fix_calculators(content):
    """Fix calculator alignment - center buttons and text."""
    # Center calculator buttons
    content = re.sub(
        r'(<div[^>]*class="[^"]*calculator[^"]*"[^>]*>.*?)(<button[^>]*>.*?</button>)(.*?</div>)',
        r'\1<div class="text-center">\2</div>\3',
        content
    )
    # Add text-center to calculator result divs
    content = re.sub(
        r'(<div[^>]*id="[^"]*calc-result[^"]*"[^>]*>)',
        r'\1<div class="text-center">',
        content
    )
    return content

def fix_footer_layout(content):
    """Fix footer layout after Mindmade removal - ensure proper structure."""
    # Fix footer bottom when it lost structure
    content = re.sub(
        r'<div class="footer-bottom">\s*<div class="row[^>]*>',
        '<div class="footer-bottom">\n      <div class="row">',
        content
    )
    return content

def fix_image_paths(content):
    """Fix common image path issues."""
    # Ensure logo paths are correct
    content = re.sub(
        r'src="logo\.svg"',
        'src="assets/images/logo.svg"',
        content
    )
    content = re.sub(
        r'src="/logo\.svg"',
        'src="assets/images/logo.svg"',
        content
    )
    return content

def fix_page_header_structure(content):
    """Fix the page header/navbar structure for consistency."""
    # Ensure loading overlay exists
    if '<div id="loading"' not in content:
        content = re.sub(
            r'(<body>)',
            r'\1\n<div id="loading" class="loading-overlay"><div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div></div>\n',
            content
        )
    return content

def fix_navbar_mindmade_references(content):
    """Check if Mindmade is referenced in navbar/header areas and remove."""
    # Check for Mindmade in header/nav
    content = re.sub(
        r'Mindmade Technologies',
        '',
        content
    )
    return content

def process_file(filepath):
    """Process a single HTML file with all fixes."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Apply all fixes
        content = fix_top_bar(content)
        content = fix_navbar_logo(content)
        content = fix_mindmade(content)
        content = fix_calculators(content)
        content = fix_footer_layout(content)
        content = fix_image_paths(content)
        content = fix_page_header_structure(content)
        content = fix_navbar_mindmade_references(content)
        
        # Clean up multiple blank lines
        content = re.sub(r'\n{3,}', '\n\n', content)
        
        if content != original:
            rel_path = os.path.relpath(filepath, BASE)
            print(f"  ✓ Fixed: {rel_path}")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        else:
            return False
    except Exception as e:
        rel_path = os.path.relpath(filepath, BASE)
        print(f"  ✗ Error processing {rel_path}: {e}")
        return False

def main():
    print("=" * 60)
    print("THAMARAI HEALTHCARE - COMPLETE WEBSITE FIX")
    print("=" * 60)
    
    html_files = get_all_html_files()
    print(f"\nFound {len(html_files)} HTML files to process.\n")
    
    fixed_count = 0
    for filepath in html_files:
        if process_file(filepath):
            fixed_count += 1
    
    print(f"\n{'=' * 60}")
    print(f"Fixed {fixed_count} out of {len(html_files)} files.")
    print(f"{'=' * 60}")
    
    # Now apply CSS fixes
    print("\nApplying CSS fixes...")
    css_fixes = """
/* ============================================
   FIXES APPLIED BY fix_website.py
   ============================================ */

/* Fix top bar removal - ensure no empty space */
.top-bar {
    display: none !important;
}

/* Fix navbar alignment after top bar removal */
body {
    padding-top: 0 !important;
}
.navbar {
    top: 0 !important;
}
#mainNav.scrolled {
    top: 0 !important;
}

/* Fix footer after Mindmade removal */
.footer-bottom .col-md-12.text-center {
    text-align: center !important;
}

/* Fix calculator alignment */
.calculator-section .text-center {
    text-align: center !important;
}
.calculator-section button,
.calculator-section .btn {
    display: inline-block;
    margin: 0 auto;
}
.calc-result {
    text-align: center;
}

/* Ensure consistent logo sizing */
.navbar-brand img {
    height: 45px !important;
    width: auto !important;
}
.footer-logo img {
    height: 50px !important;
    width: auto !important;
}

/* Fix image display */
img {
    max-width: 100%;
    height: auto;
}

/* Ensure proper spacing */
.py-5 {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
}

/* Fix any broken icon references */
.fa, .fab, .fas, .far {
    display: inline-block;
}
"""
    
    css_path = os.path.join(BASE, 'assets', 'css', 'style.css')
    try:
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        # Add fixes if not already present
        if 'FIXES APPLIED BY fix_website.py' not in css_content:
            css_content += css_fixes
            with open(css_path, 'w', encoding='utf-8') as f:
                f.write(css_content)
            print("  ✓ CSS fixes applied to style.css")
        else:
            print("  - CSS fixes already present in style.css")
    except Exception as e:
        print(f"  ✗ Error updating CSS: {e}")
    
    print(f"\n{'=' * 60}")
    print("FIX COMPLETE!")
    print(f"{'=' * 60}")

if __name__ == '__main__':
    main()