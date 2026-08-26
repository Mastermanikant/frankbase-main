---
title: "BPSC TGT Math: बहुपद एवं द्विघात समीकरण — शून्यक, शेषफल प्रमेय, श्रीधराचार्य सूत्र (8.3% Weightage)"
slug: bpsc-tgt-math-algebra-polynomials-quadratic-equations
description: "BPSC TGT Math Algebra — 46 प्रश्न (8.3%)। शून्यक, शेषफल प्रमेय, गुणनखंड प्रमेय, द्विघात सूत्र, विविक्तकर (D) और बीजगणितीय सर्वसमिकाएँ।"
date: 2026-08-21
series: "BPSC TGT Math Master Series"
article_no: 5
prev_article: "Article 04 — वाणिज्यिक अंकगणित Masterclass"
next_article: "Article 06 — त्रिकोणमिति एवं ऊँचाई-दूरी Masterclass"
robots: "noindex, follow"
lang: hi
---

# BPSC TGT Math: बहुपद एवं द्विघात समीकरण
## शून्यक, शेषफल प्रमेय, श्रीधराचार्य सूत्र (8.3% Weightage)

> [!IMPORTANT]
> **Executive Summary:** BPSC TRE 1.0/2.0/3.0 में बहुपद (Polynomials) और द्विघात समीकरण (Quadratic Equations) से कुल **46 प्रश्न (8.3%)** आए हैं। यह टॉपिक पूरी तरह **NCERT Class 9 Ch 2 और Class 10 Ch 2 व Ch 4** पर आधारित है। शेषफल प्रमेय (Remainder Theorem), गुणनखंड प्रमेय (Factor Theorem) और श्रीधराचार्य सूत्र (Quadratic Formula) — ये तीन सबसे ज़्यादा प्रश्न देने वाले उपटॉपिक हैं।

---

## 1. फॉर्मूला रेफरेंस टेबल (Formula Reference Table)

### द्विघात समीकरण के मूलों के सूत्र (Quadratic Equation — Roots & Coefficients)

द्विघात समीकरण: **ax² + bx + c = 0** (जहाँ a ≠ 0), मूल α (alpha) और β (beta)

| सूत्र | गणितीय रूप | याद करने की युक्ति |
|---|---|---|
| मूलों का योग (Sum of Roots) | α + β = −b/a | "Negative b upon a" |
| मूलों का गुणनफल (Product of Roots) | αβ = c/a | "c upon a" |
| मूलों का अंतर (Difference) | α − β = √[(α+β)² − 4αβ] | D निकालकर |
| α² + β² | (α+β)² − 2αβ | BPSC का सबसे बड़ा ट्रैप |
| α³ + β³ | (α+β)³ − 3αβ(α+β) | घन सूत्र से |
| नया समीकरण बनाएँ | x² − (α+β)x + αβ = 0 | Sum और Product से |

### त्रिघात समीकरण के मूल (Cubic Equation — ax³ + bx² + cx + d = 0)

मूल α, β, γ (alpha, beta, gamma)

| सूत्र | गणितीय रूप |
|---|---|
| α + β + γ | = −b/a |
| αβ + βγ + γα | = c/a |
| αβγ | = −d/a |

### श्रीधराचार्य सूत्र (Quadratic Formula / Sridharacharya Formula)

```
        −b ± √(b² − 4ac)
x =    ─────────────────
               2a
```

- यह सूत्र **ax² + bx + c = 0** का सीधा हल देता है।
- **श्रीधराचार्य** भारतीय गणितज्ञ थे जिन्होंने इसे 9वीं शताब्दी में प्रतिपादित किया।

### विविक्तकर (Discriminant — D)

**D = b² − 4ac**

| D का मान | मूलों की प्रकृति | उदाहरण |
|---|---|---|
| D > 0 | दो अलग वास्तविक मूल (2 distinct real roots) | x² − 5x + 6 = 0 → D = 1 |
| D = 0 | दो बराबर वास्तविक मूल (equal/repeated roots) | x² − 2x + 1 = 0 → D = 0 |
| D < 0 | कोई वास्तविक मूल नहीं (no real roots) | x² + x + 1 = 0 → D = −3 |

