# 🌸 Thamarai Fertility & Women's Health Center

<p align="center">
  <img src="https://img.shields.io/badge/Healthcare-Website-0ea5a4?style=for-the-badge&logo=heart&logoColor=white" />
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JavaScript-f97316?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Bootstrap-5.3.2-7952b3?style=for-the-badge&logo=bootstrap&logoColor=white" />
  <img src="https://img.shields.io/badge/Backend-Node.js%20%7C%20Express-339933?style=for-the-badge&logo=node.js&logoColor=white" />
  <img src="https://img.shields.io/badge/Database-API%20Driven-2563eb?style=for-the-badge&logo=databricks&logoColor=white" />
</p>

<p align="center">
  <strong>A modern, responsive fertility & women's healthcare web platform</strong>
</p>

<p align="center">
  <a href="https://thamaraihealthcare.com/">🌐 Live Website</a>
  •
  <a href="#-features">Features</a>
  •
  <a href="#-technology-stack">Tech Stack</a>
  •
  <a href="#-project-architecture">Architecture</a>
  •
  <a href="#-pages--modules">Pages</a>
</p>

---

## ✨ Project Overview

**Thamarai Fertility & Women's Health Center** is a modern healthcare website redesign created for a fertility and women's health organization with multiple branches across Tamil Nadu.

The project combines:

* 🎨 Modern responsive frontend design
* 📱 Mobile-first user experience
* ✨ Smooth scroll animations
* 🧩 Reusable UI components
* 🔌 REST API integration
* 👨‍⚕️ Dynamic doctor profiles
* 📝 Dynamic healthcare blogs
* ❓ API-powered FAQs
* 🧮 Interactive health calculators
* 📅 Appointment/contact workflows
* 💬 WhatsApp and call-to-action integrations
* 🔍 SEO-friendly structure
* ⚡ Fast and lightweight static frontend

The local version modernizes and consolidates the content architecture of the original WordPress website into a streamlined frontend + backend application.

---

# 🌐 Live Website

<p align="center">

### 🏥 Thamarai Fertility & Women's Health Center

<a href="https://thamaraihealthcare.com/">
  <img src="https://img.shields.io/badge/Visit%20Live%20Website-thamaraihealthcare.com-0ea5a4?style=for-the-badge&logo=googlechrome&logoColor=white" />
</a>

</p>

> **Note:** The live production website and this local development project represent two different implementations of the same healthcare platform.

---

# 🎯 Project Goals

The redesign focuses on transforming a traditional healthcare website into a more engaging digital experience.

### Primary objectives

* Improve navigation and discoverability
* Present healthcare services clearly
* Create a professional medical brand experience
* Improve mobile responsiveness
* Introduce interactive healthcare tools
* Create reusable frontend sections
* Connect frontend pages with backend APIs
* Provide dynamic doctor and blog content
* Improve accessibility and usability
* Build a scalable foundation for future features

---

# 💎 Frontend Experience

The website is designed around a **premium healthcare UI experience**.

### 🎨 Visual Design

* Clean medical aesthetic
* Modern card-based layouts
* Gradient backgrounds
* Rounded UI components
* Responsive typography
* Consistent spacing system
* Professional CTA sections
* Interactive hover states
* Glass-style visual elements
* Image overlays
* Animated statistics

### ⚡ Motion & Interaction

Powered by **AOS**, Bootstrap animations and custom JavaScript.

```text
Scroll
   ↓
Section enters viewport
   ↓
AOS animation triggered
   ↓
Cards / statistics / content reveal
   ↓
Interactive hover states
   ↓
Smooth user journey
```

### 📱 Responsive Experience

Designed for:

```text
📱 Mobile
   ↓
📲 Tablet
   ↓
💻 Laptop
   ↓
🖥️ Desktop
```

The navigation, cards, forms, galleries and calculators adapt to different screen sizes.

---

# 🚀 Key Features

## 🏠 Interactive Homepage

The homepage acts as the central healthcare experience.

### Hero Carousel

Four primary promotional slides:

* Creating families over three decades
* A baby for every couple
* Landmark ICSI achievement
* Advanced Y chromosome micro-deletion detection

Each slide includes an appropriate CTA.

---

## 🏥 Healthcare Services

The platform organizes healthcare services into dedicated categories.

### Fertility

* Fertility evaluation
* IUI
* IVF
* ICSI
* Egg donation
* Assisted reproduction

### Andrology

* Semen analysis
* Sperm DNA fragmentation
* Y chromosome testing
* Karyotyping

### Genetics

