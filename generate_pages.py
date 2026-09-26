import os, shutil

base = r'c:\Users\ELCOT\Desktop\thamarai-healthcare'
template = os.path.join(base, 'iui.html')

pages = {
    'icsi.html': {
        'title': 'ICSI Procedure',
        'desc': 'Intracytoplasmic Sperm Injection (ICSI) at Thamarai Fertility - advanced treatment for severe male factor infertility by injecting a single sperm directly into an egg.',
        'canonical': 'icsi.html',
        'eyebrow': 'ADVANCED ART',
        'hero_title': 'Intracytoplasmic Sperm Injection <span class="text-gradient">(ICSI)</span>',
        'hero_sub': 'Advanced micromanipulation technique where a single healthy sperm is injected directly into the egg for fertilization.',
        'content_title': 'What is ICSI?',
        'content_text': 'Intracytoplasmic Sperm Injection (ICSI) is a specialized form of IVF where a single sperm is injected directly into the cytoplasm of an egg. This technique is particularly effective for severe male factor infertility and has helped thousands of couples achieve pregnancy.'
    },
    'sperm-freezing.html': {
        'title': 'Sperm Freezing',
        'desc': 'Sperm freezing and cryopreservation at Thamarai Fertility - preserve fertility for future use with advanced sperm banking technology.',
        'canonical': 'sperm-freezing.html',
        'eyebrow': 'FERTILITY PRESERVATION',
        'hero_title': 'Sperm <span class="text-gradient">Freezing</span>',
        'hero_sub': 'Preserve your fertility with advanced sperm cryopreservation technology for future family building.',
        'content_title': 'What is Sperm Freezing?',
        'content_text': 'Sperm freezing, also known as sperm cryopreservation, is a process where sperm cells are preserved at very low temperatures for future use. This allows men to maintain their fertility potential even when facing treatments that may affect sperm production.'
    },
    'embryo-freezing.html': {
        'title': 'Embryo Freezing',
        'desc': 'Embryo freezing (cryopreservation) at Thamarai Fertility - preserve embryos for future IVF cycles with high survival rates.',
        'canonical': 'embryo-freezing.html',
        'eyebrow': 'EMBRYO CRYOPRESERVATION',
        'hero_title': 'Embryo <span class="text-gradient">Freezing</span>',
        'hero_sub': 'Cryopreservation of embryos for future use, offering higher cumulative pregnancy rates per egg retrieval cycle.',
        'content_title': 'What is Embryo Freezing?',
        'content_text': 'Embryo freezing (cryopreservation) allows couples to store surplus high-quality embryos from an IVF cycle for future use. This increases the cumulative chance of pregnancy from a single egg retrieval and reduces the need for repeated ovarian stimulation.'
    },
    'pgd.html': {
        'title': 'PGD - Genetic Testing',
        'desc': 'Preimplantation Genetic Diagnosis (PGD) at Thamarai Fertility - screen embryos for genetic disorders before implantation for healthy pregnancies.',
        'canonical': 'pgd.html',
        'eyebrow': 'GENETIC TESTING',
        'hero_title': 'Preimplantation Genetic Diagnosis <span class="text-gradient">(PGD)</span>',
        'hero_sub': 'Advanced genetic screening of embryos to identify genetic disorders before implantation, ensuring healthier pregnancies.',
        'content_title': 'What is PGD?',
        'content_text': 'Preimplantation Genetic Diagnosis (PGD) is a cutting-edge technique used in conjunction with IVF to screen embryos for genetic abnormalities before they are transferred to the uterus. This helps prevent passing on inherited genetic disorders.'
    },
    'egg-donation.html': {
        'title': 'Egg & Embryo Donation',
        'desc': 'Egg and embryo donation program at Thamarai Fertility - helping women achieve pregnancy with donated eggs or embryos.',
        'canonical': 'egg-donation.html',
        'eyebrow': 'DONOR PROGRAM',
        'hero_title': 'Egg & Embryo <span class="text-gradient">Donation</span>',
        'hero_sub': 'Helping women achieve pregnancy through anonymous egg and embryo donation programs with rigorous screening.',
        'content_title': 'Egg & Embryo Donation',
        'content_text': 'Egg and embryo donation offers hope to women who cannot conceive with their own eggs due to advanced age, premature ovarian failure, genetic disorders, or repeated IVF failures. Donors undergo thorough medical and genetic screening.'
    },
    'surrogacy.html': {
        'title': 'Surrogacy',
        'desc': 'Surrogacy program at Thamarai Fertility - helping intended parents achieve their dream of parenthood through gestational surrogacy.',
        'canonical': 'surrogacy.html',
        'eyebrow': 'FAMILY BUILDING',
        'hero_title': '<span class="text-gradient">Surrogacy</span> Program',
        'hero_sub': 'A compassionate path to parenthood for couples and individuals who cannot carry a pregnancy themselves.',
        'content_title': 'What is Surrogacy?',
        'content_text': 'Surrogacy is an arrangement where a woman (the surrogate) carries and delivers a child for another couple or person (the intended parents). At Thamarai Fertility, we offer gestational surrogacy where the surrogate has no genetic relationship to the child.'
    },
    'uterine-factor.html': {
        'title': 'Uterine Factor Infertility',
        'desc': 'Uterine factor infertility at Thamarai Fertility - diagnosis and treatment for fibroids, polyps, adhesions, and uterine abnormalities.',
        'canonical': 'uterine-factor.html',
        'eyebrow': 'UTERINE HEALTH',
        'hero_title': 'Uterine Factor <span class="text-gradient">Infertility</span>',
        'hero_sub': 'Understanding how uterine abnormalities can affect fertility and the advanced treatments available.',
        'content_title': 'Understanding Uterine Factor',
        'content_text': 'The uterus plays a vital role in fertility by providing the environment for embryo implantation and fetal development. Uterine factor infertility occurs when structural or functional abnormalities of the uterus prevent successful pregnancy.'
    },
    'ovulatory-factor.html': {
        'title': 'Ovulatory Factor Infertility',
        'desc': 'Ovulatory factor infertility at Thamarai Fertility - diagnosis and treatment for ovulation disorders including PCOS and hormonal imbalances.',
        'canonical': 'ovulatory-factor.html',
        'eyebrow': 'OVULATION',
        'hero_title': 'Ovulatory Factor <span class="text-gradient">Infertility</span>',
        'hero_sub': 'Understanding ovulation disorders and how they affect fertility, with comprehensive diagnostic and treatment options.',
        'content_title': 'Ovulatory Factor Infertility',
        'content_text': 'Ovulation disorders are among the most common causes of female infertility. Regular ovulation is essential for conception, and when ovulation is irregular or absent, fertility is significantly affected.'
    },
    'tubal-factor.html': {
        'title': 'Tubal Factor Infertility',
        'desc': 'Tubal factor infertility at Thamarai Fertility - diagnosis and treatment for blocked or damaged fallopian tubes.',
        'canonical': 'tubal-factor.html',
        'eyebrow': 'FALLOPIAN TUBES',
        'hero_title': 'Tubal Factor <span class="text-gradient">Infertility</span>',
        'hero_sub': 'How blocked or damaged fallopian tubes affect fertility and the advanced treatments available to overcome this challenge.',
        'content_title': 'Tubal Factor Infertility',
        'content_text': 'The fallopian tubes play a crucial role in fertility as the site where fertilization occurs and the pathway for the embryo to reach the uterus. Tubal factor infertility occurs when the fallopian tubes are blocked, damaged, or scarred.'
    },
    'pelvic-factor.html': {
        'title': 'Pelvic Factor Infertility',
        'desc': 'Pelvic factor infertility at Thamarai Fertility - diagnosis and treatment for endometriosis, pelvic adhesions, and pelvic inflammatory disease.',
        'canonical': 'pelvic-factor.html',
        'eyebrow': 'PELVIC HEALTH',
        'hero_title': 'Pelvic Factor <span class="text-gradient">Infertility</span>',
        'hero_sub': 'How pelvic conditions like endometriosis and adhesions can affect fertility and the treatment options available.',
        'content_title': 'Pelvic Factor Infertility',
        'content_text': 'Pelvic factor infertility refers to fertility problems caused by conditions affecting the pelvic region, including endometriosis, pelvic inflammatory disease (PID), and pelvic adhesions.'
    },
    'coital-factor.html': {
        'title': 'Coital Factor Infertility',
        'desc': 'Coital factor infertility at Thamarai Fertility - addressing sexual difficulties that affect conception including erectile dysfunction and ejaculation disorders.',
        'canonical': 'coital-factor.html',
        'eyebrow': 'SEXUAL HEALTH',
        'hero_title': 'Coital Factor <span class="text-gradient">Infertility</span>',
        'hero_sub': 'Understanding how sexual difficulties can impact fertility and the supportive treatments available.',
        'content_title': 'Coital Factor Infertility',
        'content_text': 'Coital factor infertility refers to fertility problems arising from difficulties with sexual intercourse that prevent successful conception. This includes erectile dysfunction, ejaculation disorders, and other sexual difficulties.'
    },
    'fetal-medicine.html': {
        'title': 'Fetal Medicine',
        'desc': 'Fetal medicine unit at Thamarai Fertility - advanced prenatal diagnosis, fetal ultrasound, and management of high-risk pregnancies.',
        'canonical': 'fetal-medicine.html',
        'eyebrow': 'FETAL CARE',
        'hero_title': 'Fetal Medicine <span class="text-gradient">Unit</span>',
        'hero_sub': 'Advanced prenatal diagnosis and comprehensive care for the unborn baby with state-of-the-art technology.',
        'content_title': 'Fetal Medicine at Thamarai',
        'content_text': 'The fetal medicine unit at Thamarai Fertility provides comprehensive care for the unborn baby. With technological advances, the care for the unborn fetus has assumed newer dimensions, allowing early detection and management of potential issues.'
    },
    'genetic-clinic.html': {
        'title': 'Genetic Clinic',
        'desc': 'Genetic clinic at Thamarai Fertility - genetic counseling, carrier screening, PGD, and chromosomal analysis for couples planning pregnancy.',
        'canonical': 'genetic-clinic.html',
        'eyebrow': 'GENETICS',
        'hero_title': '<span class="text-gradient">Genetic</span> Clinic',
        'hero_sub': 'Comprehensive genetic counseling and testing under one roof with expert genetic specialists.',
        'content_title': 'Genetic Clinic Services',
        'content_text': 'The Genetic Clinic at Thamarai Fertility offers a comprehensive approach to genetic health with genetic counseling and advanced genetic laboratory services under one roof.'
    },
    'endoscopy-clinic.html': {
        'title': 'Endoscopy Clinic',
        'desc': 'Endoscopy clinic at Thamarai Fertility - minimally invasive hysteroscopy and laparoscopy for diagnosis and treatment of reproductive issues.',
        'canonical': 'endoscopy-clinic.html',
        'eyebrow': 'MINIMALLY INVASIVE',
        'hero_title': 'Endoscopy <span class="text-gradient">Clinic</span>',
        'hero_sub': 'Minimally invasive diagnostic and therapeutic procedures for menstrual and reproductive health issues.',
        'content_title': 'Endoscopy Clinic',
        'content_text': 'The Endoscopy Clinic at Thamarai Fertility specializes in minimally invasive procedures to diagnose and treat conditions affecting the reproductive organs. Problems affecting menstrual and reproductive health are analyzed by special investigations and treated with advanced techniques.'
    },
    'andrology-clinic.html': {
        'title': 'Andrology Clinic',
        'desc': 'Andrology clinic at Thamarai Fertility - comprehensive male fertility assessment, semen analysis, and treatment for male infertility.',
        'canonical': 'andrology-clinic.html',
        'eyebrow': 'MALE HEALTH',
        'hero_title': '<span class="text-gradient">Andrology</span> Clinic',
        'hero_sub': 'Specialized male fertility assessment and treatment center with comprehensive diagnostic capabilities.',
        'content_title': 'Andrology Clinic Services',
        'content_text': 'The Andrology Clinic at Thamarai Fertility provides comprehensive male fertility assessment and treatment. Male infertility is one of the major causes of a barren marriage, and our specialists provide thorough evaluation and advanced treatments.'
    },
    'high-risk-pregnancy.html': {
        'title': 'High Risk Pregnancy Care',
        'desc': 'High-risk pregnancy care at Thamarai Fertility - specialized management for women with medical conditions or pregnancy complications.',
        'canonical': 'high-risk-pregnancy.html',
        'eyebrow': 'HIGH RISK PREGNANCY',
        'hero_title': 'High Risk Pregnancy <span class="text-gradient">Care</span>',
        'hero_sub': 'Specialized medical care for women with high-risk pregnancies ensuring the best outcomes for mother and baby.',
        'content_title': 'High Risk Pregnancy Care',
        'content_text': 'High-risk pregnancy care at Thamarai Fertility provides comprehensive management for women with medical conditions or pregnancy complications that require specialized attention and monitoring.'
    },
    'cancer-screening.html': {
        'title': 'Cancer Screening for Women',
        'desc': 'Cancer screening for women at Thamarai Fertility - cervical cancer screening, breast cancer awareness, and preventive gynecological care.',
        'canonical': 'cancer-screening.html',
        'eyebrow': 'WOMENS HEALTH',
        'hero_title': 'Cancer Screening <span class="text-gradient">& Prevention</span>',
        'hero_sub': 'Comprehensive cancer screening and preventive care for women to detect and prevent gynecological cancers early.',
        'content_title': 'Cancer Screening Services',
        'content_text': 'Cancer screening is an essential part of women\'s preventive healthcare. At Thamarai Fertility, we provide comprehensive screening services to detect gynecological cancers at their earliest, most treatable stages.'
    },
    'menopause.html': {
        'title': 'Menopause Management',
        'desc': 'Menopause management at Thamarai Fertility - expert care for perimenopause, menopause symptoms, hormone therapy, and bone health.',
        'canonical': 'menopause.html',
        'eyebrow': 'WOMENS HEALTH',
        'hero_title': 'Menopause <span class="text-gradient">Management</span>',
        'hero_sub': 'Comprehensive care and support for women navigating the transition through perimenopause and menopause.',
        'content_title': 'Understanding Menopause',
        'content_text': 'Menopause is a natural biological process that marks the end of a woman\'s reproductive years. At Thamarai Fertility, we provide comprehensive support and treatment options to help women navigate this transition comfortably.'
    },
    'adolescence.html': {
        'title': 'Adolescent Gynecology',
        'desc': 'Adolescent gynecology at Thamarai Fertility - specialized care for teenage girls addressing menstrual disorders, reproductive health education, and development concerns.',
        'canonical': 'adolescence.html',
        'eyebrow': 'ADOLESCENT HEALTH',
        'hero_title': 'Adolescent <span class="text-gradient">Gynecology</span>',
        'hero_sub': 'Specialized gynecological care for teenage girls addressing their unique health needs with sensitivity and expertise.',
        'content_title': 'Adolescent Gynecology Services',
        'content_text': 'Adolescent gynecology addresses the unique reproductive health needs of teenage girls. At Thamarai Fertility, we provide specialized care in a comfortable and confidential environment.'
    },
    'counselling.html': {
        'title': 'Prenatal & Postnatal Counselling',
        'desc': 'Prenatal and postnatal counselling at Thamarai Fertility - comprehensive support for parents-to-be including baby care, lactation consultancy, and parenting classes.',
        'canonical': 'counselling.html',
        'eyebrow': 'COUNSELLING',
        'hero_title': 'Prenatal & Postnatal <span class="text-gradient">Counselling</span>',
        'hero_sub': 'Comprehensive guidance and support for parents-to-be from conception through pregnancy, childbirth, and beyond.',
        'content_title': 'Pregnancy Counselling Services',
        'content_text': 'Thamarai Fertility, in partnership with Siksha Baby Care, provides comprehensive counselling services to support parents-to-be through every stage of their journey from conception to parenting.'
    }
}