### शेषफल प्रमेय (Remainder Theorem)

```
यदि बहुपद p(x) को (x − a) से विभाजित करें,
तो शेषफल = p(a)
```

**गुणनखंड प्रमेय (Factor Theorem):**
```
यदि p(a) = 0, तो (x − a), p(x) का गुणनखंड है।
```

### बीजगणितीय सर्वसमिकाएँ (Key Algebraic Identities)

| सर्वसमिका | विस्तृत रूप |
|---|---|
| (a + b + c)² | = a² + b² + c² + 2ab + 2bc + 2ca |
| a³ + b³ + c³ − 3abc | = (a + b + c)(a² + b² + c² − ab − bc − ca) |
| a³ + b³ | = (a + b)(a² − ab + b²) |
| a³ − b³ | = (a − b)(a² + ab + b²) |
| (a + b)³ | = a³ + 3a²b + 3ab² + b³ |
| (a − b)³ | = a³ − 3a²b + 3ab² − b³ |

> **विशेष नोट:** यदि a + b + c = 0, तो a³ + b³ + c³ = **3abc** — यह BPSC में बार-बार आता है।

---

## 2. कोर कॉन्सेप्ट्स — BPSC के ट्रैप और गोल्डन रूल्स

### BPSC का सबसे बड़ा ट्रैप: α² + β² और α³ + β³

**ट्रैप:** "यदि द्विघात समीकरण के मूल α और β हों, तो α² + β² का मान ज्ञात करें।"

```
α² + β² = (α + β)² − 2αβ
         = (−b/a)² − 2(c/a)
         = b²/a² − 2c/a
```

**गलती:** छात्र α² + β² = (α+β)² लिखते हैं — यह गलत है, 2αβ घटाना जरूरी है।

---

**ट्रैप 2 — शेषफल का गलत sign:**
p(x) = x³ − 2x + 5 को (x + 1) से विभाजित करने पर शेषफल:
```
यहाँ (x + 1) = (x − (−1)), इसलिए a = −1
शेषफल = p(−1) = (−1)³ − 2(−1) + 5 = −1 + 2 + 5 = 6
```
**गलती:** छात्र a = +1 डाल देते हैं। (x + a) में a negative होता है।

---

**ट्रैप 3 — Degree की पहचान:**
$p(x) = x^3 + x^2 - 4x - 4$ — यह **Cubic (घनीय)** है, degree = 3, इसके **3 शून्यक** होंगे।

---

**ट्रैप 4 — D की इकाई (Discriminant का sign):**
$x^2 + x + 1 = 0$ के लिए: D = 1 − 4 = **−3 < 0** → कोई वास्तविक मूल नहीं।
BPSC में "मूलों की प्रकृति" पूछने वाले प्रश्न सबसे आसान होते हैं — D का sign ही उत्तर है।

---

## 3. वास्तविक परीक्षा प्रश्न (BPSC TRE-Style PYQs with Solution)

### PYQ-Style प्रश्न 1 — शेषफल प्रमेय

**यदि p(x) = x³ + 3x² − 2x + 5 को (x − 2) से विभाजित करें, तो शेषफल क्या होगा?**

हल (Remainder Theorem):
```
शेषफल = p(2)
       = (2)³ + 3(2)² − 2(2) + 5
       = 8 + 12 − 4 + 5
       = 21
```

उत्तर: **21**
> NCERT Source: Class 9, Ch 2 — Polynomials, Theorem 2.1 (Remainder Theorem)

---

### PYQ-Style प्रश्न 2 — मूलों का योग और गुणनफल

**द्विघात समीकरण 2x² − 5x + 3 = 0 के मूलों का योग और गुणनफल ज्ञात करें।**

हल:
```
a = 2, b = −5, c = 3

मूलों का योग (α + β) = −b/a = −(−5)/2 = 5/2

मूलों का गुणनफल (αβ) = c/a = 3/2
```

उत्तर: **α + β = 5/2, αβ = 3/2**
> NCERT Source: Class 10, Ch 2 — Polynomials

---