* Genetic counselling
* PGD
* Chromosomal analysis
* Carrier screening

### Women's Health

* Gynecology
* Menopause
* Adolescence
* Obesity
* Cancer screening
* Special clinics

### Pregnancy Care

* Fetal medicine
* High-risk pregnancy care
* Antenatal care
* Postnatal care
* Pregnancy assessment

### Neonatal & Pediatric Care

* NICU services
* Neonatology
* Pediatric care

---

# 👨‍⚕️ Doctor Directory

The **Our Doctors** module presents medical professionals through interactive profile cards.

Each doctor profile can include:

```text
Doctor Name
      ↓
Specialization
      ↓
Qualifications
      ↓
Experience
      ↓
Branch
      ↓
Availability
      ↓
Consultation Fee
      ↓
Awards & Achievements
```

### Dynamic Doctor Details

Doctor information is loaded using:

```http
GET /api/public/doctors/:id
```

Example:

```text
doctor-details.html?doc=uthraraj
```

Supported profiles include:

* Dr. P. Uthraraj
* Dr. C.V. Kannaki Uthraraj
* Dr. Nachappa Sivanesan Uthraraj
* Dr. Mangayarkarasi
* Dr. Devdas Madhavan
* Dr. Barani Kumar

---

# 💬 Success Stories

Dedicated testimonial sections provide a human-centered presentation of patient experiences.

Example categories:

* IVF Success
* ICSI Treatment
* IUI Success

The UI uses:

* Testimonial cards
* Profile imagery
* Quote layouts
* CTA sections
* Responsive carousel-style presentation

---

# 🖼️ Interactive Gallery

The gallery module provides a visual representation of the healthcare environment.

### Features

* Responsive image grid
* Hover animations
* Image overlays
* Caption display
* Virtual laboratory tour section
* Branch-based gallery navigation

---

# 🏆 Achievements

The achievements section uses animated counters and feature cards.

### Highlight Statistics

```text
15,000+
IUI Success

5,524+
IVF Success

7
Branches

21+
Consultants
```

### Achievement Categories

* Landmark reproductive medicine achievements
* ISO & NABH certification
* Advanced diagnostics
* Difficult-case fertility care
* Genetic testing

---

# 📅 Events & Workshops

The events section showcases institutional activities.

### Included Events

* ISO Function
* IUI Workshop
* Bangkok Conference
* Rally for the Girl Child

The card-based layout provides:

```text
Event Image
     ↓
Event Category
     ↓
Event Title
     ↓
Description
     ↓
Event Details
```

---

# 📝 Dynamic Healthcare Blog

The blog system is API-driven.

### Blog Listing

```http
GET /api/blogs/public
```

Supports:

* Blog listing
* Pagination
* Categories
* Recent posts
* Related content
* Sidebar navigation

### Blog Details

```http
GET /api/blogs/public/:slug
```

Includes:

* Full article
* Related posts
* Social sharing
* Comments
* Dynamic content

### Comment API

```http
POST /api/blogs/public/:id/comment
```

---

# ❓ Dynamic FAQ System

The FAQ module retrieves healthcare questions dynamically from the backend.

```http
GET /api/faqs/public
```

Category filtering:

```http
GET /api/faqs/public?category=X
```

### Frontend Features

* Category filters
* Accordion UI
* Dynamic content loading
* Responsive layout
* FAQ structured data

---

# 🧮 Interactive Health Calculators

One of the key frontend features is the interactive calculator suite.

## IVF Success Calculator

Inputs include:

* Age
* Weight
* Infertility duration
* Previous attempts

---

## Ovulation Calculator

Uses:

* Last menstrual period
* Cycle length

---

## Due Date Calculator

Supports:

* LMP-based calculation
* Conception-date calculation

---

## BMI Calculator

Calculates:

```text
BMI = Weight / Height²
```

and displays the corresponding BMI category.

---

## Fertility Assessment Quiz

A short interactive assessment based on four questions.

The UI dynamically calculates an indicative score.

> ⚠️ These calculators are intended as informational tools and should not replace professional medical advice.

---

# 📅 Appointment System

The appointment interface provides a dedicated patient enquiry workflow.

### Form Fields

```text
Name
Doctor
Email
Phone
Preferred Date
Subject
Message
```

Submitted data is sent to:

```http
POST /api/contact
```

---

# 📍 Multi-Branch Support

The platform represents multiple healthcare locations.

### Branches

