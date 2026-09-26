#!/usr/bin/env python3
"""
Thamarai Healthcare - Complete Page Generator
Generates all new content pages for the enterprise platform
"""
import os

BASE = r'c:\Users\ELCOT\Desktop\thamarai-healthcare'
TEMPLATE = os.path.join(BASE, 'iui.html')

with open(TEMPLATE, 'r', encoding='utf-8') as f:
    BASE_HTML = f.read()

def create_page(filename, info):
    output = os.path.join(BASE, filename)
    if os.path.exists(output):
        print(f'⏩ Skipping {filename} - already exists')
        return
    content = BASE_HTML
    
    content = content.replace(
        '<title>IUI Treatment | Thamarai Fertility & Women\'s Health Center</title>',
        f'<title>{info["title"]} | Thamarai Fertility & Women\'s Health Center</title>'
    )
    old_desc = 'name="description" content="Intrauterine Insemination (IUI) treatment at Thamarai Fertility - a safe, effective fertility procedure for couples trying to conceive."'
    content = content.replace(old_desc, f'name="description" content="{info["desc"]}"')
    content = content.replace('https://thamaraihealthcare.com/iui.html', f'https://thamaraihealthcare.com/{info["canonical"]}')
    content = content.replace('FERTILITY PROCEDURE', info['eyebrow'])
    old_hero = 'Intrauterine <span class="text-gradient">Insemination (IUI)</span>'
    content = content.replace(old_hero, info['hero_title'])
    old_sub = 'A safe, simple, and effective fertility treatment that places specially prepared sperm directly into the uterus.'
    content = content.replace(old_sub, info['hero_sub'])
    old_ctitle = 'What is IUI?'
    content = content.replace(old_ctitle, info['content_title'])
    old_text = 'Intrauterine Insemination (IUI) is a fertility treatment that involves placing specially prepared sperm directly into a woman\'s uterus around the time of ovulation. This procedure increases the number of sperm that reach the fallopian tubes, thereby increasing the chance of fertilization.'
    content = content.replace(old_text, info['content_text'])
    
    # Replace main section
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
    content = content.replace(old_section, info.get('custom_section', old_section))
    
    # Update active nav
    active = info.get('nav_active', 'Clinics')
    for m in ['Fertility', 'Tests', 'Procedures', 'Clinics']:
        content = content.replace(f'class="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown">{m}', f'class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">{m}')
    content = content.replace(f'class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">{active}', f'class="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown">{active}')
    
    with open(output, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'✅ Created {filename}')

def make_section(sections):
    html = ''
    for sec in sections:
        html += f'\n          <h3 class="mt-4">{sec["heading"]}</h3>\n          <p>{sec["content"]}</p>'
        if sec.get('list'):
            html += '\n          <ul>'
            for item in sec['list']:
                html += f'\n            <li>{item}</li>'
            html += '\n          </ul>'
        for sub in sec.get('subsections', []):
            html += f'\n          <h4 class="h5 mt-3">{sub["heading"]}</h4>\n          <p>{sub["content"]}</p>'
            if sub.get('list'):
                html += '\n          <ul>'
                for item in sub['list']:
                    html += f'\n            <li>{item}</li>'
                html += '\n          </ul>'
    html += '''
          <div class="bg-gradient-cta p-4 rounded-4 text-center text-white mt-4">
            <h4 class="text-white">Need expert medical guidance?</h4>
            <p class="text-white-50 mb-3">Our specialists are here to provide comprehensive care and treatment.</p>
            <a href="contact.html#makeAppointment" class="btn btn-accent btn-lg shadow-accent"><i class="bi bi-calendar-check me-2"></i>Book a Consultation</a>
          </div>'''
    return html

