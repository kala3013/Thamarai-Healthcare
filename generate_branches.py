#!/usr/bin/env python3
"""Generate branch-specific pages for Thamarai Healthcare"""
import os

BASE = r'c:\Users\ELCOT\Desktop\thamarai-healthcare'
TEMPLATE = os.path.join(BASE, 'iui.html')

with open(TEMPLATE, 'r', encoding='utf-8') as f:
    BASE_HTML = f.read()

branches = {
    'branch-coimbatore.html': {
        'title': 'Thamarai Fertility Center - Coimbatore',
        'desc': 'Thamarai Fertility Center in Coimbatore - leading fertility clinic with IVF, ICSI, IUI, and women\'s health services at our main branch on Avinashi Road.',
        'name': 'Coimbatore (Main Branch)',
        'address': '#1518, PKD Nagar, Avinashi Road, Coimbatore - 641004',
        'phone': '0422-2626999',
        'mobile': '99655 24788',
        'email': 'thamaraifertility@gmail.com',
        'timings': 'Mon - Sat: 9:00 AM - 6:00 PM',
        'doctors': ['Dr. P. Uthraraj', 'Dr. C.V. Kannaki Uthraraj', 'Dr. Nandhini'],
        'services': ['IVF Treatment', 'ICSI Procedure', 'IUI Treatment', 'Laparoscopy', 'Hysteroscopy', 'Fetal Medicine', 'High Risk Pregnancy Care', 'PCOS Management']
    },
    'branch-chennai.html': {
        'title': 'Thamarai Fertility Center - Chennai',
        'desc': 'Thamarai Fertility Center in Chennai - advanced fertility treatments including IVF, ICSI, and women\'s healthcare services in Chennai.',
        'name': 'Chennai',
        'address': '#45, Mount Road, Opp. to US Consulate, Chennai - 600006',
        'phone': '044-28259999',
        'mobile': '99655 24788',
        'email': 'chennai@thamaraihealthcare.com',
        'timings': 'Mon - Sat: 9:00 AM - 6:00 PM',
        'doctors': ['Dr. P. Uthraraj', 'Dr. Preethi'],
        'services': ['IVF Treatment', 'ICSI', 'IUI', 'Scanning', 'Counselling']
    },
    'branch-salem.html': {
        'title': 'Thamarai Fertility Center - Salem',
        'desc': 'Thamarai Fertility Center in Salem - comprehensive fertility services and women\'s healthcare in Salem district.',
        'name': 'Salem',
        'address': '#123, Omalur Main Road, Salem - 636004',
        'phone': '0427-2333999',
        'mobile': '99655 24788',
        'email': 'salem@thamaraihealthcare.com',
        'timings': 'Mon - Sat: 9:00 AM - 6:00 PM',
        'doctors': ['Dr. P. Uthraraj', 'Dr. Kavitha'],
        'services': ['IVF', 'ICSI', 'IUI', 'Scanning', 'Pharmacy']
    },
    'branch-tiruppur.html': {
        'title': 'Thamarai Fertility Center - Tiruppur',
        'desc': 'Thamarai Fertility Center in Tiruppur - fertility treatments and women\'s health services in Tiruppur.',
        'name': 'Tiruppur',
        'address': '#67, Kumaran Road, Tiruppur - 641601',
        'phone': '0421-2244999',
        'mobile': '99655 24788',
        'email': 'tiruppur@thamaraihealthcare.com',
        'timings': 'Mon - Sat: 9:00 AM - 6:00 PM',
        'doctors': ['Dr. P. Uthraraj'],
        'services': ['Consultation', 'IUI', 'Scanning', 'Basic Fertility Services']
    },
    'branch-pollachi.html': {
        'title': 'Thamarai Fertility Center - Pollachi',
        'desc': 'Thamarai Fertility Center in Pollachi - fertility consultations and women\'s healthcare services in Pollachi.',
        'name': 'Pollachi',
        'address': '#89, Kovai Road, Pollachi - 642001',
        'phone': '04259-226699',
        'mobile': '99655 24788',
        'email': 'pollachi@thamaraihealthcare.com',
        'timings': 'Mon - Sat: 9:00 AM - 6:00 PM',
        'doctors': ['Dr. P. Uthraraj'],
        'services': ['Consultation', 'Scanning', 'Pharmacy']
    }
}

