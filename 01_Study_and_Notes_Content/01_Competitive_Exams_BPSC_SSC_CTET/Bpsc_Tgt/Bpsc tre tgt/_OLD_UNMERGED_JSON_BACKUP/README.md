# ⚠️ OLD UNMERGED JSON BACKUP — KNOWN ISSUES & AUDIT LOG

## 📅 Snapshot Timestamp: 2026-08-21 | 13:00 IST
## 📂 Location: `D:\01_Websites_and_Content\MMY_Website_Project\02_frankbase.com\01_Study_and_Notes_Content\01_Competitive_Exams_BPSC_SSC_CTET\Bpsc_Tgt\Bpsc tre tgt\_OLD_UNMERGED_JSON_BACKUP`

---

## 🔍 Why These JSON Files Are Being Replaced (The 3 Core Issues):

1. **❌ Hindi & English Split Duplication:**
   - Instead of combining the Hindi and English versions of Question #1 into a single structured object (`hindi_text` + `english_text`), the old converter generated two separate objects (one in English, one in Hindi).
   - This inflated 120-question papers to 240 entries, and 150-question papers to 300 entries.

2. **❌ Missing Bilingual Option Keys:**
   - The options dictionary contained only one language per object instead of clean bilingual pairs (`options: { "A": { "hi": "...", "en": "..." } }`).

3. **❌ Missing Full-Page WebP Manifest Reference:**
   - These old files do not contain references to the high-resolution scanned `.webp` pages of the original exam question booklet.

---

## 🗑️ Deletion Safety Status:
Once the new, accurate, merged JSON files and WebP page exports are generated and verified on FrankBase, **this entire folder can be safely deleted without any data loss.**