### PYQ-Style प्रश्न 3 — α² + β² (BPSC का सबसे पसंदीदा ट्रैप)

**यदि द्विघात समीकरण x² − 7x + 10 = 0 के मूल α और β हों, तो α² + β² का मान क्या होगा?**

हल:
```
α + β = 7, αβ = 10

α² + β² = (α + β)² − 2αβ
         = 49 − 20
         = 29
```

उत्तर: **29**
> NCERT Source: Class 10, Ch 2 (Polynomials) + Application

---

### PYQ-Style प्रश्न 4 — मूलों की प्रकृति

**x² − 4x + 4 = 0 के मूलों की प्रकृति बताएँ।**

हल:
```
D = b² − 4ac = (−4)² − 4(1)(4) = 16 − 16 = 0
```

D = 0 → **दो बराबर वास्तविक मूल (Equal roots)**
मूल: x = 4/2 = **2** (दोनों मूल = 2)
> NCERT Source: Class 10, Ch 4 — Quadratic Equations

---

## 4. NCERT मैपिंग (Source Mapping)

| NCERT Chapter | कक्षा | टॉपिक कवरेज | फ़ाइल संदर्भ |
|---|---|---|---|
| Ch 2 — Polynomials | 9 | Degree, Zeroes, Remainder Theorem, Factor Theorem | ieep202.pdf |
| Ch 2 — Polynomials | 10 | Zeroes-Coefficients relationship, Cubic polynomials | jeep202.pdf |
| Ch 4 — Quadratic Equations | 10 | Quadratic Formula, Nature of Roots (D), Word Problems | jeep204.pdf |

---

## 5. क्या पढ़ें और क्या छोड़ें

### ✅ क्या पढ़ें (High-Yield Topics)

- **बहुपद की डिग्री (Degree of Polynomial):** रेखीय, द्विघात, त्रिघात
- **शेषफल प्रमेय (Remainder Theorem):** p(a) की गणना
- **गुणनखंड प्रमेय (Factor Theorem):** p(a) = 0 → (x − a) गुणनखंड
- **द्विघात के मूल (Roots of Quadratic):** factorization, completing square, formula
- **α+β = −b/a और αβ = c/a:** हर प्रश्न में यही आधार
- **α² + β² और α³ + β³:** (α+β) और αβ से derive करना
- **विविक्तकर D = b² − 4ac:** मूलों की प्रकृति पहचानना
- **बीजगणितीय सर्वसमिकाएँ (Identities):** (a+b+c)², a³+b³+c³−3abc
- NCERT Class 9 Ch 2 + Class 10 Ch 2 & Ch 4 के सभी Examples + Exercises

### ❌ क्या छोड़ें (Low-Yield / Out-of-Scope)

- **व्युत्क्रम त्रिकोणमिति (Inverse Trigonometry)** — Class 12 स्तर, BPSC TGT में नहीं
- चतुर्घात (Degree 4) और उससे ऊँचे बहुपद
- Complex (काल्पनिक) मूलों की विस्तृत गणना
- Polynomial Long Division (सिर्फ Remainder Theorem काफी है)
- Matrix और Determinant — BPSC TGT Math के बाहर

---

## 6. FAQ — अक्सर पूछे जाने वाले प्रश्न

**Q1. BPSC TGT में बहुपद से कितने प्रश्न आते हैं?**
TRE 1.0/2.0/3.0 में कुल मिलाकर **46 प्रश्न (8.3%)** — यह तीसरा/चौथा सबसे बड़ा टॉपिक है। शेषफल प्रमेय और α+β प्रश्न सबसे ज़्यादा आते हैं।

---

**Q2. शेषफल प्रमेय और लंबा भाग (Long Division) में कौन-सा बेहतर है?**
**Remainder Theorem हमेशा बेहतर है** — जब divisor linear (x−a) हो। सीधे p(a) calculate करें, 30 सेकंड में उत्तर। Long Division में 3-5 मिनट लगते हैं।

---

**Q3. α² + β² निकालने में सबसे आम गलती क्या है?**
**गलती:** α² + β² = (α+β)² मान लेना।
**सही:** α² + β² = (α+β)² − **2αβ**
2αβ घटाना कभी मत भूलें — BPSC में यह ट्रैप हर paper में आता है।

