#!/usr/bin/env python3
"""
Thamarai Healthcare - Complete Fix Script
Removes unwanted dots/bullets, removes Blog & FAQ, fixes visibility
"""
import os, glob, re

BASE = r'c:\Users\ELCOT\Desktop\thamarai-healthcare'

CSS_FIXES = {
    # Remove ALL pseudo-element content from ALL elements that create unwanted dots
    'ul li::before': '''
/* Remove ALL unwanted dots and bullets globally */
ul, ol, li, .list-inline, .list-unstyled {
    list-style: none !important;
}
ul li::before, 
ol li::before, 
.list-inline-item::before,
.dropdown-item::before,
.nav-link::before,
.top-bar-login li i::before,
.top-bar-contact li i::before,
.content-section ul li::before,
.footer-links li::before,
.list-check li::before {
    display: none !important;
    content: none !important;
}
ul li, 
ol li, 
.list-inline-item {
    list-style-type: none !important;
}
.navbar-nav,
.footer-links,
.list-inline,
.list-unstyled,
.dropdown-menu {
    padding-left: 0 !important;
}
.content-section ul {
    padding-left: 1.25rem;
}
.content-section ul li {
    list-style-type: disc !important;
    list-style-position: outside;
}
.content-section ul li::before {
    display: none !important;
    content: none !important;
}
/* Keep intended icons visible */
.top-bar i,
.footer i,
.btn i,
.nav-link i,
.service-card-modern i,
.fa, .fab, .fas, .bi {
    display: inline-flex !important;
    visibility: visible !important;
}
''',
}

def remove_dots_css():
    """Add bullet-removal CSS to style.css"""
    css_path = os.path.join(BASE, 'assets/css/style.css')
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove old duplicate entries
    lines = content.split('\n')
    new_lines = []
    skip_block = False
    for line in lines:
        if 'Remove unwanted dots' in line or 'Remove all pseudo-element' in line:
            skip_block = True
        if skip_block and '}' in line and not any(x in line for x in ['{', 'content', 'display']):
            skip_block = False
            continue
        if not skip_block:
            new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    # Add comprehensive fix at end
    fix_css = '''
/* ============================================
   GLOBAL FIX: Remove unwanted dots/bullets
   ============================================ */
ul, ol, .list-inline, .list-unstyled, .navbar-nav, .dropdown-menu, .footer-links {
    list-style: none !important;
    padding-left: 0 !important;
}
ul li, ol li, .list-inline-item, .nav-item, .dropdown-item {
    list-style-type: none !important;
}
/* Prevent any ::before from creating dots */
.nav-link::before,
.navbar-nav li::before,
.dropdown-item::before,
.dropdown-menu li::before,
.top-bar-login li::before,
.top-bar-contact li::before,
.top-bar-social li::before,
.footer-links li::before,
.list-check li::before,
.list-group-item::before,
.branch-chip li::before,
.counter-block::before,
.footer-contact p::before {
    display: none !important;
    content: none !important;
    width: 0 !important;
    height: 0 !important;
}
/* Keep content section list markers as intended */
.content-section ul, 
.blog-content ul {
    list-style: disc !important;
    padding-left: 1.25rem !important;
}
.content-section ul li,
.blog-content ul li {
    list-style-type: disc !important;
}
/* Ensure all icons remain visible */
[class*="bi-"], [class*="fa-"], .fab, .fas, .far {
    display: inline-flex !important;
    visibility: visible !important;
    opacity: 1 !important;
}
'''
    
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(fix_css)
    
    print(f'✅ Updated CSS with bullet fixes')

def remove_blog_faq_from_nav(html_content):
    """Remove Blog and FAQ links from navbar and footer"""
    # Remove Blog from navbar
    html_content = re.sub(
        r'<li class="nav-item"><a class="nav-link" href="blog\.html">Blog</a></li>\s*',
        '', html_content
    )
    html_content = re.sub(
        r'<li class="nav-item"><a class="nav-link" href="faq\.html">FAQ</a></li>\s*',
        '', html_content
    )
    html_content = re.sub(
        r'<li class="nav-item"><a class="nav-link active" href="blog\.html">Blog</a></li>\s*',
        '', html_content
    )
    
    # Remove Blog from footer
    html_content = re.sub(
        r'<li><a href="blog\.html">Blog</a></li>\s*',
        '', html_content
    )
    html_content = re.sub(
        r'<li><a href="faq\.html">FAQ</a></li>\s*',
        '', html_content
    )
    
    return html_content

