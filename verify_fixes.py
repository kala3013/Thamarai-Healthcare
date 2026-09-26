#!/usr/bin/env python3
"""Verify all fixes were applied correctly."""
import glob
import os

BASE = r'c:\Users\ELCOT\Desktop\thamarai-healthcare'

# Get all HTML files
files = glob.glob(os.path.join(BASE, '*.html'))
files += glob.glob(os.path.join(BASE, 'frontend', '**', '*.html'), recursive=True)

count_topbar = 0
count_mindmade = 0
count_logo = 0
count_empty_footer = 0
total = 0

for f in files:
    try:
        content = open(f, 'r', encoding='utf-8').read()
        total += 1
        
        # Check for top-bar class
        if 'class="top-bar' in content or "class='top-bar" in content:
            count_topbar += 1
            print(f"  TOP BAR STILL EXISTS: {os.path.relpath(f, BASE)}")
        
        # Check for Mindmade
        if 'Mindmade' in content:
            count_mindmade += 1
            print(f"  MINDMADE STILL EXISTS: {os.path.relpath(f, BASE)}")
        
        # Check for navbar brand logo
        if 'navbar-brand' in content:
            count_logo += 1
        
        # Check for empty footer divs
        if '<div class="col-md-4 text-md-end"></div>' in content or "<div class='col-md-4 text-md-end'></div>" in content:
            count_empty_footer += 1
            print(f"  EMPTY FOOTER DIV: {os.path.relpath(f, BASE)}")
    except:
        pass

print(f"\n=== VERIFICATION RESULTS ===")
print(f"Total files scanned: {total}")
print(f"Files with top-bar remaining: {count_topbar}")
print(f"Files with Mindmade remaining: {count_mindmade}")
print(f"Files with navbar brand: {count_logo}")
print(f"Files with empty footer divs: {count_empty_footer}")
print(f"\nTop bar removal: {'✓ PASS' if count_topbar == 0 else '✗ FAIL'}")
print(f"Mindmade removal: {'✓ PASS' if count_mindmade == 0 else '✗ FAIL'}")
print(f"Logo in navbar: {'✓ PASS' if count_logo > 0 else '✗ FAIL'}")
print(f"Empty footer divs: {'✓ PASS' if count_empty_footer == 0 else '✗ FAIL'}")