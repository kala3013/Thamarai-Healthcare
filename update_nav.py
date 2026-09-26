import os
import re

base = r'c:\Users\ELCOT\Desktop\thamarai-healthcare'

# The new navigation block to replace
new_nav_fertility = '''<li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">Fertility</a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="fertility-basics.html">Fertility Basics</a></li>
            <li class="dropdown-submenu">
              <a class="dropdown-item dropdown-toggle" href="#">Disorders of Fertility</a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="male-factor.html">Male Factor</a></li>
                <li><a class="dropdown-item" href="male-factor.html">Treatments For Male Factor</a></li>
                <li><a class="dropdown-item" href="uterine-factor.html">Uterine Factor</a></li>
                <li><a class="dropdown-item" href="ovulatory-factor.html">Ovulatory Factor</a></li>
                <li><a class="dropdown-item" href="tubal-factor.html">Tubal Factor</a></li>
                <li><a class="dropdown-item" href="pelvic-factor.html">Pelvic Factor</a></li>
                <li><a class="dropdown-item" href="coital-factor.html">Coital Factor</a></li>
              </ul>
            </li>
          </ul>
        </li>'''

# Pages to update with their specific new nav
page_updates = {
    # Main pages - no specific active link
    'index.html': 'home',
    'about.html': 'profile',
    'gallery.html': 'gallery',
    'success-stories.html': 'profile',
    'achievements.html': 'profile',
    'contact.html': 'contact',
    'events.html': 'events',
    'blog.html': 'blog',
    'our-doctors.html': 'profile',
    'services.html': 'fertility',
    'calculators.html': 'home',
    'faq.html': 'home',
    'blog-details.html': 'blog',
    'doctor-details.html': 'home',
}