| Branch        | Location               |
| ------------- | ---------------------- |
| Coimbatore-I  | Peelamedu              |
| Coimbatore-II | KMCH                   |
| Chennai       | Fertility Solutions    |
| Salem         | Devi Hospital          |
| Tirupur       | Ganapathy Nursing Home |
| Pollachi      | Women's Health Center  |

---

# 📞 Floating Action System

Persistent action buttons are available across the website.

```text
        ┌───────────────┐
        │ 💬 WhatsApp   │
        ├───────────────┤
        │ 📞 Call Now   │
        ├───────────────┤
        │ 📅 Appointment│
        └───────────────┘
```

These improve access to high-priority healthcare actions.

---

# 🧭 Navigation Architecture

The website uses a multi-level navigation system.

```text
Home
│
├── Profile
│   ├── Our Doctors
│   ├── About Us
│   ├── Testimonials
│   ├── Virtual Lab Tour
│   ├── Academics
│   └── Research
│
├── Fertility
│   ├── Fertility Basics
│   └── Disorders of Fertility
│
├── Tests
│   ├── Tests for Ovulation
│   ├── Tests for Sperm
│   ├── Tests for Tubes & Uterus
│   └── Tests for Pelvis
│
├── Procedures
│   ├── IUI
│   ├── IVF
│   ├── ICSI
│   ├── Embryo Transfer
│   ├── Embryo Freezing
│   ├── PGD
│   └── Donation
│
├── Clinics
│   ├── Obstetrics
│   ├── Gynecology
│   ├── Fetal Medicine
│   ├── Genetic Clinic
│   └── Special Clinics
│
├── Gallery
├── Events
├── Blog
└── Contact
```

---

# 🧱 Page Architecture

The local frontend contains approximately 15 primary HTML pages.

| Page                   | Purpose                  |
| ---------------------- | ------------------------ |
| `index.html`           | Homepage                 |
| `about.html`           | Organization information |
| `services.html`        | Healthcare services      |
| `our-doctors.html`     | Doctor directory         |
| `doctor-details.html`  | Dynamic doctor profile   |
| `success-stories.html` | Patient testimonials     |
| `gallery.html`         | Gallery & virtual tour   |
| `achievements.html`    | Achievements             |
| `events.html`          | Events & workshops       |
| `blog.html`            | Blog listing             |
| `blog-details.html`    | Dynamic blog             |
| `faq.html`             | Dynamic FAQs             |
| `calculators.html`     | Interactive calculators  |
| `contact.html`         | Contact & appointments   |
| `robots.txt`           | Search engine rules      |
| `sitemap.xml`          | SEO sitemap              |

---

# 🏗️ Project Architecture

```text
THAMARAI-HEALTHCARE/
│
├── frontend/
│   │
│   ├── index.html
│   ├── about.html
│   ├── services.html
│   ├── our-doctors.html
│   ├── doctor-details.html
│   ├── success-stories.html
│   ├── gallery.html
│   ├── achievements.html
│   ├── events.html
│   ├── blog.html
│   ├── blog-details.html
│   ├── faq.html
│   ├── calculators.html
│   └── contact.html
│
├── assets/
│   ├── css/
│   ├── js/
│   ├── images/
│   ├── icons/
│   └── fonts/
│
├── backend/
│   ├── routes/
│   ├── controllers/
│   ├── models/
│   ├── middleware/
│   └── server.js
│
├── robots.txt
├── sitemap.xml
└── README.md
```

---

# 🔌 REST API Architecture

The backend follows an API-driven architecture.

```text
                FRONTEND
                    │
                    ▼
             HTTP / AJAX
                    │
                    ▼
             EXPRESS SERVER
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
      Doctors      Blogs       FAQs
        │           │           │
        └───────────┼───────────┘
                    ▼
               DATA LAYER
```

### Public API Endpoints

| Endpoint                        | Method | Purpose         |
| ------------------------------- | -----: | --------------- |
| `/api/faqs/public`              |    GET | Retrieve FAQs   |
| `/api/faqs/public?category=X`   |    GET | Filter FAQs     |
| `/api/blogs/public`             |    GET | Retrieve blogs  |
| `/api/blogs/public/:slug`       |    GET | Retrieve blog   |
| `/api/blogs/public/:id/comment` |   POST | Submit comment  |
| `/api/public/doctors/:id`       |    GET | Retrieve doctor |
| `/api/contact`                  |   POST | Submit enquiry  |

---

# 🛠️ Technology Stack

## Frontend

