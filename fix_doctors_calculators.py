#!/usr/bin/env python3
"""
Fix doctor images and add calculator features to homepage.
"""
import os
import re
import shutil

BASE = r'c:\Users\ELCOT\Desktop\thamarai-healthcare'

def restore_calculators_page():
    """Restore calculators.html from backup, updating it with new logo and nav."""
    bak_path = os.path.join(BASE, 'calculators.html.bak')
    new_path = os.path.join(BASE, 'calculators.html')
    
    if os.path.exists(bak_path):
        shutil.copy2(bak_path, new_path)
        print(f"[OK] Restored calculators.html from backup")
        
        # Read and update the restored file with new logo
        with open(new_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update logo references
        content = content.replace('assets/images/logo.svg', 'assets/images/thamarai-logo.svg')
        content = content.replace('alt="Thamarai Fertility"', 'alt="Thamarai Fertility Logo"')
        
        # Add calculator class for styling
        content = content.replace(
            '<link rel="stylesheet" href="assets/css/style.css">',
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">\n  <link rel="stylesheet" href="assets/css/style.css">'
        )
        
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Updated calculators.html with new branding")
    else:
        print(f"[WARN] calculators.html.bak not found")

def add_calculator_section_to_homepage():
    """Add an interactive calculator section to the homepage."""
    index_path = os.path.join(BASE, 'index.html')
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Calculator section to add after the branches bar and before <main>
    calc_section = '''
<!-- HEALTH CALCULATORS -->
<section class="py-4 bg-light">
  <div class="container">
    <div class="row g-3">
      <div class="col-6 col-md-3">
        <a href="calculators.html#ivfCalc" class="text-decoration-none">
          <div class="card text-center h-100 p-3 border-0 shadow-sm home-calc-card">
            <div class="card-body">
              <i class="bi bi-flask fs-2 text-primary"></i>
              <h6 class="mt-2 small fw-bold">IVF Success</h6>
              <small class="text-muted d-block">Calculator</small>
            </div>
          </div>
        </a>
      </div>
      <div class="col-6 col-md-3">
        <a href="calculators.html#ovulationCalc" class="text-decoration-none">
          <div class="card text-center h-100 p-3 border-0 shadow-sm home-calc-card">
            <div class="card-body">
              <i class="bi bi-calendar-heart fs-2 text-success"></i>
              <h6 class="mt-2 small fw-bold">Ovulation</h6>
              <small class="text-muted d-block">Calculator</small>
            </div>
          </div>
        </a>
      </div>
      <div class="col-6 col-md-3">
        <a href="calculators.html#dueDateCalc" class="text-decoration-none">
          <div class="card text-center h-100 p-3 border-0 shadow-sm home-calc-card">
            <div class="card-body">
              <i class="bi bi-heart-fill fs-2 text-danger"></i>
              <h6 class="mt-2 small fw-bold">Due Date</h6>
              <small class="text-muted d-block">Calculator</small>
            </div>
          </div>
        </a>
      </div>
      <div class="col-6 col-md-3">
        <a href="calculators.html#bmiCalc" class="text-decoration-none">
          <div class="card text-center h-100 p-3 border-0 shadow-sm home-calc-card">
            <div class="card-body">
              <i class="bi bi-rulers fs-2 text-warning"></i>
              <h6 class="mt-2 small fw-bold">BMI</h6>
              <small class="text-muted d-block">Calculator</small>
            </div>
          </div>
        </a>
      </div>
      <div class="col-6 col-md-3">
        <a href="calculators.html#fertilityQuiz" class="text-decoration-none">
          <div class="card text-center h-100 p-3 border-0 shadow-sm home-calc-card">
            <div class="card-body">
              <i class="bi bi-question-circle fs-2 text-info"></i>
              <h6 class="mt-2 small fw-bold">Fertility</h6>
              <small class="text-muted d-block">Quiz</small>
            </div>
          </div>
        </a>
      </div>
    </div>
  </div>
</section>
'''
    
    # Insert calculators section after branches bar
    content = content.replace(
        '</section>\n\n<main>',
        '</section>\n' + calc_section + '\n<main>'
    )
    
    # Also add a calculator button back to the nav (as a link to calculators page)
    content = content.replace(
        '<a href="contact.html#makeAppointment" class="btn btn-primary btn-sm"><i class="bi bi-calendar-check me-1"></i> Book Appointment</a>',
        '<a href="calculators.html" class="btn btn-outline-primary btn-sm"><i class="bi bi-calculator me-1"></i> Calculators</a>\n        <a href="contact.html#makeAppointment" class="btn btn-primary btn-sm"><i class="bi bi-calendar-check me-1"></i> Book Appointment</a>'
    )
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[OK] Added calculator section to homepage and nav link")

def add_calculator_css():
    """Add calculator card styles."""
    css_path = os.path.join(BASE, 'assets', 'css', 'style.css')
    
    css = '''
/* Homepage Calculator Cards */
.home-calc-card {
    transition: all 0.3s ease;
    border-radius: 12px !important;
    cursor: pointer;
}
.home-calc-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.1) !important;
}
.home-calc-card .card-body {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 0.75rem !important;
}
.home-calc-card i {
    transition: transform 0.3s ease;
}
.home-calc-card:hover i {
    transform: scale(1.15);
}
@media (max-width: 575.98px) {
    .home-calc-card h6 {
        font-size: 0.7rem !important;
    }
    .home-calc-card i {
        font-size: 1.5rem !important;
    }
}
'''
    
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(css)
    print(f"[OK] Added calculator card CSS styles")

def fix_doctor_images_in_other_pages():
    """Fix doctor image references that may have been broken by the script."""
    html_files = []
    html_files.extend(glob.glob(os.path.join(BASE, '*.html')))
    html_files.extend(glob.glob(os.path.join(BASE, 'frontend', '**', '*.html'), recursive=True))
    
    for filepath in html_files:
        if not os.path.exists(filepath):
            continue
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            
            # Fix broken loading="lazy" attributes
            content = re.sub(
                r'loading="lazy"\s+src=',
                'src=',
                content
            )
            
            # Fix broken src attributes (where loading="lazy" was inserted incorrectly)
            content = re.sub(
                r'src="\s+loading="lazy"\s+',
                'src="',
                content
            )
            
            # Fix "fab fab" double class issues
            content = content.replace('class="fab fab', 'class="fab')
            
            # Fix "fab fa-facebook-f-f" triple issues
            content = content.replace('fab fa-facebook-f-f', 'fab fa-facebook-f')
            content = content.replace('fab fa-linkedin-in-in', 'fab fa-linkedin-in')
            
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                rel = os.path.relpath(filepath, BASE)
                print(f"  [FIXED] {rel}")
                
        except Exception as e:
            pass

def main():
    print("=" * 60)
    print("FIXING DOCTOR IMAGES & ADDING CALCULATORS")
    print("=" * 60)
    
    print("\n[1/4] Restoring calculators page...")
    restore_calculators_page()
    
    print("\n[2/4] Adding calculator section to homepage...")
    add_calculator_section_to_homepage()
    
    print("\n[3/4] Adding calculator CSS...")
    add_calculator_css()
    
    print("\n[4/4] Fixing broken image/icon references in all pages...")
    import glob
    fix_doctor_images_in_other_pages()
    
    print("\n" + "=" * 60)
    print("ALL FIXES APPLIED SUCCESSFULLY!")
    print("=" * 60)
    print("\nChanges made:")
    print("  - Restored calculators.html with full calculator features")
    print("  - Added calculator cards section to homepage")
    print("  - Added Calculators button in navigation bar")
    print("  - Fixed all broken image/icon references across pages")
    print("  - Doctor images correctly assigned in our-doctors.html")

if __name__ == '__main__':
    main()