# 🌿 Thamarai Healthcare - Complete Healthcare Management System

A **production-ready** Healthcare Management System and Fertility & Women's Health Center Website built with modern web technologies.

## 🚀 Technology Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript |
| **Backend** | Node.js, Express.js |
| **Database** | MySQL |
| **Auth** | JWT, bcrypt |
| **Security** | Helmet, CORS, Rate Limiting |
| **Icons** | Bootstrap Icons |
| **Animations** | AOS (Animate On Scroll) |
| **File Upload** | Multer |
| **Email** | Nodemailer |

## 📋 Complete System Overview

### 1️⃣ Public Website
| Page | URL | Description |
|------|-----|-------------|
| Home | `index.html` | Hero, services, branches, counters, doctors, appointment form |
| About | `about.html` | Company history, mission, team |
| Services | `services.html` | All medical services with icons and descriptions |
| Doctors | `our-doctors.html` | Doctor profiles with specialties |
| Gallery | `gallery.html` | Hospital and facility photos |
| Achievements | `achievements.html` | Milestones, awards, animated counters |
| Events | `events.html` | Hospital events and news |
| Blog | `blog.html` | Health articles with categories, search, pagination |
| Blog Details | `blog-details.html` | Single article with comments & sharing |
| FAQ | `faq.html` | Categorized accordion FAQ with Schema markup |
| Success Stories | `success-stories.html` | Patient testimonials and video stories |
| Calculators | `calculators.html` | IVF, Ovulation, Due Date, BMI, Fertility Quiz |
| Contact | `contact.html` | Address, map, contact form, appointment booking |

### 2️⃣ Patient Portal (`/frontend/patient/`)
| Page | Description |
|------|-------------|
| Register | Patient registration with validation |
| Login | JWT-based authentication |
| Dashboard | Appointments, reports, profile overview |
| Profile | View and update personal information |
| Appointments | Book, view, and manage appointments |
| Reports | View and download medical reports |

### 3️⃣ Staff Portal (`/frontend/staff/`)
| Page | Description |
|------|-------------|
| Login | Staff authentication |
| Dashboard | Overview with stats |
| Patients | Search, add, edit, delete patients |
| Appointments | Manage patient appointments |
| Reports | Upload patient reports |
| Doctors | View doctor schedules |

### 4️⃣ Admin Portal (`/frontend/admin/`)
| Page | Description |
|------|-------------|
| Login | Admin authentication |
| Dashboard | Analytics with Chart.js |
| Patients | Full patient management |
| Appointments | All appointments CRUD |
| Doctors | Doctor management |
| Analytics | Charts for patients, appointments, branches |
| Staff | Staff user management |
| Blogs | Blog CRUD with comments moderation |
| Branches | Branch location management |
| Testimonials | Patient success stories management |
| Settings | Site settings configuration |

### 5️⃣ Backend API
| Endpoint | Description |
|----------|-------------|
| `/api/auth` | Register, Login (Patient, Staff, Admin) |
| `/api/patient` | Patient profile and data |
| `/api/appointments` | Appointment CRUD |
| `/api/reports` | Medical report upload/download |
| `/api/staff` | Staff patient management |
| `/api/doctors` | Doctor management |
| `/api/admin` | Admin dashboards and staff mgmt |
| `/api/blogs` | Blog CRUD and public endpoints |
| `/api/branches` | Branch CRUD |
| `/api/testimonials` | Testimonial CRUD |
| `/api/faqs` | FAQ management |
| `/api/services` | Services listing |
| `/api/contact` | Contact form submissions |
| `/api/notifications` | User notifications |
| `/api/public` | Public doctors list and site settings |
| `/api/upload` | File upload endpoint |

### 6️⃣ Database Tables
`patients`, `staff`, `doctors`, `appointments`, `reports`, `branches`, `blogs`, `blog_comments`, `testimonials`, `notifications`, `gallery`, `contact_messages`, `services`, `faq`, `site_settings`

### 7️⃣ Special Features
- ✅ **Floating Action Buttons** - WhatsApp, Call, Book Appointment
- ✅ **SEO Optimized** - Meta tags, Open Graph, Twitter Cards, Schema markup
- ✅ **Sitemap** - `sitemap.xml` for search engines
- ✅ **Robots.txt** - Search engine crawling rules
- ✅ **Responsive Design** - Desktop to mobile
- ✅ **Accessibility** - ARIA labels, semantic HTML
- ✅ **Healthcare Calculators** - IVF, Ovulation, Due Date, BMI, Fertility Quiz
- ✅ **Email Notifications** - Appointment booking, approval, rescheduling
- ✅ **Role-Based Access** - Patient, Staff, Admin
- ✅ **Animated Counters** - Achievements and milestones
- ✅ **Blog Comments** - User comments with moderation
- ✅ **FAQ Schema** - Structured data for search engines

## 🛠️ Quick Setup

### Prerequisites
- Node.js (v14+)
- MySQL
- npm

### Backend Setup
```bash
cd backend
cp .env.example .env   # Edit with your database credentials
npm install
# Import database
mysql -u root -p < ../database/healthcare-updated.sql
npm run dev
```

### Frontend
Simply serve the root directory with any static server:
```bash
# Using Python
python -m http.server 8000

# Or using npx
npx serve .
```

## 🌐 Deployment

### Vercel (Frontend)
1. Push to GitHub
2. Import project in Vercel
3. Set build command: None (static)
4. Set output directory: root

### Render / Railway (Backend)
1. Set build command: `cd backend && npm install`
2. Set start command: `cd backend && node server.js`
3. Set environment variables from `.env`

## 📂 Project Structure
```
thamarai-healthcare/
├── index.html, about.html, services.html, ...
├── blog.html, faq.html, calculators.html, ...
├── robots.txt, sitemap.xml
├── assets/
│   ├── css/style.css
│   ├── js/script.js
│   └── images/
├── backend/
│   ├── server.js
│   ├── config/db.js
│   ├── controllers/
│   ├── routes/
│   └── middleware/
├── database/
│   ├── healthcare.sql
│   └── healthcare-updated.sql
├── frontend/
│   ├── patient/ (register, login, dashboard, etc.)
│   ├── staff/ (login, dashboard, patients, etc.)
│   └── admin/ (dashboard, analytics, blogs, etc.)
└── README.md
```

## 🔒 Security Features
- JWT Authentication with token expiration
- bcrypt password hashing
- Helmet security headers
- CORS configuration
- Rate limiting on API routes
- Input validation on all endpoints
- Role-based access control
- File upload size limits

