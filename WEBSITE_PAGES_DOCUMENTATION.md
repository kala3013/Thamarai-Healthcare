# Thamarai Fertility & Women's Health Center - Complete Website Documentation

**Live Website:** https://thamaraihealthcare.com/ (WordPress CMS)
**Local Development:** c:\xampp\htdocs\thamarai-healthcare (Static HTML + Backend API)

---

## 1. SITE OVERVIEW

The website is for **Thamarai Fertility & Women's Health Center**, a fertility and reproductive medicine healthcare provider with 7 branches across Tamil Nadu, India. The website has two versions:

- **Live WordPress Site** (https://thamaraihealthcare.com/) - The old/main production site on WordPress 5.3.21 with LayerSlider and custom theme
- **Local Static HTML Site** (c:\xampp\htdocs\thamarai-healthcare) - A modernized redesign with Bootstrap 5, AOS animations, and a backend API (Node.js/Express)

---

## 2. COMPLETE PAGE INVENTORY

### 2.1 MAIN STATIC PAGES (Local Project)

| # | File | Page Title | URL |
|---|------|-----------|-----|
| 1 | `index.html` | Home | /index.html |
| 2 | `about.html` | About Us | /about.html |
| 3 | `services.html` | Our Services | /services.html |
| 4 | `our-doctors.html` | Our Doctors | /our-doctors.html |
| 5 | `doctor-details.html` | Doctor Profile (Dynamic) | /doctor-details.html?id=X |
| 6 | `success-stories.html` | Success Stories | /success-stories.html |
| 7 | `gallery.html` | Gallery / Virtual Lab Tour | /gallery.html |
| 8 | `achievements.html` | Achievements & Academics | /achievements.html |
| 9 | `events.html` | Events & Workshops | /events.html |
| 10 | `blog.html` | Health Blog | /blog.html |
| 11 | `blog-details.html` | Blog Post Details (Dynamic) | /blog-details.html?slug=X |
| 12 | `faq.html` | FAQ (Dynamic from API) | /faq.html |
| 13 | `calculators.html` | Health Calculators | /calculators.html |
| 14 | `contact.html` | Contact & Appointments | /contact.html |
| 15 | `robots.txt` | Robots Exclusion | /robots.txt |
| 16 | `sitemap.xml` | XML Sitemap | /sitemap.xml |

### 2.2 LIVE WORDPRESS PAGES (Not in local project)

The live WordPress site at https://thamaraihealthcare.com/ has additional pages not present as static HTML files:

| Page Path | Content |
|-----------|---------|
| `/profile/our-doctors/` | Our Doctors (WordPress) |
| `/aboutus/` | About Us (WordPress) |
| `/profile/testimonials/` | Testimonials (WordPress) |
| `/profile/virtual-lab-tour/` | Virtual Lab Tour (WordPress) |
| `/profile/academics/` | Academics (WordPress) |
| `/profile/research/` | Research (WordPress) |
| `/fertility/fertility-basics/` | Fertility Basics (WordPress) |
| `/fertility/disorders-of-fertility/male-factor/` | Male Factor |
| `/treatments-for-male-factor/` | Treatments For Male Factor |
| `/fertility/disorders-of-fertility/uterine-factor/` | Uterine Factor |
| `/fertility/disorders-of-fertility/ovulatory-factor-2/` | Ovulatory Factor |
| `/fertility/disorders-of-fertility/tubal-factor/` | Tubal Factor |
| `/fertility/disorders-of-fertility/pelvic-factor-2/` | Pelvic Factor |
| `/fertility/disorders-of-fertility/coital-factor/` | Coital Factor |
| `/tests/tests-for-ovulation/` | Tests for Ovulation |
| `/tests/tests-for-ovulation/baseline-scan-follicular-study/` | Baseline Scan & Follicular Study |
| `/tests/tests-for-ovulation/hormonal-assay/` | Hormonal Assay |
| `/tests/tests-for-ovulation/hormone-test/` | Hormone Test |
| `/tests/test-for-sperm/` | Test for Sperm |
| `/tests/test-for-sperm/semen-analysis/` | Semen Analysis |
| `/tests/test-for-sperm/y-chromosome-micro-deletion/` | Y Chromosome Micro Deletion |
| `/tests/test-for-sperm/sperm-dna-fragmentation/` | Sperm DNA Fragmentation |
| `/tests/test-for-sperm/karyotyping/` | Karyotyping |
| `/tests/tests-for-the-tubes-and-uterus/` | Tests for Tubes & Uterus |
| `/tests/tests-for-the-tubes-and-uterus/test-for-fibroid/` | Test for Fibroid |
| `/tests/tests-for-the-tubes-and-uterus/3dsonohysterosalpingogram/` | 3D Sonohysterosalpingogram |
| `/tests/test-for-pelvis/` | Test for Pelvis |
| `/procedures/ovarian-stimulation/for-iui/` | For IUI |
| `/procedures/ovarian-stimulation/for-art/` | For ART |
| `/procedures/ovarian-stimulation/ovarian-hyperstimulation/` | Ovarian Hyperstimulation |
| `/procedures/intra-uterine-insemination/` | Intra Uterine Insemination |
| `/procedures/sperm-freezing/` | Sperm Freezing |
| `/procedures/art/ivf-egg-retrieval/` | IVF - Egg Retrieval |
| `/procedures/art/icsi/` | ICSI |
| `/fertilization-and-embryo-culture/` | Fertilization and Embryo Culture |
| `/embryo-transfer/` | Embryo Transfer |
| `/procedures/embryo-freezing/` | Embryo Freezing |
| `/procedures/pgd/` | PGD |
| `/procedures/egg-and-embryo-donation/` | Egg and Embryo Donation |
| `/procedures/surrogacy/` | Surrogacy |
| `/special-clinics/` | Special Clinics |
| `/high-risk-pregnancy-care/` | High Risk Pregnancy Care |
| `/ante-natal/` | Post Natal Clinic |
| `/early-pregnancy-assessment/` | Early Pregnancy Assessment |
| `/cancer-screening/` | Cancer Screening |
| `/aub-clinic/` | AUB (Abnormal Uterine Bleeding) Clinic |
| `/contraception/` | Contraception |
| `/fetal-medicine/` | Fetal Medicine |
| `/genetic/` | Genetic Clinic |
| `/adolescence/` | Adolescence |
| `/obesity/` | Obesity |

---

## 3. NAVIGATION STRUCTURE

### 3.1 TOP BAR (All Pages)
- **Contact Info:** Phone: +91 99655 24788 | Email: thamaraifertility@gmail.com
- **Login Links:** Staff Login | Patient Login (ngrok URLs)
- **Social Media:** Facebook, Twitter/X, Instagram, LinkedIn, YouTube

### 3.2 MAIN NAVBAR

#### Home
- Link: `index.html`

#### Profile (Dropdown)
- Our Doctors → `our-doctors.html`
- About Us → `about.html`
- Testimonials → `success-stories.html`
- Virtual Lab Tour → `gallery.html`
- Academics → `achievements.html`
- Research → `achievements.html`

#### Fertility (Dropdown)
- Fertility Basics → `services.html`
- Disorders of Fertility (Sub-dropdown):
  - Male Factor → `services.html`
  - Treatments For Male Factor → `services.html`
  - Uterine Factor → `services.html`
  - Ovulatory Factor → `services.html`
  - Tubal Factor → `services.html`
  - Pelvic Factor → `services.html`
  - Coital Factor → `services.html`

#### Tests (Dropdown)
- Tests for Ovulation (Sub-dropdown):
  - Baseline Scan & Follicular Study → `services.html`
  - Hormonal Assay → `services.html`
  - Hormone Test → `services.html`
- Test for Sperm (Sub-dropdown):
  - Semen Analysis → `services.html`
  - Y Chromosome Micro Deletion → `services.html`
  - Sperm DNA Fragmentation → `services.html`
  - Karyotyping → `services.html`
- Tests for Tubes & Uterus (Sub-dropdown):
  - Test for Fibroid → `services.html`
  - 3D Sonohysterosalpingogram → `services.html`
- Test for Pelvis → `services.html`

#### Procedures (Dropdown)
- Ovarian Stimulation (Sub-dropdown):
  - For IUI → `services.html`
  - For ART → `services.html`
  - Ovarian Hyperstimulation → `services.html`
- Intra Uterine Insemination → `services.html`
- Sperm Freezing → `services.html`
- Steps for IVF & ICSI (Sub-dropdown):
  - IVF - Egg Retrieval → `services.html`
  - ICSI → `services.html`
  - Fertilization & Embryo Culture → `services.html`
- Embryo Transfer → `services.html`
- Embryo Freezing → `services.html`
- PGD → `services.html`
- Egg & Embryo Donation → `services.html`
- Surrogacy → `services.html`

#### Clinics (Dropdown)
- Obstetrics (Sub-dropdown):
  - High Risk Pregnancy Care → `services.html`
  - Post Natal Clinic → `services.html`
  - Early Pregnancy Assessment → `services.html`
  - Recurrent Pregnancy Loss → `services.html`
- Gynecology (Sub-dropdown):
  - Cancer Screening → `services.html`
  - AUB Clinic → `services.html`
  - Contraception → `services.html`
- Fetal Medicine → `services.html`
- Genetic Clinic → `services.html`
- Special Clinics (Sub-dropdown):
  - Adolescence → `services.html`
  - Obesity → `services.html`
  - Endoscopy Clinic → `services.html`
  - Andrology Clinic → `services.html`
  - Cosmetology → `services.html`
  - Menopause → `services.html`
- Counselling (Sub-dropdown):
  - Prenatal & Postnatal Counselling → `services.html`
  - Premarital Counselling → `services.html`
  - Baby Care → `services.html`
  - Sexual Medicine → `services.html`

#### Gallery
- Link: `gallery.html`

#### Events (Dropdown)
- ISO Function → `events.html`
- IUI Workshop → `events.html`
- Bangkok Conf → `events.html`
- Rally For The Girl Child → `events.html`

#### Blog
- Link: `blog.html`

#### Contact
- Link: `contact.html`

### 3.3 NAVBAR BUTTONS
- **Calculators** → `calculators.html`
- **Book Appointment** → `contact.html#makeAppointment`

---

## 4. PAGE-BY-PAGE CONTENT DETAILS

### 4.1 Home (index.html)
**Hero Carousel (4 slides):**
1. "Creating families over 3 decades. Dedication, research & innovation" - Book Appointment CTA
2. "A baby for every couple" - Success Stories CTA
3. "First ICSI pregnancy with roundheaded sperms" - Landmark Achievement
4. "Y chromosome micro deletion detection" - Advanced Diagnostics

**Branches Bar:** 6 branch chips: Coimbatore-I (Peelamedu), Coimbatore-II (KMCH), Chennai (Fertility Solutions), Salem (Devi Hospital), Tirupur (Ganapathy Nursing Home), Pollachi (Women's Health Center)

**Welcome Section:** "Your trusted partner in creating families for over three decades" with appointment form and service icons carousel (Assisted Reproduction, Andrology, Fetal Medicine, Genetics, High Risk Pregnancy, Neonatology, Pediatrics, Antenatal Classes, Gynecology, Obesity, Adolescence, Menopause, Cosmetology, Lactation Consultancy, Counseling)

**Founders Section:** Dr. P. Uthraraj (Chairman), Dr. C.V. Kannaki Uthraraj (Director), Dr. Nachappa Sivanesan Uthraraj (Advisor)

**Why Choose Us:** Track Record & Achievements, Individualised Protocols, Our Pillars

**Services Section:** Fertility Clinic, Andrology Clinic, Genetic Clinic, Endoscopy Clinic, Fetal Medicine & High Risk Pregnancy, Special Clinics for Women, Pregnancy Classes & Counselling, Neonatology, Pediatrics

**Counters:** 15,000+ IUI Success | 5,524+ IVF Success | 7 Branches | 21 Consultants

**Testimonials:** Priya & Ramesh (IVF Success), Anitha & Kumar (ICSI Treatment), Deepa & Venkat (IUI Success)

### 4.2 About Us (about.html)
**Page Hero:** "About Thamarai Fertility"

**Our Story:** Three decades of excellence, ISO & NABH certified, expert team of 21+ consultants, compassionate care, advanced technology

**Mission/Vision/Values Cards:**
- Mission: Build healthy families with compassion, innovation and integrity
- Vision: Region's first choice for fertility care
- Values: Patient-centred care, Clinical excellence, Ethical practice, Compassion & respect, Innovation & research

**Founders:** Same 3 founders as home page with detailed info

**CTA:** "Ready to start your fertility journey?" → Book Appointment

### 4.3 Services (services.html)
**Page Hero:** "Our Fertility & Women's Health Services"
Detailed descriptions of 8 service categories:
1. **Fertility Clinic** - Complete evaluation, IUI, IVF, ICSI, egg donation
2. **Andrology Clinic** - Semen analysis, sperm DNA frag, Y chromosome testing, karyotyping
3. **Genetic Clinic** - PGD, carrier screening, chromosomal analysis
4. **Endoscopy Clinic** - Hysteroscopy, laparoscopy, fibroid removal
5. **Fetal Medicine & High Risk Pregnancy** - Anomaly scans, NT scan, amniocentesis
6. **Special Clinics for Women** - Adolescent, obesity, menopause, cosmetology, cancer screening
7. **Neonatology** - NICU care, babies as low as 530 grams saved
8. **Pediatrics** - 4-decade track record at Sivameds hospital, Pollachi
9. **Pregnancy Classes & Counselling** - Partnership with Siksha Baby Care

### 4.4 Our Doctors (our-doctors.html)
**6 Doctor Cards:**
1. Dr. P. Uthraraj - Chairman, MD, DCH
2. Dr. C.V. Kannaki Uthraraj - Director, MD, DGO
3. Dr. Nachappa Sivanesan Uthraraj - Advisor, DNB
4. Dr. Mangayarkarasi - Lab Director, Ph.D
5. Dr. Devdas Madhavan - Consultant
6. Dr. Barani Kumar - Consultant

Each card links to `doctor-details.html?doc=XXX`

### 4.5 Doctor Details (doctor-details.html - Dynamic)
Dynamically loads doctor info from API (`/api/public/doctors/:id`). Displays photo, name, specialization, qualifications, experience, availability, branch, consultation fee, awards.

Also accepts query parameters: `?doc=uthraraj`, `?doc=kannaki`, `?doc=nachappa`, `?doc=mangayarkarasi`, `?doc=devdas`, `?doc=barani`

### 4.6 Success Stories (success-stories.html)
**3 Testimonials:**
1. Priya & Ramesh - "Thamarai Fertility gave us the gift of parenthood..." (IVF Success)
2. Anitha & Kumar - "The care and compassion we received..." (ICSI Treatment)
3. Deepa & Venkat - "Best fertility center in Tamil Nadu..." (IUI Success)

### 4.7 Gallery (gallery.html)
Gallery page with image grid and overlay captions. Features Virtual Lab Tour section. Links to branch-specific galleries.

### 4.8 Achievements (achievements.html)
**Counters:** 15,000+ IUI Success | 5,524+ IVF Success | 7 Branches | 21 Consultants

**Achievement Cards:**
1. Landmark Achievement - First ICSI pregnancy with roundheaded sperms
2. ISO & NABH Certified - Quality and safety standards
3. Several Thousand Happy Parents - Success with difficult cases
4. Y Chromosome Micro Deletion Detection - Advanced genetic testing

### 4.9 Events (events.html)
**4 Event Cards:**
1. ISO Function 2007 - Certification ceremony
2. IUI Workshop - Hands-on training for medical professionals
3. Bangkok Conference - International conference on reproductive medicine
4. Rally For The Girl Child - Community awareness

### 4.10 Blog (blog.html)
Dynamic blog listing page that loads posts from API (`/api/blogs/public`). Includes pagination, category filtering, sidebar with recent posts and categories.

### 4.11 Blog Details (blog-details.html)
Dynamic single post page loads from API (`/api/blogs/public/:slug`). Features: social sharing (Facebook, Twitter, WhatsApp), comments system, related posts sidebar.

### 4.12 FAQ (faq.html)
Dynamic FAQ page loading from API (`/api/faqs/public`). Features category filter buttons (loaded from API), accordion display, FAQ Schema structured data.

### 4.13 Calculators (calculators.html)
**5 Interactive Tools:**
1. **IVF Success Calculator** - Based on age, weight, infertility duration, previous attempts
2. **Ovulation Calculator** - Based on LMP and cycle length
3. **Due Date Calculator** - Based on LMP or conception date
4. **BMI Calculator** - Height/weight based with category
5. **Fertility Assessment Quiz** - 4 questions scoring fertility indicators

### 4.14 Contact (contact.html)
**Contact Info:** Head Office address, phone numbers, email

**6 Branch Locations:** Coimbatore-I (Peelamedu), Coimbatore-II (KMCH), Chennai (Fertility Solutions), Salem (Devi Hospital), Tirupur (Ganapathy Nursing Home), Pollachi (Women's Health Center)

**Appointment Form:** Name, Choose Doctor (7 options), Email, Phone, Preferred Date, Subject, Message

---

## 5. CROSS-PAGE LINKING MATRIX

| From \ To | index | about | services | doctors | doctor-details | success-stories | gallery | achievements | events | blog | blog-details | faq | calculators | contact |
|-----------|-------|-------|----------|---------|----------------|-----------------|---------|--------------|--------|------|-------------|-----|-------------|---------|
| **index** | - | ✓ | ✓ | ✓ | - | ✓ | ✓ | ✓ | - | - | - | - | ✓ | ✓ |
| **about** | - | - | - | ✓ | - | - | - | - | - | - | - | - | - | ✓ |
| **services** | - | - | - | - | - | - | - | - | - | - | - | - | - | ✓ |
| **our-doctors** | - | - | - | - | ✓(6) | - | - | - | - | - | - | - | - | ✓ |
| **success-stories** | - | - | - | ✓ | - | - | ✓ | - | - | - | - | - | - | - |
| **gallery** | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| **achievements** | - | ✓ | - | ✓ | - | ✓ | ✓ | - | - | - | - | - | - | - |
| **events** | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| **blog** | ✓ | ✓ | ✓ | ✓ | - | - | - | ✓ | - | - | ✓ | ✓ | - | ✓ |
| **blog-details** | ✓ | ✓ | ✓ | ✓ | - | - | - | - | - | ✓ | - | - | - | ✓ |
| **faq** | ✓ | ✓ | ✓ | ✓ | - | - | - | - | - | - | - | - | - | ✓ |
| **calculators** | ✓ | - | ✓ | - | - | - | - | - | - | - | - | - | - | ✓ |
| **contact** | - | - | - | - | - | - | - | - | - | - | - | - | ✓ | - |

---

## 6. FOOTER STRUCTURE (All Pages)

### Footer Links Section (4 Columns):
1. **About Our Clinic:** Our Doctors, About Us, Testimonials, Virtual Lab Tour, Academics, Research
2. **Fertility:** Fertility Basics, Male Factor, Ovulatory Factor, Uterine Factor, Tubal Factor, Pelvic Factor, Coital Factor
3. **Procedures:** IUI, IVF - Egg Retrieval, ICSI, Sperm Freezing, Embryo Freezing, PGD, Egg & Embryo Donation
4. **Contact Us:** Address (#1518, PKD Nagar, Avinashi Rd, Coimbatore - 641004), Phone (0422-2626999, 99655 24788), Email

### Footer Bottom:
- © 2026 Thamarai Fertility. All Rights Reserved.
- Design: Mindmade Technologies

### Footer Social Links:
Facebook, Twitter/X, Instagram, LinkedIn, YouTube

### Floating Action Buttons (All Pages):
- WhatsApp Chat (+91 99655 24788)
- Call Now (0422-2626999)
- Book Appointment (scrolls to #makeAppointment)

---

## 7. BACKEND API ENDPOINTS

The local project has a Node.js/Express backend:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/faqs/public` | GET | Get all FAQs |
| `/api/faqs/public?category=X` | GET | Filter FAQs by category |
| `/api/blogs/public` | GET | Get all blog posts |
| `/api/blogs/public/:slug` | GET | Get single blog post with related posts & comments |
| `/api/blogs/public/:id/comment` | POST | Submit a comment |
| `/api/public/doctors/:id` | GET | Get doctor details |
| `/api/contact` | POST | Submit contact/appointment form |

---

## 8. EXTERNAL INTEGRATIONS

| Service | Purpose |
|---------|---------|
| Bootstrap 5.3.2 | CSS framework |
| Bootstrap Icons | Icon library |
| Font Awesome 6.5.1 | Social media icons |
| OwlCarousel 2.3.4 | Service icons carousel |
| AOS 2.3.1 | Scroll animations |
| Google Fonts (Inter, Poppins) | Typography |
| jQuery 3.7.1 | JavaScript library |
| ngrok (bd733462.ngrok.io) | Staff/Patient login portal |
| WhatsApp API | Floating chat button |
| Facebook/Instagram/LinkedIn/YouTube/Twitter | Social media profiles |

---

## 9. KEY CONTACT INFORMATION

- **Phone:** 0422-2626999, +91 99655 24788
- **Email:** thamaraifertility@gmail.com
- **Address:** #1518, PKD Nagar, Avinashi Rd, Coimbatore - 641004
- **Branches:** Coimbatore (Peelamedu & KMCH), Chennai, Salem, Tirupur, Pollachi
- **Social:** Facebook (@thamaraifertility), X/Twitter (@thamaraiivf), Instagram (@thamaraiivf), LinkedIn (Thamarai Fertility), YouTube (@thamaraiivf)

---

## 10. LIVE WEBSITE (WORDPRESS) VERSUS LOCAL PROJECT

| Aspect | Live WordPress Site | Local Static Project |
|--------|-------------------|---------------------|
| **CMS** | WordPress 5.3.21 | Static HTML + API |
| **Theme** | Custom "thamarai" theme | Bootstrap 5 custom CSS |
| **Slider** | LayerSlider | Bootstrap carousel |
| **Menu** | Fly Menu plugin | Bootstrap navbar with dropdowns |
| **Forms** | Contact Form 7 | Custom AJAX forms |
| **Animations** | jQuery | AOS library |
| **Content Pages** | Many individual WordPress pages | Single-page summaries linking to `services.html` |
| **URL Structure** | Pretty URLs (e.g., `/fertility/fertility-basics/`) | Flat `.html` files |

**Note:** The local static HTML project consolidates the WordPress site's many individual pages (about 50+ content pages) into a streamlined set of ~15 HTML files. All the sub-pages (Male Factor, Fertility Basics, IVF steps, etc.) from the WordPress site all redirect to `services.html` in the local version, which provides summarized content.