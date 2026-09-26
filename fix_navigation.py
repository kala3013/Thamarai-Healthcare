#!/usr/bin/env python3
"""
Thamarai Healthcare - Complete Navigation & Link Fix
Fixes all broken links, connects dropdown items to correct pages
"""
import os, glob

BASE = r'c:\Users\ELCOT\Desktop\thamarai-healthcare'

# === CORRECT LINK MAPPINGS ===
# Maps current (often wrong) href -> correct href for each dropdown text

LINK_FIXES = {
    # --- Profile ---
    'our-doctors.html': 'our-doctors.html',
    'about.html': 'about.html',
    'success-stories.html': 'success-stories.html',
    'gallery.html': 'gallery.html',
    'achievements.html': 'achievements.html',
    
    # --- Fertility ---
    'fertility-basics.html': 'fertility-basics.html',
    
    # --- Disorders of Fertility (submenu) ---
    'male-factor.html': 'male-factor.html',
    'uterine-factor.html': 'uterine-factor.html',
    'ovulatory-factor.html': 'ovulatory-factor.html',
    'tubal-factor.html': 'tubal-factor.html',
    'pelvic-factor.html': 'pelvic-factor.html',
    'coital-factor.html': 'coital-factor.html',
    
    # --- Tests - Ovulation ---
    'baseline-scan.html': 'baseline-scan.html',
    'hormonal-assay.html': 'hormonal-assay.html',
    'hormone-testing.html': 'hormone-testing.html',
    
    # --- Tests - Sperm ---
    'semen-analysis.html': 'semen-analysis.html',
    'y-chromosome-deletion.html': 'y-chromosome-deletion.html',
    'sperm-dna-fragmentation.html': 'sperm-dna-fragmentation.html',
    'karyotyping.html': 'karyotyping.html',
    
    # --- Tests - Tubes & Uterus ---
    'fibroid-assessment.html': 'fibroids.html',
    'sonohysterosalpingogram.html': 'sonohysterosalpingogram.html',
    
    # --- Tests - Pelvis ---
    'pelvic-scan.html': 'pelvic-scan.html',
    
    # --- Procedures - Ovarian Stimulation ---
    'ovarian-stimulation.html': 'ovarian-stimulation.html',
    'iui.html': 'iui.html',
    'ivf.html': 'ivf.html',
    
    # --- Procedures - IUI ---
    'iui.html': 'iui.html',
    
    # --- Procedures - Sperm Freezing ---
    'sperm-freezing.html': 'sperm-freezing.html',
    
    # --- Procedures - IVF/ICSI ---
    'icsi.html': 'icsi.html',
    
    # --- Procedures - Embryo ---
    'embryo-freezing.html': 'embryo-freezing.html',
    
    # --- Procedures - Advanced ---
    'pgd.html': 'pgd.html',
    'egg-donation.html': 'egg-donation.html',
    'surrogacy.html': 'surrogacy.html',
    
    # --- Clinics - Obstetrics ---
    'high-risk-pregnancy.html': 'high-risk-pregnancy.html',
    'pregnancy-care.html': 'pregnancy-care.html',
    'postnatal-care.html': 'postnatal-care.html',
    
    # --- Clinics - Gynecology ---
    'cancer-screening.html': 'cancer-screening.html',
    'menopause.html': 'menopause.html',
    'pcos.html': 'pcos.html',
    'endometriosis.html': 'endometriosis.html',
    'fibroids.html': 'fibroids.html',
    'menstrual-disorders.html': 'menstrual-disorders.html',
    
    # --- Clinics - Fetal Medicine ---
    'fetal-medicine.html': 'fetal-medicine.html',
    
    # --- Clinics - Genetic ---
    'genetic-clinic.html': 'genetic-clinic.html',
    
    # --- Clinics - Special ---
    'adolescence.html': 'adolescence.html',
    'endoscopy-clinic.html': 'endoscopy-clinic.html',
    'andrology-clinic.html': 'andrology-clinic.html',
    
    # --- Clinics - Counselling ---
    'counselling.html': 'counselling.html',
    
    # --- Other ---
    'events.html': 'events.html',
    'blog.html': 'blog.html',
    'contact.html': 'contact.html',
    'calculators.html': 'calculators.html',
    'branch-coimbatore.html': 'branch-coimbatore.html',
    'branch-chennai.html': 'branch-chennai.html',
    'branch-salem.html': 'branch-salem.html',
    'branch-tiruppur.html': 'branch-tiruppur.html',
    'branch-pollachi.html': 'branch-pollachi.html',
    'fertility-preservation.html': 'fertility-preservation.html',
    'breastfeeding-support.html': 'breastfeeding-support.html',
    'pediatrics.html': 'pediatrics.html',
    'neonatology.html': 'neonatology.html',
}

