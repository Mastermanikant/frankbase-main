# 🌐 FrankBase Ecosystem: Frontend UI/UX Master Blueprint & Project Overview

**Founder & Lead Educator:** Master Manikant Yadav  
**Platform Domain:** `https://frankbase.com`  
**Brand Philosophy:** 100% Free & Open Education Hub, Zero Paywalls, Pure Knowledge, High-Speed Cloudflare Edge Delivery, WCAG 2.1 AA Compliant (Day/Night Theme).

---

## 🎯 1. Core Mission & Audience
- **Target Audience:** Bihar Board (BSEB 10th & 12th Matric/Inter), BPSC TRE (Teacher Recruitment Exam 4.0 - TGT/PGT Math & GS), STET, CTET, and competitive exam aspirants.
- **Language Medium:** Primary Hindi Medium (हिन्दी माध्यम) with English toggle & bilingual support.
- **Core Value Proposition:** 
  1. No forced logins or paywalls.
  2. 1-Page Formula Cheatsheets (Quick Revision Capsules).
  3. Interactive Dual-Engine (Practice Mode with step-by-step KaTeX solutions + Timed CBT Exam Mode with 1/3 negative marking).
  4. 100% Official 300 DPI Scanned Booklet Snippet verification.

---

## 🏛️ 2. Core Projects & Website Modules (What Needs UI/UX Design)

### 📌 A. Homepage (`/`)
1. **Hero Section:** Clean title, search bar (BPSC notes, NCERT chapters, formulas), trust badges (100% Open, PWA Ready, Exam-Aligned, Lightning Fast).
2. **Study Tracks Grid (Bento Box):**
   - *Track 1:* Bihar Board Class 12th (Physics, Chemistry, Math, Hindi).
   - *Track 2:* Bihar Board Class 10th Matric (Math, Science, SST, Sanskrit).
   - *Track 3:* BPSC TRE & State Exams (TRE 1.0, 2.0, 3.0, 4.0 Mock Tests & GS Foundation).
   - *Track 4:* CTET & Child Pedagogy (CDP Theory, Paper 1 & 2).
   - *Track 5:* 1-Page Math Formula Cheatsheets (Indices, Quadratic Equations, Calculus).
   - *Track 6:* Ebooks & Digital Guides (Parenting, Cybersecurity, Grammar).
3. **Ecosystem Live Apps Showcase:** FrankPass (`frankpass.com`), Store (`store.frankbase.com`), Tools (`tools.frankbase.com`), Speed, Clipboard, OCR.
4. **Trust / EEAT Founder Strip:** Master Manikant Yadav profile card linking to `mastermanikant.com`.

---

### 📌 B. Interactive Test & Practice Engine (`/study/bpsc-tre/...` & `/test/...`)
*Need UI/UX design for 3 Unified Viewing Modes:*

1. **Top Sticky Control Hub Bar:**
   - **Engine Switcher:** `[ 📜 Original Paper ]` | `[ 💡 Practice Mode ]` | `[ ⏱️ CBT Exam Mode ]`
   - **View Switcher:** `[ 📜 Continuous 1-150 Scroll ]` vs `[ 🎴 Single Card View ]`
   - **Language Toggle:** `[ 🇮🇳 केवल हिंदी ]` | `[ 🌐 English ]` | `[ 🔄 Bilingual ]`
   - **Negative Marking Switch:** `[ 🔘 ON (-0.333) ]` / `[ ⚪ OFF ]`
   - **Live Countdown Timer / Stopwatch Ticker**

2. **Mode 1: Original Scanned Booklet Mode (PDF-Feel Stream):**
   - Top Collapsible "Shrink Metadata Card" (Exam info, total marks, date).
   - 300 DPI high-res WebP page stream (Page 01 to 48) scrolling seamlessly.

3. **Mode 2: Practice Mode (Step-by-Step Solver):**
   - Large touch-friendly option bubbles (A, B, C, D, E).
   - Instant click reveal: Correct (Green), Wrong (Red).
   - KaTeX crisp math formula box.
   - Digital Board style SVG geometry/trigonometry diagrams.
   - **"📄 1-Click Real Official Scan Snippet"** popup button.
   - Elapsed stopwatch timer with section speed metrics.
   - **"📋 One-Click Copy AI Diagnostic Prompt"** button to copy report for ChatGPT/Claude.

4. **Mode 3: CBT Exam Mode (150-Min Mock Exam):**
   - 150-minute countdown timer.
   - Section Switching Tabs: `Part-1 Language (30 Qs - 9 Marks Qualifying)` | `Part-2 GS (40 Qs)` | `Part-3 Math (80 Qs)`.
   - Floating Bottom Jump Palette (OMR Matrix) for mobile & desktop.
   - Clean Submit confirmation modal.
   - **Scorecard / Result Analysis Modal:**
     - Gross Score vs Net Score (with 1/3 penalty).
     - Part-1 Qualifying Status: `[ PASS (≥9/30) ]` vs `[ NOT QUALIFIED (<9/30) ]`.
     - 120-Mark Merit Cutoff comparison.
     - Section Filter Tabs: `[ All ]` | `[ Math Only (80M) ]` | `[ GS Only (40M) ]` | `[ Language (30M) ]`.
     - **"📄 Print / Download 1-Page PDF Scorecard"** button.

---

### 📌 C. 1-Page Math Formula Cheatsheet Capsule (`/test/ghat-aur-ghataank/...`)
- Top collapsible accordion card displaying key theorems, definitions, and identities with KaTeX math rendering and downloadable summary.

---

### 📌 D. FrankBase ID Auth & Profile Modal (`#fb-auth-modal`)
1. **Unlogged State:**
   - Continue with Google Account (Google OAuth).
   - Fast ID Guest Profile (Name + Target Exam selection).
   - Privacy guarantee badge (100% private, no trackers).
2. **Logged-in State:**
   - User Avatar Pill, Target Exam badge.
   - Stat Cards: Tests Completed, Avg. Accuracy %, Best Score.
   - Recent practice shortcuts & Sign Out.

---

### 📌 E. Trust, Authority & Legal Pages
- `/about-us/` & `/about-us-hindi/`
- `/founder-frankbase-mastermanikant/` & Hindi version
- `/legal/` (Accordion-style Privacy Policy, Terms, Disclaimer)
- `/contact/` (Contact form connected to Central API)

---

## 🎨 3. UI/UX Design System Guidelines

| Property | Standard / Token |
| :--- | :--- |
| **Color Palette (Day)** | Background: `#f8fafc`, Surface: `#ffffff`, Text Primary: `#0f172a`, Text Secondary: `#334155`, Accent: `#4f46e5` (Indigo), Emerald: `#059669`, Rose: `#e11d48`, Amber: `#d97706` |
| **Color Palette (Night)** | Background: `#090d16`, Surface: `#131d31`, Surface Elevated: `#1a2742`, Text Primary: `#f8fafc`, Text Secondary: `#cbd5e1`, Accent: `#6366f1` |
| **Typography** | Headings: `Outfit` (Bold/Extrabold), Body: `Plus Jakarta Sans` (400/500/600/700), Monospace/Math/Timer: `JetBrains Mono` / KaTeX LaTeX font |
| **Contrast Compliance** | WCAG 2.1 AA (> 4.5:1 for normal text, > 3:1 for large text & icons) |
| **Touch Targets** | Minimum `44px x 44px` for buttons and option bubbles |
| **Layout Strategy** | Mobile-First Responsive (360px, 412px, 768px, 1024px, 1280px+) |