with open(template, 'r', encoding='utf-8') as f:
    base_content = f.read()

for filename, info in pages.items():
    output = os.path.join(base, filename)
    
    content = base_content
    
    # Replace title
    content = content.replace('<title>IUI Treatment | Thamarai Fertility & Women\'s Health Center</title>', 
        f'<title>{info["title"]} | Thamarai Fertility & Women\'s Health Center</title>')
    
    # Replace description
    content = content.replace('name="description" content="Intrauterine Insemination (IUI) treatment at Thamarai Fertility - a safe, effective fertility procedure for couples trying to conceive."',
        f'name="description" content="{info["desc"]}"')
    
    # Replace canonical
    content = content.replace('https://thamaraihealthcare.com/iui.html', f'https://thamaraihealthcare.com/{info["canonical"]}')
    
    # Replace eyebrow
    content = content.replace('FERTILITY PROCEDURE', info['eyebrow'])
    
    # Replace hero title
    old_hero = 'Intrauterine <span class="text-gradient">Insemination (IUI)</span>'
    content = content.replace(old_hero, info['hero_title'])
    
    # Replace hero subtitle
    old_sub = 'A safe, simple, and effective fertility treatment that places specially prepared sperm directly into the uterus.'
    content = content.replace(old_sub, info['hero_sub'])
    
    # Replace content title
    old_ctitle = 'What is IUI?'
    content = content.replace(old_ctitle, info['content_title'])
    
    # Replace main content intro paragraph
    old_text = 'Intrauterine Insemination (IUI) is a fertility treatment that involves placing specially prepared sperm directly into a woman\'s uterus around the time of ovulation. This procedure increases the number of sperm that reach the fallopian tubes, thereby increasing the chance of fertilization.'
    content = content.replace(old_text, info['content_text'])
    
    # Update active nav class
    nav_key = filename.replace('.html', '')
    if nav_key in ['icsi', 'sperm-freezing', 'embryo-freezing', 'pgd', 'egg-donation', 'surrogacy']:
        content = content.replace('class="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown">Procedures', 'class="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown">Procedures')
        content = content.replace('href="ivf.html">IVF – Egg Retrieval', f'href="{filename}">IVF – Egg Retrieval')
    
    with open(output, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✅ Created {filename} - {info["title"]}')

print(f'\n🎉 All {len(pages)} pages created successfully!')