# === HREF FIX MAP ===
# Maps specific wrong href patterns to correct ones based on link text context
HREF_CONTEXT_FIXES = [
    # ---- FERTILITY MENU ----
    # Tests menu items currently point to wrong pages
    ('href="fertility-basics.html">Baseline Scan', 'href="baseline-scan.html">Baseline Scan'),
    ('href="fertility-basics.html">Hormonal Assay', 'href="hormonal-assay.html">Hormonal Assay'),
    ('href="fertility-basics.html">Hormone Test', 'href="hormone-testing.html">Hormone Test'),
    ('href="fertility-basics.html">Hormone Testing', 'href="hormone-testing.html">Hormone Testing'),
    
    # Sperm tests currently point to male-factor.html
    ('href="male-factor.html">Semen Analysis', 'href="semen-analysis.html">Semen Analysis'),
    ('href="male-factor.html">Y Chromosome', 'href="y-chromosome-deletion.html">Y Chromosome Micro Deletion'),
    ('href="male-factor.html">Sperm DNA', 'href="sperm-dna-fragmentation.html">Sperm DNA Fragmentation'),
    ('href="male-factor.html">Karyotyping', 'href="karyotyping.html">Karyotyping'),
    
    # Tube/Uterus tests
    ('href="uterine-factor.html">Test for Fibroid', 'href="fibroids.html">Fibroid Assessment'),
    ('href="uterine-factor.html">3D Sonohysterosalpingogram', 'href="sonohysterosalpingogram.html">3D Sonohysterosalpingogram'),
    
    # Pelvis test
    ('href="pelvic-factor.html">Test for Pelvis', 'href="pelvic-scan.html">Pelvic Scan & Evaluation'),
    
    # ---- PROCEDURES ----
    ('href="iui.html">For IUI', 'href="ovarian-stimulation.html">For IUI'),
    ('href="ivf.html">For ART', 'href="ovarian-stimulation.html">For ART'),
    ('href="ivf.html">Ovarian Hyperstimulation', 'href="ovarian-stimulation.html">Ovarian Hyperstimulation'),
    ('href="ivf.html">IVF', 'href="ivf.html">IVF - Egg Retrieval'),
    ('href="ivf.html">Fertilization', 'href="ivf.html">Fertilization & Embryo Culture'),
    ('href="ivf.html">Embryo Transfer', 'href="ivf.html">Embryo Transfer'),
    
    # ---- CLINICS ----
    ('href="high-risk-pregnancy.html">Post Natal Clinic', 'href="postnatal-care.html">Post Natal Clinic'),
    ('href="high-risk-pregnancy.html">Early Pregnancy', 'href="pregnancy-care.html">Early Pregnancy Assessment'),
    ('href="high-risk-pregnancy.html">Recurrent Pregnancy', 'href="pregnancy-care.html">Recurrent Pregnancy Loss'),
    ('href="high-risk-pregnancy.html">AUB Clinic', 'href="menstrual-disorders.html">AUB Clinic'),
    ('href="high-risk-pregnancy.html">Contraception', 'href="menstrual-disorders.html">Contraception'),
    ('href="high-risk-pregnancy.html">Obesity', 'href="pcos.html">Obesity Clinic'),
    ('href="high-risk-pregnancy.html">Cosmetology', 'href="pcos.html">Cosmetology'),
    
    # Patient/Staff Login links
    ('href="http://bd733462.ngrok.io/user/doctorlogin"', 'href="/frontend/staff/login.html"'),
    ('href="http://bd733462.ngrok.io/user/patientlogin"', 'href="/frontend/patient/login.html"'),
]