for filename, b in branches.items():
    output = os.path.join(BASE, filename)
    if os.path.exists(output):
        print(f'⏩ Skipping {filename}')
        continue
    
    content = BASE_HTML
    
    # Update meta
    content = content.replace(
        '<title>IUI Treatment | Thamarai Fertility & Women\'s Health Center</title>',
        f'<title>{b["title"]} | Thamarai Fertility & Women\'s Health Center</title>'
    )
    content = content.replace(
        'name="description" content="Intrauterine Insemination (IUI) treatment at Thamarai Fertility - a safe, effective fertility procedure for couples trying to conceive."',
        f'name="description" content="{b["desc"]}"'
    )
    content = content.replace('https://thamaraihealthcare.com/iui.html', f'https://thamaraihealthcare.com/{filename}')
    
    # Replace hero
    content = content.replace('FERTILITY PROCEDURE', 'OUR BRANCHES')
    content = content.replace('Intrauterine <span class="text-gradient">Insemination (IUI)</span>', f'Thamarai Fertility <span class="text-gradient">{b["name"]}</span>')
    content = content.replace('A safe, simple, and effective fertility treatment that places specially prepared sperm directly into the uterus.', f'Visit our {b["name"]} branch for comprehensive fertility and women\'s healthcare services.')
    content = content.replace('What is IUI?', f'Welcome to Thamarai Fertility - {b["name"]}')
    content = content.replace('Intrauterine Insemination (IUI) is a fertility treatment that involves placing specially prepared sperm directly into a woman\'s uterus around the time of ovulation. This procedure increases the number of sperm that reach the fallopian tubes, thereby increasing the chance of fertilization.', f'Thamarai Fertility Center in {b["name"]} offers world-class fertility treatments and women\'s healthcare services. Our branch is equipped with state-of-the-art facilities and staffed by experienced specialists dedicated to providing personalized care.')
    
    # Build branch content
    doctors_html = ''.join([f'<li>{d}</li>' for d in b['doctors']])
    services_html = ''.join([f'<span class="badge bg-primary-soft text-primary me-1 mb-1">{s}</span>' for s in b['services']])
    
    custom_section = f'''
          <div class="row g-4 mt-3">
            <div class="col-lg-6">
              <div class="card h-100 border-0 shadow-sm">
                <div class="card-body p-4">
                  <h4 class="h5 mb-3"><i class="bi bi-geo-alt-fill text-primary me-2"></i>Address</h4>
                  <p class="mb-0">{b["address"]}</p>
                </div>
              </div>
            </div>
            <div class="col-lg-6">
              <div class="card h-100 border-0 shadow-sm">
                <div class="card-body p-4">
                  <h4 class="h5 mb-3"><i class="bi bi-telephone-fill text-primary me-2"></i>Contact</h4>
                  <p class="mb-1"><strong>Phone:</strong> {b["phone"]}</p>
                  <p class="mb-1"><strong>Mobile:</strong> {b["mobile"]}</p>
                  <p class="mb-0"><strong>Email:</strong> {b["email"]}</p>
                </div>
              </div>
            </div>
            <div class="col-lg-6">
              <div class="card h-100 border-0 shadow-sm">
                <div class="card-body p-4">
                  <h4 class="h5 mb-3"><i class="bi bi-clock-fill text-primary me-2"></i>Working Hours</h4>
                  <p class="mb-0">{b["timings"]}</p>
                </div>
              </div>
            </div>
            <div class="col-lg-6">
              <div class="card h-100 border-0 shadow-sm">
                <div class="card-body p-4">
                  <h4 class="h5 mb-3"><i class="bi bi-person-badge text-primary me-2"></i>Our Doctors</h4>
                  <ul class="mb-0">{doctors_html}</ul>
                </div>
              </div>
            </div>
          </div>
          
          <h3 class="mt-4">Services Offered</h3>
          <p>{services_html}</p>
          
          <div class="bg-gradient-cta p-4 rounded-4 text-center text-white mt-4">
            <h4 class="text-white">Book an Appointment at {b["name"]}</h4>
            <p class="text-white-50 mb-3">Call us or book online to schedule your consultation.</p>
            <div class="d-flex justify-content-center gap-3 flex-wrap">
              <a href="tel:{b["phone"]}" class="btn btn-light btn-lg"><i class="bi bi-telephone-fill me-2"></i>Call Now</a>
              <a href="contact.html#makeAppointment" class="btn btn-accent btn-lg shadow-accent"><i class="bi bi-calendar-check me-2"></i>Book Online</a>
            </div>
          </div>'''
    
    old_section = '''          <h3>The IUI Procedure - Step by Step</h3>
          <div class="row g-3 mt-3">
            <div class="col-md-6">
              <div class="flow-step"><div class="step-num">1</div><h5 class="h6">Ovulation Monitoring</h5><p class="small text-muted mb-0">Monitoring follicle development through ultrasound scans and tracking ovulation timing.</p></div>
            </div>
            <div class="col-md-6">
              <div class="flow-step"><div class="step-num">2</div><h5 class="h6">Sperm Collection & Preparation</h5><p class="small text-muted mb-0">The sperm sample is collected and washed in the lab to concentrate the healthiest sperm.</p></div>
            </div>
            <div class="col-md-6">
              <div class="flow-step"><div class="step-num">3</div><h5 class="h6">Insemination</h5><p class="small text-muted mb-0">A thin, flexible catheter is used to place the prepared sperm directly into the uterus.</p></div>
            </div>
            <div class="col-md-6">
              <div class="flow-step"><div class="step-num">4</div><h5 class="h6">Luteal Support</h5><p class="small text-muted mb-0">Progesterone supplements may be given to support the uterine lining for implantation.</p></div>
            </div>
          </div>

          <h3 class="mt-4">Success Rates</h3>
          <p>Thamarai Fertility has achieved over <strong>15,000+ IUI successes</strong>. The success rate of IUI depends on several factors including the woman\'s age, the cause of infertility, and sperm quality. On average, IUI success rates range from 10-20% per cycle.</p>

          <h3>Advantages of IUI</h3>
          <ul>
            <li>Less invasive than IVF</li>
            <li>More affordable than advanced ART procedures</li>
            <li>Minimal medication required</li>
            <li>Quick procedure (takes only minutes)</li>
            <li>Can be repeated in subsequent cycles</li>
          </ul>'''
    content = content.replace(old_section, custom_section)
    
    with open(output, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'✅ Created {filename}')

print(f"\n🎉 All branch pages created successfully!")