| Technology         | Purpose                     |
| ------------------ | --------------------------- |
| HTML5              | Semantic page structure     |
| CSS3               | Custom visual styling       |
| JavaScript         | Interactivity               |
| Bootstrap 5.3.2    | Responsive UI               |
| Bootstrap Icons    | Interface icons             |
| Font Awesome 6.5.1 | Social icons                |
| AOS 2.3.1          | Scroll animations           |
| OwlCarousel 2.3.4  | Content carousel            |
| jQuery 3.7.1       | DOM & interaction utilities |

## Backend

| Technology   | Purpose                        |
| ------------ | ------------------------------ |
| Node.js      | Runtime                        |
| Express.js   | REST API                       |
| REST APIs    | Frontend/backend communication |
| AJAX / Fetch | Dynamic data loading           |

## Design

```text
Inter
Poppins
Bootstrap Grid
Responsive Cards
CSS Animations
AOS
Carousel Components
```

---

# 🎨 UI Components

The project contains reusable visual patterns such as:

### Navbar

* Multi-level dropdowns
* Responsive mobile menu
* CTA buttons
* Social links

### Hero

* Full-width carousel
* Background imagery
* Animated content
* Primary CTAs

### Cards

* Doctor cards
* Service cards
* Blog cards
* Event cards
* Achievement cards
* Testimonial cards

### Forms

* Appointment form
* Contact form
* Blog comments
* Calculator inputs

### Feedback

* Toasts
* Alerts
* Loading states
* Empty states
* Error messages

---

# 📱 Responsive Design

The frontend follows a mobile-first approach.

```text
              Responsive UI
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
     Mobile       Tablet       Desktop
       │            │            │
       ▼            ▼            ▼
    1 Column     2 Columns    Multi Column
```

Special attention is given to:

* Navigation
* Hero sections
* Forms
* Doctor cards
* Service cards
* Gallery
* Calculators
* Footer
* Floating action buttons

---

# 🔍 SEO Features

The project includes foundational SEO support.

### Included

* Semantic HTML
* Page titles
* Meta descriptions
* `robots.txt`
* `sitemap.xml`
* FAQ structured data
* Clean navigation hierarchy
* Descriptive content sections
* Responsive design

---

# 🔐 Authentication & External Portals

The website provides separate access links for:

* 👨‍💼 Staff Login
* 👩‍⚕️ Patient Login

The local development architecture can connect these portals through external services such as **ngrok** during development.

---

# 🔗 External Integrations

| Service          | Usage                 |
| ---------------- | --------------------- |
| Bootstrap        | UI framework          |
| Bootstrap Icons  | UI icons              |
| Font Awesome     | Social icons          |
| AOS              | Scroll animations     |
| OwlCarousel      | Carousels             |
| Google Fonts     | Typography            |
| jQuery           | Frontend utilities    |
| WhatsApp         | Patient communication |
| Social Platforms | Brand presence        |
| ngrok            | Development tunnel    |

---

# 🆚 Original vs Modernized Architecture

| Area              | Original Website       | Local Redesign       |
| ----------------- | ---------------------- | -------------------- |
| CMS               | WordPress              | Static HTML + API    |
| Theme             | Custom WordPress Theme | Custom Bootstrap UI  |
| Slider            | LayerSlider            | Bootstrap Carousel   |
| Menu              | Plugin-based           | Bootstrap Navbar     |
| Forms             | Contact Form 7         | AJAX/API             |
| Animations        | jQuery                 | AOS + CSS            |
| Content           | Many WordPress pages   | Consolidated modules |
| Data              | CMS-based              | REST API             |
| URL Structure     | Pretty URLs            | HTML pages           |
| Interactive Tools | Limited                | Calculator suite     |

---

# 🧠 Engineering Highlights

This project demonstrates practical implementation of:

* Responsive frontend development
* Component-oriented UI thinking
* REST API integration
* Dynamic rendering
* Query-string based routing
* Form handling
* Client-side validation
* Animation integration
* Healthcare UX
* SEO fundamentals
* Multi-level navigation
* Interactive calculators
* Dynamic filtering
* Pagination
* Social sharing
* Mobile-first design

---

# 📊 Project Scale

```text
                 THAMARAI
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
     FRONTEND     BACKEND     CONTENT
        │           │           │
      ~15 HTML    REST API     50+ legacy
       Pages      Services     pages
        │           │           │
        └───────────┼───────────┘
                    ▼
            Healthcare Platform
```

---

# 🚀 Local Development

### 1. Clone Repository

```bash
git clone https://github.com/kala3013/thamarai-healthcare.git
```

### 2. Navigate to Project

```bash
cd thamarai-healthcare
```

### 3. Frontend

The static frontend can be opened using:

```text
index.html
```

For a better development experience, use VS Code Live Server.