def update_page(filename, active_type):
    filepath = os.path.join(base, filename)
    if not os.path.exists(filepath):
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace Fertility nav block (Fertility Basics, Male Factor, etc.)
    old_fertility_pattern = re.compile(
        r'<li class="nav-item dropdown">\s*<a class="nav-link[^"]*" href="#" role="button" data-bs-toggle="dropdown">Fertility</a>\s*<ul class="dropdown-menu">\s*<li><a class="dropdown-item" href="services\.html">Fertility Basics</a></li>.*?</ul>\s*</li>',
        re.DOTALL
    )
    content = old_fertility_pattern.sub(new_nav_fertility, content, count=1)
    
    # Replace Tests nav block
    old_tests_pattern = re.compile(
        r'<li class="nav-item dropdown">\s*<a class="nav-link[^"]*" href="#" role="button" data-bs-toggle="dropdown">Tests</a>.*?</li>\s*<li class="nav-item dropdown">\s*<a class="nav-link[^"]*" href="#" role="button" data-bs-toggle="dropdown">Procedures</a>',
        re.DOTALL
    )
    
    new_tests_and_procedures = '''<li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">Tests</a>
          <ul class="dropdown-menu">
            <li class="dropdown-submenu"><a class="dropdown-item dropdown-toggle" href="#">Tests for Ovulation</a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="fertility-basics.html">Baseline Scan & Follicular Study</a></li>
                <li><a class="dropdown-item" href="fertility-basics.html">Hormonal Assay</a></li>
                <li><a class="dropdown-item" href="fertility-basics.html">Hormone Test</a></li>
              </ul>
            </li>
            <li class="dropdown-submenu"><a class="dropdown-item dropdown-toggle" href="#">Test for Sperm</a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="male-factor.html">Semen Analysis</a></li>
                <li><a class="dropdown-item" href="male-factor.html">Y Chromosome Micro Deletion</a></li>
                <li><a class="dropdown-item" href="male-factor.html">Sperm DNA Fragmentation</a></li>
                <li><a class="dropdown-item" href="male-factor.html">Karyotyping</a></li>
              </ul>
            </li>
            <li class="dropdown-submenu"><a class="dropdown-item dropdown-toggle" href="#">Tests for Tubes & Uterus</a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="uterine-factor.html">Test for Fibroid</a></li>
                <li><a class="dropdown-item" href="uterine-factor.html">3D Sonohysterosalpingogram</a></li>
              </ul>
            </li>
            <li><a class="dropdown-item" href="pelvic-factor.html">Test for Pelvis</a></li>
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">Procedures</a>'''
    
    content = old_tests_pattern.sub(new_tests_and_procedures, content, count=1)
    
    # Replace remaining procedures entries
    procedures_replacements = [
        ('href="services.html">For IUI</a>', 'href="iui.html">For IUI</a>'),
        ('href="services.html">For ART</a>', 'href="ivf.html">For ART</a>'),
        ('href="services.html">Ovarian Hyperstimulation</a>', 'href="ivf.html">Ovarian Hyperstimulation</a>'),
        ('href="services.html">Intra Uterine Insemination</a>', 'href="iui.html">Intra Uterine Insemination</a>'),
        ('href="services.html">Sperm Freezing</a>', 'href="sperm-freezing.html">Sperm Freezing</a>'),
        ('href="services.html">IVF – Egg Retrieval</a>', 'href="ivf.html">IVF – Egg Retrieval</a>'),
        ('href="services.html">ICSI</a>', 'href="icsi.html">ICSI</a>'),
        ('href="services.html">Fertilization & Embryo Culture</a>', 'href="ivf.html">Fertilization & Embryo Culture</a>'),
        ('href="services.html">Embryo Transfer</a>', 'href="ivf.html">Embryo Transfer</a>'),
        ('href="services.html">Embryo Freezing</a>', 'href="embryo-freezing.html">Embryo Freezing</a>'),
        ('href="services.html">PGD</a>', 'href="pgd.html">PGD</a>'),
        ('href="services.html">Egg & Embryo Donation</a>', 'href="egg-donation.html">Egg & Embryo Donation</a>'),
        ('href="services.html">Surrogacy</a>', 'href="surrogacy.html">Surrogacy</a>'),
        # Clinics
        ('href="services.html">High Risk Pregnancy Care</a>', 'href="high-risk-pregnancy.html">High Risk Pregnancy Care</a>'),
        ('href="services.html">Post Natal Clinic</a>', 'href="high-risk-pregnancy.html">Post Natal Clinic</a>'),
        ('href="services.html">Early Pregnancy Assessment</a>', 'href="high-risk-pregnancy.html">Early Pregnancy Assessment</a>'),
        ('href="services.html">Recurrent Pregnancy Loss</a>', 'href="high-risk-pregnancy.html">Recurrent Pregnancy Loss</a>'),
        ('href="services.html">Cancer Screening</a>', 'href="cancer-screening.html">Cancer Screening</a>'),
        ('href="services.html">AUB Clinic</a>', 'href="high-risk-pregnancy.html">AUB Clinic</a>'),
        ('href="services.html">Contraception</a>', 'href="high-risk-pregnancy.html">Contraception</a>'),
        ('href="services.html">Fetal Medicine</a>', 'href="fetal-medicine.html">Fetal Medicine</a>'),
        ('href="services.html">Genetic Clinic</a>', 'href="genetic-clinic.html">Genetic Clinic</a>'),
        ('href="services.html">Adolescence</a>', 'href="adolescence.html">Adolescence</a>'),
        ('href="services.html">Obesity</a>', 'href="high-risk-pregnancy.html">Obesity</a>'),
        ('href="services.html">Endoscopy Clinic</a>', 'href="endoscopy-clinic.html">Endoscopy Clinic</a>'),
        ('href="services.html">Andrology Clinic</a>', 'href="andrology-clinic.html">Andrology Clinic</a>'),
        ('href="services.html">Cosmetology</a>', 'href="high-risk-pregnancy.html">Cosmetology</a>'),
        ('href="services.html">Menopause</a>', 'href="menopause.html">Menopause</a>'),
        ('href="services.html">Prenatal & Postnatal Counselling</a>', 'href="counselling.html">Prenatal & Postnatal Counselling</a>'),
        ('href="services.html">Premarital Counselling</a>', 'href="counselling.html">Premarital Counselling</a>'),
        ('href="services.html">Baby Care</a>', 'href="counselling.html">Baby Care</a>'),
        ('href="services.html">Sexual Medicine</a>', 'href="counselling.html">Sexual Medicine</a>'),
        # Footer links
        ('href="services.html">Fertility Basics</a>', 'href="fertility-basics.html">Fertility Basics</a>'),
        ('href="services.html">Male Factor</a>', 'href="male-factor.html">Male Factor</a>'),
        ('href="services.html">Ovulatory Factor</a>', 'href="ovulatory-factor.html">Ovulatory Factor</a>'),
        ('href="services.html">Uterine Factor</a>', 'href="uterine-factor.html">Uterine Factor</a>'),
        ('href="services.html">Tubal Factor</a>', 'href="tubal-factor.html">Tubal Factor</a>'),
        ('href="services.html">Pelvic Factor</a>', 'href="pelvic-factor.html">Pelvic Factor</a>'),
        ('href="services.html">Coital Factor</a>', 'href="coital-factor.html">Coital Factor</a>'),
        ('href="services.html">IVF – Egg Retrieval</a>', 'href="ivf.html">IVF – Egg Retrieval</a>'),
        ('href="services.html">ICSI</a>', 'href="icsi.html">ICSI</a>'),
        ('href="services.html">Sperm Freezing</a>', 'href="sperm-freezing.html">Sperm Freezing</a>'),
        ('href="services.html">Embryo Freezing</a>', 'href="embryo-freezing.html">Embryo Freezing</a>'),
        ('href="services.html">PGD</a>', 'href="pgd.html">PGD</a>'),
        ('href="services.html">Egg & Embryo Donation</a>', 'href="egg-donation.html">Egg & Embryo Donation</a>'),
    ]
    
    for old, new in procedures_replacements:
        content = content.replace(old, new)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

