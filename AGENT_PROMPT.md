# 🧠 AGENT PROMPT: 02_FRANKBASE.COM

You are operating on **FrankBase Main Hub (`https://frankbase.com`)**, the flagship Knowledge & Education Portal of the FrankBase Digital Ecosystem.

### 🌐 Brand Core & Scope:
- **Canonical URL:** `https://frankbase.com`
- **Role:** Main Hindi-Medium & Bihar Board (10th/12th, BPSC TRE, STET, MCQs, Study Notes, Digital Skills).
- **Primary Support Email:** `support@frankbase.com` $\rightarrow$ `mastermanikant.in@gmail.com`
- **Umbrella Legal Email:** `legal@frankbase.com` $\rightarrow$ `mastermanikant.in@gmail.com`
- **System No-Reply:** `noreply@frankbase.com` (Automated System Receipts & Downloads)

### 🛡️ Auth & UX Strategy:
- **Public Use (Zero Friction):** All educational notes, formulas, syllabus breakdowns, and blogs are 100% free and open without login.
- **Progressive Google Login (Only):** Required only when a student wants to leave a comment, upvote a study note, or bookmark chapters to their personal dashboard.
- **Contact Form Target:** `POST https://mmcentral.pages.dev/api/submit-lead` (with `tenant_id: "frankbase_hub"`, `source_domain: "frankbase.com"`).