def fix_html_file(filepath):
    """Fix all navigation links in a single HTML file"""
    if not os.path.exists(filepath):
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # Apply all context-based fixes
    for old, new in HREF_CONTEXT_FIXES:
        if old in content:
            content = content.replace(old, new)
            changes.append(f'  Fixed: {old[:50]}... -> {new[:50]}...')
    
    # Fix any remaining broken links where wrong pages are linked
    # e.g. Tests menu items pointing to fertility-basics.html instead of their dedicated pages
    wrong_links = [
        # Test links
        ('href="fertility-basics.html" class="dropdown-item">Baseline Scan & Follicular Study</a>', 
         'href="baseline-scan.html" class="dropdown-item">Baseline Scan & Follicular Study</a>'),
        ('href="fertility-basics.html" class="dropdown-item">Hormonal Assay</a>', 
         'href="hormonal-assay.html" class="dropdown-item">Hormonal Assay</a>'),
        ('href="fertility-basics.html" class="dropdown-item">Hormone Test</a>', 
         'href="hormone-testing.html" class="dropdown-item">Hormone Testing</a>'),
        
        # Test for Sperm links
        ('href="male-factor.html" class="dropdown-item">Semen Analysis</a>', 
         'href="semen-analysis.html" class="dropdown-item">Semen Analysis</a>'),
        ('href="male-factor.html" class="dropdown-item">Y Chromosome Micro Deletion</a>', 
         'href="y-chromosome-deletion.html" class="dropdown-item">Y Chromosome Micro Deletion</a>'),
        ('href="male-factor.html" class="dropdown-item">Sperm DNA Fragmentation</a>', 
         'href="sperm-dna-fragmentation.html" class="dropdown-item">Sperm DNA Fragmentation</a>'),
        ('href="male-factor.html" class="dropdown-item">Karyotyping</a>', 
         'href="karyotyping.html" class="dropdown-item">Karyotyping</a>'),
        
        # Test for Tubes & Uterus
        ('href="uterine-factor.html" class="dropdown-item">Test for Fibroid</a>', 
         'href="fibroids.html" class="dropdown-item">Fibroid Assessment</a>'),
        ('href="uterine-factor.html" class="dropdown-item">3D Sonohysterosalpingogram</a>', 
         'href="sonohysterosalpingogram.html" class="dropdown-item">3D Sonohysterosalpingogram</a>'),
        
        # Pelvis
        ('href="pelvic-factor.html" class="dropdown-item">Test for Pelvis</a>', 
         'href="pelvic-scan.html" class="dropdown-item">Pelvic Scan & Evaluation</a>'),
        
        # Procedures - Ovarian Stimulation
        ('href="iui.html" class="dropdown-item">For IUI</a>', 
         'href="ovarian-stimulation.html" class="dropdown-item">For IUI</a>'),
        ('href="ivf.html" class="dropdown-item">For ART</a>', 
         'href="ovarian-stimulation.html" class="dropdown-item">For ART</a>'),
        ('href="ivf.html" class="dropdown-item">Ovarian Hyperstimulation</a>', 
         'href="ovarian-stimulation.html" class="dropdown-item">Ovarian Hyperstimulation</a>'),
        
        # Obstetrics
        ('href="high-risk-pregnancy.html" class="dropdown-item">Post Natal Clinic</a>', 
         'href="postnatal-care.html" class="dropdown-item">Post Natal Clinic</a>'),
        ('href="high-risk-pregnancy.html" class="dropdown-item">Early Pregnancy Assessment</a>', 
         'href="pregnancy-care.html" class="dropdown-item">Early Pregnancy Assessment</a>'),
        ('href="high-risk-pregnancy.html" class="dropdown-item">Recurrent Pregnancy Loss</a>', 
         'href="pregnancy-care.html" class="dropdown-item">Recurrent Pregnancy Loss</a>'),
        ('href="high-risk-pregnancy.html" class="dropdown-item">AUB Clinic</a>', 
         'href="menstrual-disorders.html" class="dropdown-item">AUB Clinic</a>'),
        ('href="high-risk-pregnancy.html" class="dropdown-item">Contraception</a>', 
         'href="menstrual-disorders.html" class="dropdown-item">Contraception</a>'),
        ('href="high-risk-pregnancy.html" class="dropdown-item">Obesity</a>', 
         'href="pcos.html" class="dropdown-item">Obesity Clinic</a>'),
        ('href="high-risk-pregnancy.html" class="dropdown-item">Cosmetology</a>', 
         'href="pcos.html" class="dropdown-item">Cosmetology</a>'),
         
        # Login links
        ('href="http://bd733462.ngrok.io/user/doctorlogin"', 
         'href="/frontend/staff/login.html"'),
        ('href="http://bd733462.ngrok.io/user/patientlogin"', 
         'href="/frontend/patient/login.html"'),
    ]
    
    for old, new in wrong_links:
        if old in content:
            content = content.replace(old, new)
            changes.append(f'  Fixed link: {old[:50]}...')
    
    # Fix footer links pointing to wrong pages
    footer_fixes = [
        ('href="high-risk-pregnancy.html"', 'href="pregnancy-care.html"'),
    ]
    
    # Fix Patient Portal login in index.html top bar
    content = content.replace(
        'href="/frontend/patient/login.html">Patient Login',
        'href="/frontend/patient/login.html">Patient Login'
    )
    content = content.replace(
        'href="/frontend/staff/login.html">Staff Login', 
        'href="/frontend/staff/login.html">Staff Login'
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'✅ Fixed: {os.path.basename(filepath)}')
        for c in changes[:5]:  # Show first 5 changes
            print(c)
        return True
    return False