# Update main pages
for page, active in page_updates.items():
    if update_page(page, active):
        print(f'✅ Updated navigation in {page}')

# Also update footer-only references in all existing pages
# (pages that don't have nav but may have services.html links in footer)
all_pages = [f for f in os.listdir(base) if f.endswith('.html')]
for f in all_pages:
    filepath = os.path.join(base, f)
    with open(filepath, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    # Apply replacements to footer links too
    footer_replacements = [
        ('href="services.html">Fertility Basics</a>', 'href="fertility-basics.html">Fertility Basics</a>'),
        ('href="services.html">Male Factor</a>', 'href="male-factor.html">Male Factor</a>'),
        ('href="services.html">Ovulatory Factor</a>', 'href="ovulatory-factor.html">Ovulatory Factor</a>'),
        ('href="services.html">Uterine Factor</a>', 'href="uterine-factor.html">Uterine Factor</a>'),
        ('href="services.html">Tubal Factor</a>', 'href="tubal-factor.html">Tubal Factor</a>'),
        ('href="services.html">Pelvic Factor</a>', 'href="pelvic-factor.html">Pelvic Factor</a>'),
        ('href="services.html">Coital Factor</a>', 'href="coital-factor.html">Coital Factor</a>'),
        ('href="services.html">IVF – Egg Retrieval</a>', 'href="ivf.html">IVF – Egg Retrieval</a>'),
        ('href="services.html">ICSI</a>', 'href="icsi.html">ICSI</a>'),
        ('href="services.html">Sperm Freezing</a>', 'href="sperm-freezing.html">Sperm Freezing</a>'),
        ('href="services.html">Embryo Freezing</a>', 'href="embryo-freezing.html">Embryo Freezing</a>'),
        ('href="services.html">PGD</a>', 'href="pgd.html">PGD</a>'),
        ('href="services.html">Egg & Embryo Donation</a>', 'href="egg-donation.html">Egg & Embryo Donation</a>'),
    ]
    
    for old, new in footer_replacements:
        content = content.replace(old, new)
    
    with open(filepath, 'w', encoding='utf-8') as fh:
        fh.write(content)

print('\n🎉 All pages updated with new navigation links!')