---

**Q4. Discriminant (D) क्या है और इसे कैसे याद रखें?**
D = b² − 4ac — यह quadratic ax²+bx+c=0 का "quality meter" है।
- D > 0 → 2 अलग वास्तविक मूल ✓
- D = 0 → 2 बराबर मूल (repeated) ✓
- D < 0 → कोई वास्तविक मूल नहीं ✗

याद करने का तरीका: **"Positive = Possible, Zero = Same, Negative = None"**

---

**Q5. α + β = −b/a में negative sign क्यों है?**
क्योंकि standard form ax² + bx + c = 0 में, Vieta's formulas से: मूलों का योग = −b/a। जब equation को (x−α)(x−β) = 0 expand करें तो coefficient of x = −(α+β), जो equation में b = a×(−(α+β)) बनाता है।

---

**Q6. गुणनखंड प्रमेय (Factor Theorem) कब apply करते हैं?**
जब यह जानना हो कि कोई value p(x) का zero (शून्यक) है या नहीं।
- p(a) = 0 → (x−a) गुणनखंड है
- p(a) ≠ 0 → (x−a) गुणनखंड नहीं, और p(a) = शेषफल

---

**Q7. नया द्विघात समीकरण कैसे बनाएँ जब α और β दिए हों?**
सूत्र: **x² − (α+β)x + αβ = 0**
उदाहरण: मूल 3 और 5 हों → x² − (3+5)x + (3×5) = 0 → **x² − 8x + 15 = 0**

---

**Q8. a³ + b³ + c³ − 3abc का shortcut कब use करें?**
जब a + b + c = 0, तो a³ + b³ + c³ = 3abc।
BPSC में यह type का प्रश्न: "यदि x + y + z = 0 हो, तो x³ + y³ + z³ का मान" → उत्तर सीधे **3xyz**।

---

**Q9. Completing the Square (वर्ग पूर्ण करना) जरूरी है?**
BPSC TRE के लिए Quadratic Formula (श्रीधराचार्य सूत्र) पर्याप्त है। Completing the Square की method समझने के लिए जरूरी है (NCERT Class 10 Ch 4 में explanation है) लेकिन परीक्षा में formula ही use करें।

---

**Q10. Polynomial का degree और zeroes में क्या सम्बन्ध है?**
**Degree = Maximum possible zeroes की संख्या।**
- Degree 1 (linear) → 1 zero
- Degree 2 (quadratic) → 2 zeroes
- Degree 3 (cubic) → 3 zeroes
BPSC में "किसी polynomial के अधिकतम शून्यक" पूछते हैं — उत्तर = degree।

---

## 7. त्वरित चेकलिस्ट (Quick Action Checklist)

- [ ] NCERT Class 9 Ch 2 — Polynomials: सभी Exercises + Examples हल करें
- [ ] NCERT Class 10 Ch 2 — Polynomials: zeroes-coefficients relationship याद करें
- [ ] NCERT Class 10 Ch 4 — Quadratic Equations: D = b² − 4ac practice करें
- [ ] Remainder Theorem: 10 प्रश्न सिर्फ p(a) calculate करके हल करें
- [ ] α+β = −b/a और αβ = c/a — 10 equations से practice करें
- [ ] α² + β², α³ + β³ वाले 5 प्रश्न हल करें (2αβ घटाना याद रखें)
- [ ] D के तीनों cases (>0, =0, <0) के 2-2 उदाहरण note करें
- [ ] बीजगणितीय सर्वसमिकाएँ: (a+b+c)² और a³+b³+c³−3abc याद करें
- [ ] श्रीधराचार्य सूत्र से 5 equations हल करें (दोनों ± cases)
- [ ] TRE PYQs में Algebra section separately attempt करें और time note करें

---

📌 **अगला आर्टिकल → Article 06: BPSC TGT Math — त्रिकोणमिति एवं ऊँचाई-दूरी Masterclass: सर्वसमिकाएँ, विशेष कोण, उन्नयन-अवनमन कोण (15.4% Weightage)**