def hp(title, eyebrow, hero_title, hero_sub, sections, canonical=None, nav='Clinics'):
    return {
        'title': title, 'desc': f'{title} at Thamarai Fertility - comprehensive information on symptoms, causes, diagnosis, treatment options, and expert care.',
        'canonical': canonical or title.lower().replace(' ', '-')+'.html', 'eyebrow': eyebrow,
        'hero_title': hero_title, 'hero_sub': hero_sub,
        'content_title': f'About {title}', 'content_text': hero_sub,
        'custom_section': make_section(sections), 'nav_active': nav
    }

# Page definitions
pages = {
    'pcos.html': hp('PCOS - Polycystic Ovary Syndrome', 'WOMENS HEALTH', 'PCOS <span class="text-gradient">Management</span>',
        'Comprehensive diagnosis and treatment of Polycystic Ovary Syndrome affecting hormonal balance and fertility.',
        [{'heading':'What is PCOS?','content':'Polycystic Ovary Syndrome (PCOS) is a hormonal disorder common among women of reproductive age. Women with PCOS may have infrequent or prolonged menstrual periods or excess male hormone (androgen) levels. The ovaries may develop numerous small collections of fluid (follicles) and fail to regularly release eggs.'},
         {'heading':'Symptoms of PCOS','content':'PCOS symptoms often begin around the time of the first menstrual period.','list':['Irregular periods - infrequent, irregular or prolonged menstrual cycles','Excess androgen - elevated male hormones causing hirsutism, severe acne, male-pattern baldness','Polycystic ovaries - enlarged ovaries with numerous small fluid-filled sacs','Weight gain or difficulty losing weight','Thinning hair or hair loss from the scalp','Darkening of skin along neck creases, groin, and underneath breasts','Skin tags in the armpits or neck area']},
         {'heading':'Causes and Risk Factors','content':'The exact cause of PCOS is unknown.','list':['Excess insulin may increase androgen production','Low-grade inflammation affecting ovulation','Heredity - family history increases risk','Excess androgen production by ovaries']},
         {'heading':'Diagnosis','content':'There is no single test to diagnose PCOS.','list':['Physical exam checking for excess hair growth and acne','Pelvic ultrasound to check ovary appearance','Blood tests for hormone levels, glucose tolerance','Thyroid function tests']},
         {'heading':'Treatment Options','content':'PCOS treatment focuses on managing individual concerns.','subsections':[
             {'heading':'Lifestyle Modifications','content':'Weight loss through diet and exercise can improve PCOS symptoms.','list':['Low-glycemic index diet','Regular aerobic exercise and strength training','Stress management','Adequate sleep']},
             {'heading':'Medications','content':'Several medications help regulate cycles and treat symptoms.','list':['Birth control pills to regulate periods','Metformin for insulin resistance','Clomiphene or letrozole for ovulation induction','Anti-androgen medications']},
             {'heading':'Fertility Treatments','content':'For women trying to conceive with PCOS.','list':['Ovulation induction with letrozole or clomiphene','IUI with fertility medications','IVF for complex cases','Ovarian drilling procedure']}]},
         {'heading':'Complications','content':'PCOS can increase the risk of several health complications.','list':['Type 2 diabetes and gestational diabetes','High blood pressure and cardiovascular disease','Endometrial cancer risk','Metabolic syndrome','Sleep apnea','Depression and anxiety']}], canonical='pcos.html'),
    
    'endometriosis.html': hp('Endometriosis', 'WOMENS HEALTH', 'Endometriosis <span class="text-gradient">Care</span>',
        'Expert diagnosis and treatment of endometriosis - a painful condition where uterine-like tissue grows outside the uterus.',
        [{'heading':'What is Endometriosis?','content':'Endometriosis is an often painful disorder in which tissue similar to the endometrium grows outside your uterus, most commonly on your ovaries, fallopian tubes and the tissue lining your pelvis.'},
         {'heading':'Symptoms','content':'The primary symptom is pelvic pain, often associated with menstrual periods.','list':['Painful periods (dysmenorrhea)','Pain with intercourse','Pain with bowel movements or urination','Excessive bleeding','Infertility','Fatigue, diarrhea, constipation, bloating, nausea']},
         {'heading':'Stages of Endometriosis','content':'Classified into four stages based on location, extent, and depth.','list':['Stage I (Minimal) - small lesions, shallow implants','Stage II (Mild) - light lesions and shallow implants','Stage III (Moderate) - deep implants, some adhesions','Stage IV (Severe) - deep implants, extensive adhesions']},
         {'heading':'Diagnosis','content':'Diagnosing endometriosis requires a comprehensive approach.','list':['Pelvic examination','Ultrasound to detect endometriomas','MRI for detailed imaging','Laparoscopy - definitive diagnosis','Biopsy for confirmation']},
         {'heading':'Treatment Options','content':'Treatment depends on severity and fertility goals.','subsections':[
             {'heading':'Medical Management','content':'Pain management and hormonal therapy.','list':['NSAIDs for pain relief','Hormonal contraceptives','GnRH agonists','Progestin therapy','Aromatase inhibitors']},
             {'heading':'Surgical Treatment','content':'For moderate to severe cases.','list':['Laparoscopic excision of implants','Laparoscopic ablation','Endometrioma removal','Hysterectomy for severe cases']}]}], canonical='endometriosis.html'),
    
    'fibroids.html': hp('Uterine Fibroids', 'WOMENS HEALTH', 'Uterine <span class="text-gradient">Fibroids</span>',
        'Expert diagnosis and treatment of uterine fibroids - noncancerous growths affecting fertility and quality of life.',
        [{'heading':'What are Uterine Fibroids?','content':'Uterine fibroids are noncancerous growths of the uterus that often appear during childbearing years. Also called leiomyomas or myomas, they range from seedlings to bulky masses that can distort the uterus.'},
         {'heading':'Types','content':'Fibroids are classified by location.','list':['Intramural - within the muscular wall','Subserosal - outside the uterus','Submucosal - under the uterine lining','Pedunculated - on a stalk','Cervical - in the cervix']},
         {'heading':'Symptoms','content':'Many women have no symptoms. When present, symptoms may include:','list':['Heavy menstrual bleeding','Pelvic pressure and pain','Frequent urination','Constipation and bloating','Back or leg pain','Pain during intercourse','Infertility or recurrent pregnancy loss']},
         {'heading':'Causes and Risk Factors','content':'','list':['Genetic changes','Hormones - estrogen and progesterone promote growth','Age - more common in 30s and 40s','Family history','Obesity','Diet']},
         {'heading':'Diagnosis','content':'','list':['Pelvic examination','Ultrasound','3D Sonohysterosalpingogram','Hysteroscopy','MRI']},
         {'heading':'Treatment Options','content':'','subsections':[
             {'heading':'Medical Management','content':'','list':['NSAIDs','Iron supplements','Hormonal birth control','GnRH agonists','Tranexamic acid']},
             {'heading':'Minimally Invasive','content':'','list':['Uterine artery embolization','MRI-guided focused ultrasound','Radiofrequency ablation','Laparoscopic myomectomy','Hysteroscopic myomectomy']},
             {'heading':'Surgical Options','content':'','list':['Abdominal myomectomy','Hysterectomy','Endometrial ablation']}]}], canonical='fibroids.html'),
    
    'menstrual-disorders.html': hp('Menstrual Disorders', 'WOMENS HEALTH', 'Menstrual <span class="text-gradient">Disorders</span>',
        'Comprehensive care for menstrual disorders including heavy bleeding, irregular periods, painful periods, and PMS.',
        [{'heading':'Understanding Menstrual Disorders','content':'Menstrual disorders are problems affecting a woman\'s normal menstrual cycle, among the most common reasons for gynecological care.'},
         {'heading':'Types','content':'Common disorders include:','list':['Amenorrhea - absence of periods','Dysmenorrhea - severe cramps','Menorrhagia - heavy bleeding','Metrorrhagia - bleeding between periods','Oligomenorrhea - infrequent periods','PMS - premenstrual syndrome','PMDD - severe PMS']},
         {'heading':'Symptoms','content':'','list':['Missing three or more periods','Periods lasting longer than 7 days','Soaking through pads/tampons every hour','Passing large blood clots','Severe cramping','Bleeding between periods','Irregular cycle lengths']},
         {'heading':'Causes','content':'','list':['Hormonal imbalances','Uterine fibroids or polyps','Endometriosis','PCOS','Thyroid disorders','Pelvic Inflammatory Disease','Stress','Eating disorders']},
         {'heading':'Diagnosis','content':'','list':['Medical history and menstrual calendar','Physical and pelvic examination','Blood tests','Pelvic ultrasound','Endometrial biopsy','Hysteroscopy','MRI']},
         {'heading':'Treatment Options','content':'','subsections':[
             {'heading':'Medical Management','content':'','list':['NSAIDs','Hormonal contraceptives','Progestin therapy','Tranexamic acid','GnRH agonists','Antidepressants for PMDD']},
             {'heading':'Surgical Options','content':'','list':['Dilation and curettage (D&C)','Hysteroscopic resection','Endometrial ablation','Myomectomy','Hysterectomy']}]}], canonical='menstrual-disorders.html'),
    
    'pregnancy-care.html': hp('Pregnancy Care', 'PREGNANCY CARE', 'Pregnancy <span class="text-gradient">Care</span>',
        'Comprehensive antenatal and pregnancy care services ensuring the health of both mother and baby throughout pregnancy.',
        [{'heading':'Comprehensive Pregnancy Care','content':'At Thamarai Fertility, we provide complete pregnancy care services from conception through delivery.'},
         {'heading':'Antenatal Care Services','content':'','list':['Early pregnancy assessment and dating scan','Regular growth monitoring and ultrasound','Blood tests and glucose screening','Anomaly scans at 18-22 weeks','Fetal Doppler studies','Nutritional counseling','Birth planning classes']},
         {'heading':'Trimester-by-Trimester Care','content':'','subsections':[
             {'heading':'First Trimester (Weeks 1-12)','content':'','list':['Confirmation of pregnancy','Dating scan','Nuchal translucency scan','Management of morning sickness','Lifestyle guidance']},
             {'heading':'Second Trimester (Weeks 13-28)','content':'','list':['Anomaly scan','Glucose tolerance test','Blood pressure monitoring','Iron supplementation']},
             {'heading':'Third Trimester (Weeks 29-40)','content':'','list':['Growth scans','Breech presentation checks','Birth plan discussions','Breastfeeding classes','Signs of labor education']}]},
         {'heading':'Nutrition During Pregnancy','content':'','list':['Folic acid supplementation','Iron-rich foods','Calcium for bone development','Adequate protein','Omega-3 fatty acids','Fruits, vegetables, whole grains','8-10 glasses of water daily']},
         {'heading':'Warning Signs','content':'Contact your doctor immediately if you experience:','list':['Vaginal bleeding or fluid leakage','Severe abdominal pain','Sudden swelling of face/hands/feet','Severe headaches','Decreased fetal movement','Fever or chills','Painful urination']}], canonical='pregnancy-care.html'),
    
    'postnatal-care.html': hp('Postnatal Care', 'POSTNATAL CARE', 'Postnatal <span class="text-gradient">Care</span>',
        'Comprehensive postnatal care for new mothers focusing on recovery, breastfeeding support, and emotional well-being.',
        [{'heading':'What is Postnatal Care?','content':'Postnatal care is provided to mother and baby immediately after childbirth and during the first six weeks (the postpartum period).'},
         {'heading':'Postnatal Care Services','content':'','list':['Immediate postpartum assessment','Uterine involution monitoring','Perineal wound care','C-section wound care','Breastfeeding support','Postnatal exercises','Emotional well-being screening','Family planning counseling','Newborn care education']},
         {'heading':'Physical Recovery','content':'Your body goes through significant changes after delivery.','list':['Uterine healing over 6 weeks','Vaginal recovery 2-3 weeks','C-section recovery 4-6 weeks','Hormonal changes','Lochia (bleeding) 4-6 weeks','Breast engorgement','Gradual weight loss']},
         {'heading':'Breastfeeding Support','content':'','list':['Positioning and latching techniques','Management of engorgement and mastitis','Pumping and milk storage guidance','Returning to work planning','Tongue-tie assessment']},
         {'heading':'Emotional Well-being','content':'','list':['Baby blues - first 2 weeks','Postpartum depression support','Postpartum anxiety','Bonding difficulties','Sleep deprivation strategies']},
         {'heading':'When to Seek Help','content':'Contact your doctor if you experience:','list':['Heavy vaginal bleeding','Large blood clots','Fever above 100.4°F','Severe headache with vision changes','Signs of wound infection','Thoughts of harming yourself or baby']}], canonical='postnatal-care.html'),
    
    'pediatrics.html': hp('Pediatrics', 'PEDIATRICS', 'Pediatric <span class="text-gradient">Care</span>',
        'Comprehensive pediatric care for children from newborns to adolescents, including well-child visits, vaccinations, and developmental assessments.',
        [{'heading':'Pediatric Care at Thamarai','content':'Our pediatric department provides complete healthcare for children from birth through adolescence.'},
         {'heading':'Newborn Care Services','content':'','list':['Newborn assessment and Apgar scoring','Physical examination within 24 hours','Newborn screening tests','Jaundice monitoring','Breastfeeding support','Umbilical cord care','Parent education']},
         {'heading':'Vaccination Schedule','content':'We follow the recommended immunization schedule.','list':['Birth - BCG, Hepatitis B, OPV','6 Weeks - DTwP/IPV, Hepatitis B, Rotavirus, PCV','10 Weeks - DTwP/IPV, Rotavirus, PCV','14 Weeks - DTwP/IPV, Hepatitis B, Rotavirus, PCV','9 Months - Measles, Rubella','12 Months - Hepatitis A, PCV booster','15 Months - MMR, Varicella','18 Months - DTwP/IPV booster','5 Years - DTwP/IPV booster, MMR','10-12 Years - Tdap, HPV']},
         {'heading':'Growth Monitoring','content':'','list':['Height, weight, head circumference measurements','WHO growth chart plotting','Developmental screening','Motor skills assessment','Language evaluation','Vision and hearing screening']},
         {'heading':'Common Conditions Treated','content':'','list':['Respiratory infections','Asthma and allergies','Ear infections','Gastrointestinal issues','Skin conditions','Urinary tract infections','Growth concerns','Developmental delays']}], canonical='pediatrics.html'),
    
    'neonatology.html': hp('Neonatology', 'NEONATOLOGY', 'Neonatology <span class="text-gradient">Services</span>',
        'Specialized medical care for newborn infants, particularly premature or ill newborns requiring intensive care in our NICU.',
        [{'heading':'What is Neonatology?','content':'Neonatology focuses on medical care of newborn infants, especially premature or ill newborns. Our Level III NICU provides the highest standard of care.'},
         {'heading':'NICU Services','content':'','list':['24/7 monitoring by neonatologists','Advanced respiratory support (ventilators, CPAP)','Total parenteral nutrition','Thermoregulation with incubators','Phototherapy for jaundice','Cranial ultrasound and echocardiography','Neonatal transport services','Developmental care']},
         {'heading':'Premature Baby Care','content':'','list':['Kangaroo Mother Care','Temperature management','Respiratory support','Feeding support','Infection prevention','Retinopathy screening','Hearing screening','Neurodevelopmental follow-up']},
         {'heading':'Conditions We Treat','content':'','list':['Prematurity','Low birth weight','Respiratory distress syndrome','Neonatal jaundice','Meconium aspiration','Neonatal sepsis','Perinatal asphyxia','Congenital anomalies']},
         {'heading':'Why Choose Thamarai?','content':'','list':['Level III NICU with advanced equipment','Round-the-clock neonatologist coverage','Integrated care with obstetrics','Family-centered care approach','High survival rates']}], canonical='neonatology.html'),
    
    'breastfeeding-support.html': hp('Breastfeeding Support', 'BREASTFEEDING', 'Breastfeeding <span class="text-gradient">Support</span>',
        'Expert lactation consultation and breastfeeding support services for new mothers.',
        [{'heading':'Breastfeeding Support at Thamarai','content':'Our certified lactation consultants provide expert support, education, and guidance to help mothers successfully breastfeed.'},
         {'heading':'Our Services','content':'','list':['Prenatal breastfeeding education','In-hospital lactation support','One-on-one consultation','Positioning and latching guidance','Pumping and milk storage education','Returning to work planning','Tongue-tie assessment','Mastitis management','Low milk supply evaluation']},
         {'heading':'Benefits of Breastfeeding','content':'','list':['Complete nutrition for baby','Antibodies boosting immunity','Reduced risk of infections','Lower SIDS risk','Healthy weight gain','Brain development support','Uterine contraction after birth','Reduced maternal cancer risk']},
         {'heading':'Common Challenges','content':'','list':['Sore nipples - proper positioning','Engorgement - frequent feeding','Mastitis - antibiotics and rest','Low milk supply - power pumping','Thrush - antifungal treatment','Latching difficulties - consultant support']},
         {'heading':'Pumping and Storage Guide','content':'','list':['Room temperature - up to 4 hours','Refrigerator - up to 4 days','Freezer compartment - up to 2 weeks','Deep freezer - up to 6 months','Thaw in refrigerator or warm water','Never microwave breast milk']}], canonical='breastfeeding-support.html'),
    
    'fertility-preservation.html': hp('Fertility Preservation', 'FERTILITY PRESERVATION', 'Fertility <span class="text-gradient">Preservation</span>',
        'Advanced fertility preservation options including egg freezing, sperm freezing, and embryo freezing.',
        [{'heading':'What is Fertility Preservation?','content':'Fertility preservation involves saving eggs, sperm, or reproductive tissue to help individuals have biological children in the future.'},
         {'heading':'Who Should Consider?','content':'','list':['Women diagnosed with cancer needing chemotherapy','Men diagnosed with cancer','Women with autoimmune diseases','Women with endometriosis','Individuals undergoing gender transition','Women delaying childbearing','Family history of early menopause']},
         {'heading':'Egg Freezing','content':'','list':['Ovarian stimulation for 10-14 days','Ultrasound and blood test monitoring','Egg retrieval under sedation (15-20 min)','Vitrification freezing at -196°C','Storage in liquid nitrogen','Best outcomes before age 35']},
         {'heading':'Sperm Freezing','content':'','list':['Semen sample collection','Semen analysis','Cryoprotectant addition','Slow freezing or vitrification','Storage in liquid nitrogen','Used for IUI, IVF, or ICSI']},
         {'heading':'Embryo Freezing','content':'','list':['Eggs retrieved and fertilized via IVF/ICSI','Embryos cultured to blastocyst stage','High-quality embryos selected','Vitrification (>95% survival)','Transfer in future cycles without stimulation']}], canonical='fertility-preservation.html', nav='Procedures'),
    
    'ovarian-stimulation.html': hp('Ovarian Stimulation', 'FERTILITY TREATMENT', 'Ovarian <span class="text-gradient">Stimulation</span>',
        'Controlled ovarian stimulation for IUI and IVF treatments with close monitoring to optimize outcomes.',
        [{'heading':'What is Ovarian Stimulation?','content':'Ovarian stimulation uses fertility medications to stimulate ovaries to develop multiple follicles, maximizing chances of successful fertilization and pregnancy.'},
         {'heading':'For IUI','content':'Mild stimulation is used.','list':['Oral medications (clomiphene/letrozole) for 5 days','Low-dose gonadotropin injections if needed','Ultrasound monitoring of follicles','Trigger injection at 18-20mm','IUI 36-40 hours after trigger','1-3 mature follicles typical']},
         {'heading':'For IVF/ICSI','content':'More intensive stimulation required.','list':['Gonadotropin injections for 10-14 days','GnRH antagonist protocol','Monitoring every 2-3 days','Dose adjustments as needed','Trigger when 3+ follicles reach 18mm','Goal: 8-15 mature follicles']},
         {'heading':'OHSS','content':'Ovarian Hyperstimulation Syndrome - a potential complication.','list':['Mild - bloating, mild pain','Moderate - significant pain, vomiting','Severe - rapid weight gain, breathing difficulty','Risk factors: young age, PCOS, high AMH','Prevention: coasting, GnRH trigger','Close monitoring for early detection']},
         {'heading':'Medications Used','content':'','list':['Clomiphene citrate (oral)','Letrozole (oral)','Recombinant FSH (Gonal-F, Puregon)','Urinary gonadotropins (Menopur)','GnRH antagonists (Cetrotide)','hCG trigger (Ovidrel)','Progesterone supplements']}], canonical='ovarian-stimulation.html', nav='Procedures'),
}