### 4. Backend

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

or:

```bash
node server.js
```

---

# 🧪 Development Environment

The original local project was developed using:

```text
Windows
XAMPP
VS Code
Node.js
Express.js
Browser DevTools
Git
GitHub
```

Local project path:

```text
C:\xampp\htdocs\thamarai-healthcare
```

---

# 📁 Recommended Repository Structure

```text
thamarai-healthcare/
│
├── index.html
├── about.html
├── services.html
├── our-doctors.html
├── doctor-details.html
├── success-stories.html
├── gallery.html
├── achievements.html
├── events.html
├── blog.html
├── blog-details.html
├── faq.html
├── calculators.html
├── contact.html
│
├── css/
│   ├── style.css
│   ├── responsive.css
│   └── animations.css
│
├── js/
│   ├── main.js
│   ├── doctors.js
│   ├── blogs.js
│   ├── faq.js
│   ├── calculators.js
│   └── contact.js
│
├── images/
│   ├── doctors/
│   ├── services/
│   ├── gallery/
│   ├── events/
│   └── testimonials/
│
├── backend/
│   ├── server.js
│   ├── routes/
│   ├── controllers/
│   └── models/
│
├── robots.txt
├── sitemap.xml
└── README.md
```

---

# 📸 UI Showcase

> Add screenshots/GIFs of your redesigned interface here to make the repository visually stronger.

### 🏠 Homepage

```text
[ Add homepage screenshot here ]
```

### 👨‍⚕️ Doctors

```text
[ Add doctors page screenshot here ]
```

### 🏥 Services

```text
[ Add services page screenshot here ]
```

### 🧮 Health Calculators

```text
[ Add calculators screenshot here ]
```

### 📱 Mobile Experience

```text
[ Add mobile screenshots here ]
```

---

# 🎬 Recommended GitHub Demo

For a more impressive repository presentation, add a short GIF/video showing:

```text
Homepage
   ↓
Animated Hero
   ↓
Services
   ↓
Doctor Directory
   ↓
Doctor Details
   ↓
Gallery
   ↓
Blog
   ↓
FAQ
   ↓
Health Calculator
   ↓
Appointment Form
```

---

# 🔮 Future Enhancements

Planned improvements can include:

* 🔐 Patient authentication
* 👨‍⚕️ Doctor dashboard
* 📅 Real-time appointment scheduling
* 🗓️ Doctor availability calendar
* 💳 Online consultation/payment
* 🧾 Digital prescription system
* 📊 Patient dashboard
* 🔔 Appointment notifications
* 🌐 Tamil/English multilingual support
* 🤖 AI healthcare FAQ assistant
* 📱 Progressive Web App
* 🔍 Advanced search
* 🗺️ Interactive branch locator
* ☁️ Cloud deployment
* 🐳 Dockerized backend
* 🔄 CI/CD pipeline

---

# 🧑‍💻 Developer

<p align="center">

### Kalanidhi M C

**Computer Science Engineering Student | Full Stack Developer | Cloud & DevOps Enthusiast**

</p>

<p align="center">

<a href="https://github.com/kala3013">
<img src="https://img.shields.io/badge/GitHub-kala3013-181717?style=for-the-badge&logo=github" />
</a>

</p>

---

# 📫 Connect

<p align="center">

<a href="mailto:kalanidhimurugan@gmail.com">
<img src="https://img.shields.io/badge/Email-kalanidhimurugan%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" />
</a>

<a href="https://github.com/kala3013">
<img src="https://img.shields.io/badge/GitHub-kala3013-181717?style=for-the-badge&logo=github&logoColor=white" />
</a>

</p>

---

# ⭐ Why This Project Matters

This project goes beyond a traditional static healthcare website.

It demonstrates how a legacy content-heavy healthcare platform can be transformed into a **modern, responsive and API-driven digital experience** while maintaining a strong focus on:

```text
                USER EXPERIENCE
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       DESIGN       CONTENT       FUNCTION
          │            │            │
          ▼            ▼            ▼
      Responsive    Healthcare     APIs
       UI/UX        Content      Calculators
          │            │            │
          └────────────┼────────────┘
                       ▼
              MODERN WEB PLATFORM
```

---

## 🏥 Healthcare Website

**Thamarai Fertility & Women's Health Center**

📍 Coimbatore, Tamil Nadu, India

🌐 **Live Website:**
https://thamaraihealthcare.com/

---

<p align="center">

### ⭐ If you find this project interesting, consider starring the repository!

**Built with ❤️ using modern web technologies**

</p>