# === FIX ALL HTML FILES ===
html_files = glob.glob(os.path.join(BASE, '*.html'))
print("🔧 Fixing navigation links across all pages...")
print("=" * 60)

fixed_count = 0
for filepath in sorted(html_files):
    filename = os.path.basename(filepath)
    # Skip frontend pages (they have their own nav system)
    if filename.startswith('branch-') or filename in [
        'baseline-scan.html', 'hormonal-assay.html', 'hormone-testing.html',
        'semen-analysis.html', 'y-chromosome-deletion.html', 'sperm-dna-fragmentation.html',
        'karyotyping.html', 'sonohysterosalpingogram.html', 'pelvic-scan.html',
        'ovarian-stimulation.html', 'fertility-preservation.html',
        'pcos.html', 'endometriosis.html', 'fibroids.html', 'menstrual-disorders.html',
        'pregnancy-care.html', 'postnatal-care.html', 'pediatrics.html', 'neonatology.html',
        'breastfeeding-support.html', 'branch-coimbatore.html', 'branch-chennai.html',
        'branch-salem.html', 'branch-tiruppur.html', 'branch-pollachi.html'
    ]:
        if fix_html_file(filepath):
            fixed_count += 1
    else:
        if fix_html_file(filepath):
            fixed_count += 1

print(f"\n🎉 Fixed {fixed_count} files with navigation links!")
print("\n📋 To verify, check:")
print("   - All Test menu items point to correct test pages")
print("   - All Clinic menu items point to correct clinic pages")
print("   - All Procedure menu items point to correct procedure pages")
print("   - Login links point to proper portal pages")