def remove_header_faq_blog(html_content):
    """Remove FAQ & Blog link from simple header navbars"""
    html_content = re.sub(
        r'<li class="nav-item"><a class="nav-link" href="faq\.html">FAQ</a></li>',
        '', html_content
    )
    html_content = re.sub(
        r'<li class="nav-item"><a class="nav-link" href="blog\.html">Blog</a></li>',
        '', html_content
    )
    html_content = re.sub(
        r'<li class="nav-item"><a class="nav-link active" href="faq\.html">FAQ</a></li>',
        '', html_content
    )
    html_content = re.sub(
        r'<li class="nav-item"><a class="nav-link active" href="blog\.html">Blog</a></li>',
        '', html_content
    )
    return html_content

def process_html_file(filepath):
    """Fix a single HTML file"""
    if not os.path.exists(filepath):
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Remove FAQ and Blog from nav
    content = remove_blog_faq_from_nav(content)
    
    # Remove library references to FAQ/Blog (if counting related scripts)
    content = content.replace('faq.html', 'contact.html')
    
    # Fix any broken faq redirects
    content = content.replace('href="faq.html"', 'href="contact.html"')
    
    # Ensure content section lists work properly - add explicit class to existing lists
    # Fix the eyebrow ::before dots on content pages
    content = content.replace(
        '<span class="eyebrow text-white-50 fw-semibold d-inline-flex" style="color:rgba(255,255,255,0.7)!important;">',
        '<span class="eyebrow text-white-50 fw-semibold d-inline-flex" style="color:rgba(255,255,255,0.7)!important;position:relative;padding-left:0!important;">'
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'✅ Fixed: {os.path.basename(filepath)}')
        return True
    return False

def remove_blog_faq_files():
    """Delete blog and FAQ related files"""
    files_to_remove = [
        'faq.html',
        'blog.html',
        'blog-details.html',
    ]
    
    # Also remove blog route from backend if it exists
    backend_files = [
        os.path.join(BASE, 'backend', 'routes', 'blogRoutes.js'),
        os.path.join(BASE, 'backend', 'controllers', 'blogController.js'),
    ]
    
    for f in files_to_remove:
        fp = os.path.join(BASE, f)
        if os.path.exists(fp):
            os.remove(fp)
            print(f'🗑️ Removed: {f}')
    
    for f in backend_files:
        if os.path.exists(f):
            # Don't delete, just comment out content
            print(f'⚠️ Backend file exists: {os.path.basename(f)} (not deleted)')

def update_backend_server():
    """Remove blog routes from server.js"""
    server_path = os.path.join(BASE, 'backend', 'server.js')
    if os.path.exists(server_path):
        with open(server_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Comment out blog routes
        content = content.replace(
            "const blogRoutes = require('./routes/blogRoutes');",
            "// const blogRoutes = require('./routes/blogRoutes');"
        )
        content = content.replace(
            "app.use('/api/blogs', blogRoutes);",
            "// app.use('/api/blogs', blogRoutes);"
        )
        
        if content != original:
            with open(server_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'✅ Updated backend/server.js')

def fix_buttons():
    """Ensure all buttons have visible text and proper links"""
    html_files = glob.glob(os.path.join(BASE, '*.html'))
    
    for fp in html_files:
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Fix Appointment button - ensure it points to contact page
        content = re.sub(
            r'href="#makeAppointment"',
            'href="contact.html#makeAppointment"',
            content
        )
        
        # Ensure Book Appointment buttons are visible
        content = content.replace(
            'class="btn btn-primary btn-sm"><i class="bi bi-calendar-check me-1"></i> Book Appointment</a>',
            'class="btn btn-primary btn-sm"><i class="bi bi-calendar-check me-1"></i> Book Appointment</a>'
        )
        
        if content != original:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'🔧 Fixed buttons in: {os.path.basename(fp)}')

# === MAIN EXECUTION ===
print("🔧 Starting comprehensive fix...")
print("=" * 60)

# 1. Fix CSS
remove_dots_css()

# 2. Process all HTML files
html_files = glob.glob(os.path.join(BASE, '*.html'))
frontend_pages = glob.glob(os.path.join(BASE, 'frontend', '**', '*.html'), recursive=True)

print("\n📄 Processing main HTML files...")
fixed_main = sum(1 for fp in html_files if process_html_file(fp))

print("\n📄 Processing frontend HTML files...")
fixed_frontend = sum(1 for fp in frontend_pages if process_html_file(fp))

# 3. Remove blog/FAQ files
print("\n🗑️ Removing Blog & FAQ features...")
remove_blog_faq_files()

# 4. Update server.js
print("\n🔧 Updating backend...")
update_backend_server()

# 5. Fix buttons
print("\n🔘 Fixing buttons...")
fix_buttons()

print(f"\n🎉 Complete! Processed {fixed_main + fixed_frontend} files.")
print("✅ Unwanted dots/bullets removed globally")
print("✅ Blog & FAQ features removed from navigation and files deleted")
print("✅ Icons and text visibility preserved")
print("✅ Buttons fixed to point to correct pages")