# Simple test pages
simple_pages = {
    'baseline-scan.html': {'title':'Baseline Scan & Follicular Study','desc':'Baseline ultrasound and follicular study monitoring follicle development for IUI and IVF.','canonical':'baseline-scan.html','eyebrow':'OVULATION TEST','hero_title':'Baseline Scan & <span class="text-gradient">Follicular Study</span>','hero_sub':'Ultrasound monitoring of ovarian follicles to track egg development for fertility treatment.','content_title':'What is a Follicular Study?','content_text':'A follicular study is a series of ultrasound scans performed to monitor the growth and development of ovarian follicles, essential for planning IUI, IVF, or natural conception.','nav_active':'Tests'},
    'hormonal-assay.html': {'title':'Hormonal Assay','desc':'Hormonal assay testing evaluating hormone levels for fertility assessment.','canonical':'hormonal-assay.html','eyebrow':'HORMONE TEST','hero_title':'Hormonal <span class="text-gradient">Assay</span>','hero_sub':'Blood tests to evaluate reproductive hormone levels and identify imbalances affecting fertility.','content_title':'What is a Hormonal Assay?','content_text':'A hormonal assay measures levels of various reproductive hormones to evaluate ovarian reserve, ovulatory function, and identify hormonal imbalances.','nav_active':'Tests'},
    'hormone-testing.html': {'title':'Hormone Testing','desc':'Complete hormone panel including FSH, LH, AMH, prolactin, and thyroid function tests.','canonical':'hormone-testing.html','eyebrow':'HORMONE TEST','hero_title':'Hormone <span class="text-gradient">Testing</span>','hero_sub':'Complete hormone panel to evaluate fertility potential and diagnose hormonal disorders.','content_title':'Hormone Testing for Fertility','content_text':'Key hormones tested include FSH, LH, estradiol, progesterone, AMH, prolactin, and thyroid hormones for comprehensive reproductive health assessment.','nav_active':'Tests'},
    'semen-analysis.html': {'title':'Semen Analysis','desc':'Comprehensive evaluation of sperm count, motility, morphology for male fertility assessment.','canonical':'semen-analysis.html','eyebrow':'MALE FERTILITY TEST','hero_title':'Semen <span class="text-gradient">Analysis</span>','hero_sub':'Laboratory test evaluating sperm health, count, motility, and morphology for male fertility.','content_title':'What is Semen Analysis?','content_text':'Semen analysis examines sperm quantity and quality - count, motility (movement), morphology (shape), and other crucial fertility parameters.','nav_active':'Tests'},
    'y-chromosome-deletion.html': {'title':'Y Chromosome Micro Deletion','desc':'Genetic test identifying Y chromosome deletions causing male infertility.','canonical':'y-chromosome-deletion.html','eyebrow':'GENETIC TEST','hero_title':'Y Chromosome <span class="text-gradient">Micro Deletion</span>','hero_sub':'Genetic testing for Y chromosome deletions causing severe male factor infertility.','content_title':'Y Chromosome Micro Deletion Analysis','content_text':'Y chromosome micro deletion is a genetic cause of male infertility where small pieces of the Y chromosome are missing, affecting sperm production.','nav_active':'Tests'},
    'sperm-dna-fragmentation.html': {'title':'Sperm DNA Fragmentation','desc':'DNA damage assessment in sperm affecting fertility and pregnancy outcomes.','canonical':'sperm-dna-fragmentation.html','eyebrow':'SPERM TEST','hero_title':'Sperm DNA <span class="text-gradient">Fragmentation</span>','hero_sub':'Testing DNA damage in sperm that can impact fertilization, embryo development, and pregnancy success.','content_title':'What is Sperm DNA Fragmentation?','content_text':'Sperm DNA fragmentation testing measures DNA damage within sperm cells. High rates affect fertilization, embryo quality, and increase miscarriage risk.','nav_active':'Tests'},
    'karyotyping.html': {'title':'Karyotyping','desc':'Chromosomal analysis identifying genetic abnormalities causing infertility or recurrent pregnancy loss.','canonical':'karyotyping.html','eyebrow':'GENETIC TEST','hero_title':'<span class="text-gradient">Karyotyping</span>','hero_sub':'Chromosomal analysis to identify abnormalities causing infertility or recurrent pregnancy loss.','content_title':'What is Karyotyping?','content_text':'Karyotyping examines chromosomes to identify structural abnormalities or numerical changes causing infertility.','nav_active':'Tests'},
    'sonohysterosalpingogram.html': {'title':'3D Sonohysterosalpingogram','desc':'Advanced ultrasound evaluating uterine cavity and fallopian tube patency.','canonical':'sonohysterosalpingogram.html','eyebrow':'UTERINE TEST','hero_title':'3D <span class="text-gradient">Sonohysterosalpingogram</span>','hero_sub':'Advanced 3D ultrasound imaging to evaluate uterine cavity and assess tubal patency.','content_title':'What is 3D Sonohysterosalpingogram?','content_text':'3D SIS is an advanced ultrasound technique using saline contrast to visualize the uterine cavity and evaluate tubal patency.','nav_active':'Tests'},
    'pelvic-scan.html': {'title':'Pelvic Scan','desc':'Comprehensive ultrasound imaging of pelvic organs for fertility assessment.','canonical':'pelvic-scan.html','eyebrow':'PELVIC EVALUATION','hero_title':'Pelvic <span class="text-gradient">Scan</span>','hero_sub':'Ultrasound imaging of pelvic organs to evaluate reproductive health.','content_title':'What is a Pelvic Scan?','content_text':'A pelvic scan creates images of the pelvis including uterus, ovaries, and fallopian tubes, essential for diagnosing gynecological conditions.','nav_active':'Tests'},
}

pages.update(simple_pages)

print("🚀 Generating all new pages...")
print(f"📝 Total pages: {len(pages)}")
print("=" * 50)

for filename, info in pages.items():
    if os.path.exists(os.path.join(BASE, filename)):
        print(f'⏩ Skipping {filename} - already exists')
        continue
    create_page(filename, info)

print(f"\n🎉 All pages generated successfully!")