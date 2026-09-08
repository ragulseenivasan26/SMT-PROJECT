"""
Engineering NEC Symbols, Schematics & Vernacular Pedagogical Engine
Compliant with:
- National Electrical Code (NEC / NFPA 70)
- IEEE Standard 315 / ANSI Y32.2 (Electrical & Electronics Graphic Symbols)
- IEC 60617 (International Electrotechnical Commission)
- Bureau of Indian Standards (BIS SP 30 - National Electrical Code of India)
- NEP 2020 Mother-Tongue Technical Education
"""

import re
import math
from typing import Dict, List, Any, Optional

# ============================================================================
# COMPREHENSIVE ENGINEERING NEC & SCHEMATIC SYMBOLS DATABASE (45+ Symbols)
# ============================================================================
ENGINEERING_SYMBOLS_DB: List[Dict[str, Any]] = [
    # -------------------------------------------------------------------------
    # CATEGORY: ELECTRICAL POWER & WIRING (NEC STANDARDS)
    # -------------------------------------------------------------------------
    {
        "id": "earth_ground",
        "name": "Earth Ground",
        "category": "electrical_wiring",
        "category_name": "Electrical Power & Wiring",
        "nec_code": "NEC Article 250 (Grounding and Bonding)",
        "ieee_code": "IEEE 315 Sec. 2.1.1 / IEC 60617-02-15-01",
        "symbol_type": "Schematic / Blueprint",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><line x1="50" y1="15" x2="50" y2="55" stroke="currentColor" stroke-width="4"/><line x1="20" y1="55" x2="80" y2="55" stroke="currentColor" stroke-width="5" stroke-linecap="round"/><line x1="32" y1="67" x2="68" y2="67" stroke="currentColor" stroke-width="4" stroke-linecap="round"/><line x1="42" y1="79" x2="58" y2="79" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg>',
        "formula": "R_ground <= 25 Ohms (NEC 250.53(A)(2) Single Electrode Rule)",
        "pinout_specs": "Electrode connection: Bare Copper Wire (6 AWG to 2/0 AWG), Ground Rod minimum 8 ft (2.44 m)",
        "english_desc": "Direct physical electrical connection to the earth's mass. Dissipates lightning surges, stabilizes circuit voltage relative to earth, and provides a safe zero-potential reference plane.",
        "tamil": {
            "name": "பூமி இணைப்பு (Earth Ground)",
            "explanation": "மின்னோட்டத்தை பாதுகாப்பாக பூமியுடன் இணைக்கும் அமைப்பு. மின்னல் தாக்கம் மற்றும் அதிர்வு மின்னழுத்தங்களிலிருந்து (Surge) மின் சாதனங்களையும் மனிதர்களையும் பாதுகாக்கும் பூஜ்ஜிய மின்னழுத்த (0V) பாதுகாப்பு கம்பி.",
            "application": "வீட்டு சுவிட்ச்போர்டு, தொழிற்சாலை மோட்டார்கள் மற்றும் மின் பகிர்மான பெட்டிகள் (Earthing Rod)."
        },
        "hindi": {
            "name": "अर्थ ग्राउंड (Earth Ground)",
            "explanation": "बिजली के झटके और ओवर-वोल्टेज से सुरक्षा के लिए सर्किट को सीधे पृथ्वी से जोड़ने वाला सुरक्षा कनेक्शन। यह 0V संदर्भ प्रदान करता है।",
            "application": "घरेलू वायरिंग, ट्रांसफार्मर और मुख्य पैनल।"
        },
        "telugu": {
            "name": "ఎర్త్ గ్రౌండ్ (Earth Ground)",
            "explanation": "విద్యుత్ సర్క్యూట్‌ను భూమితో కలిపే రక్షణ వ్యవస్థ. షార్ట్ సర్క్యూట్ మరియు అధిక వోల్టేజ్ నుండి కాపాడుతుంది.",
            "application": "గృహ వైరింగ్ మరియు మోటార్లు."
        }
    },
    {
        "id": "circuit_breaker",
        "name": "Circuit Breaker",
        "category": "electrical_wiring",
        "category_name": "Electrical Power & Wiring",
        "nec_code": "NEC Article 240 (Overcurrent Protection)",
        "ieee_code": "IEEE 315 Sec. 13.1 / IEC 60617-07-02-01",
        "symbol_type": "Schematic / Blueprint",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><line x1="15" y1="50" x2="35" y2="50" stroke="currentColor" stroke-width="4"/><circle cx="35" cy="50" r="3" fill="currentColor"/><path d="M 35 48 Q 50 20 65 52" fill="none" stroke="currentColor" stroke-width="4"/><circle cx="65" cy="50" r="3" fill="currentColor"/><line x1="65" y1="50" x2="85" y2="50" stroke="currentColor" stroke-width="4"/><line x1="42" y1="28" x2="58" y2="28" stroke="#f59e0b" stroke-width="3" stroke-dasharray="2,2"/></svg>',
        "formula": "I_trip >= 125% of Continuous Load (NEC 210.20(A))",
        "pinout_specs": "Standard ratings: 15A, 20A, 30A, 50A, 100A, 200A; Interrupting Rating (AIC): 10kA to 65kA",
        "english_desc": "An automatically operated electrical switch designed to protect an electrical circuit from damage caused by excess current from an overload or short circuit.",
        "tamil": {
            "name": "மின்சுற்று முறிப்பான் (Circuit Breaker)",
            "explanation": "மின்சுற்றில் அதிகப்படியான மின்னோட்டம் (Overload) அல்லது குறுக்குச்சுற்று (Short Circuit) ஏற்படும்போது, தானாகவே மின் இணைப்பைத் துண்டித்து தீவிபத்துகளைத் தடுக்கும் தானியங்கி பாதுகாப்பு கருவி (MCB/MCCB).",
            "application": "வீடுகள் மற்றும் தொழிற்சாலைகளின் மெயின் டிஸ்ட்ரிபியூஷன் போர்டு (MCB, MCCB, ELCB)."
        },
        "hindi": {
            "name": "सर्किट ब्रेकर (Circuit Breaker)",
            "explanation": "अत्यधिक करंट या शॉर्ट सर्किट होने पर बिजली के प्रवाह को स्वतः बंद करने वाला सुरक्षात्मक स्विच।",
            "application": "डिस्ट्रीब्यूशन बोर्ड और औद्योगिक सुरक्षा।"
        },
        "telugu": {
            "name": "సర్క్యూట్ బ్రేకర్ (Circuit Breaker)",
            "explanation": "అధిక విద్యుత్ లేదా షార్ట్ సర్క్యూట్ సంభవించినప్పుడు విద్యుత్ సరఫరాను ఆటోమేటిక్‌గా నిలిపివేసే పరికరం.",
            "application": "మెయిన్ డిస్ట్రిబ్యూషన్ బోర్డులు."
        }
    },
    {
        "id": "single_pole_switch",
        "name": "Single-Pole Switch (SPST)",
        "category": "electrical_wiring",
        "category_name": "Electrical Power & Wiring",
        "nec_code": "NEC Article 404 (Switches)",
        "ieee_code": "IEEE 315 Sec. 4.1.1 / ANSI Y32.2",
        "symbol_type": "Architectural Blueprint & Schematic",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><line x1="15" y1="50" x2="35" y2="50" stroke="currentColor" stroke-width="4"/><circle cx="35" cy="50" r="4" fill="currentColor"/><line x1="35" y1="48" x2="65" y2="22" stroke="currentColor" stroke-width="4" stroke-linecap="round"/><circle cx="65" cy="50" r="4" fill="currentColor"/><line x1="65" y1="50" x2="85" y2="50" stroke="currentColor" stroke-width="4"/><text x="45" y="85" font-size="16" font-weight="bold" fill="#06b6d4" text-anchor="middle">S</text></svg>',
        "formula": "Open: R = Infinity, I = 0; Closed: R ≈ 0, V_drop ≈ 0",
        "pinout_specs": "Hot Line In, Switched Hot Out, Ground terminal; Standard 120V/240V 15A/20A rating",
        "english_desc": "Controls lighting or equipment from a single location by making or breaking the hot/live conductor path.",
        "tamil": {
            "name": "ஒற்றை முனை சுவிட்ச் (Single-Pole Switch)",
            "explanation": "ஒரே இடத்திலிருந்து மின் விளக்கு அல்லது சாதனத்திற்கு செல்லும் மின்சாரத்தை இயக்கவும் (ON) நிறுத்தவும் (OFF) பயன்படும் அடிப்படை மின் சுவிட்ச்.",
            "application": "அறை விளக்குகள், மின்விசிறிகள் மற்றும் பொதுவான மின் உபகரணங்கள்."
        },
        "hindi": {
            "name": "सिंगल पोल स्विच (Single Pole Switch)",
            "explanation": "एक ही स्थान से किसी उपकरण या लाइट को चालू या बंद करने वाला मानक स्विच।",
            "application": "कमरे की लाइट और पंखे।"
        },
        "telugu": {
            "name": "సింగిల్ పోల్ స్విచ్ (Single Pole Switch)",
            "explanation": "ఒకే ప్రదేశం నుండి విద్యుత్ ఉపకరణాన్ని ఆన్ లేదా ఆఫ్ చేయడానికి ఉపయోగించే స్విచ్.",
            "application": "లైట్లు మరియు ఫ్యాన్లు."
        }
    },
    {
        "id": "duplex_receptacle",
        "name": "Duplex Receptacle / Outlet",
        "category": "electrical_wiring",
        "category_name": "Electrical Power & Wiring",
        "nec_code": "NEC Article 210.52 (Dwelling Unit Receptacle Outlets)",
        "ieee_code": "ANSI / IEEE Std 315 Plan Symbol",
        "symbol_type": "Architectural Blueprint",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><circle cx="50" cy="50" r="32" fill="none" stroke="currentColor" stroke-width="4"/><line x1="50" y1="18" x2="50" y2="82" stroke="currentColor" stroke-width="4"/><line x1="38" y1="50" x2="38" y2="70" stroke="currentColor" stroke-width="3"/><line x1="62" y1="50" x2="62" y2="70" stroke="currentColor" stroke-width="3"/></svg>',
        "formula": "Max Spacing: 12 ft between outlets along floor line (NEC 210.52(A)(1))",
        "pinout_specs": "NEMA 5-15R / 5-20R: Hot (Brass), Neutral (Silver), Ground (Green screw); 125V 15A/20A",
        "english_desc": "Standard wall outlet providing two plug sockets for connecting portable appliances and cords to electrical power.",
        "tamil": {
            "name": "இரட்டை மின் சொருகுவாய் (Duplex Outlet / Socket)",
            "explanation": "சுவர்களில் பொருத்தப்படும் நிலையான இரண்டு-பிளக் மின் சொருகி (Socket). இதில் Hot (மின்சாரம்), Neutral (மடக்கு கம்பி) மற்றும் Ground (பூமி) கம்பிகள் இணைக்கப்பட்டிருக்கும்.",
            "application": "வீட்டு உபயோக பொருட்கள், லேப்டாப் மற்றும் சார்ஜர் இணைப்புகள்."
        },
        "hindi": {
            "name": "डुप्लेक्स सॉकेट (Duplex Outlet)",
            "explanation": "दीवार पर लगा मानक दो-प्लग आउटलेट जिसमें घरेलू उपकरण जोड़े जाते हैं।",
            "application": "घरेलू प्लग पॉइंट।"
        },
        "telugu": {
            "name": "డ్యూప్లెక్స్ అవుట్‌లెట్ (Duplex Outlet)",
            "explanation": "గోడపై అమర్చే ప్రామాణిక రెండు సాకెట్ల విద్యుత్ ప్లగ్ పాయింట్.",
            "application": "గృహ విద్యుత్ ప్లగ్గులు."
        }
    },
    {
        "id": "gfci_receptacle",
        "name": "GFCI Receptacle (Ground-Fault Interrupter)",
        "category": "electrical_wiring",
        "category_name": "Electrical Power & Wiring",
        "nec_code": "NEC Article 210.8 (Ground-Fault Circuit-Interrupter Protection)",
        "ieee_code": "NEC Safety Code Mandated Device",
        "symbol_type": "Architectural Blueprint",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><circle cx="50" cy="50" r="32" fill="none" stroke="currentColor" stroke-width="4"/><line x1="50" y1="18" x2="50" y2="82" stroke="currentColor" stroke-width="4"/><text x="50" y="55" font-size="14" font-weight="bold" fill="#10b981" text-anchor="middle">GFI</text></svg>',
        "formula": "Trip Threshold: 4 mA to 6 mA leakage current within 25 ms (Class A GFCI)",
        "pinout_specs": "Line terminals (Supply), Load terminals (Protected downstream downstream outlets), Test & Reset buttons",
        "english_desc": "Detects hazardous ground fault currents (current leakage to ground via water or human body) and cuts power in milliseconds to prevent electrocution.",
        "tamil": {
            "name": "மின்கசிவு பாதுகாப்பு சொருகுவாய் (GFCI / RCD)",
            "explanation": "தண்ணீர் அல்லது ஈரப்பதம் உள்ள இடங்களில் மனித உடலில் மின்சாரம் பாயும் ஆபத்து ஏற்பட்டால் (4-6 மில்லிஆம்பியர் கசிவு), 25 மில்லி வினாடிகளுக்குள் மின்சாரத்தை முழுமையாக நிறுத்தி உயிரைக் காக்கும் நவீன பாதுகாப்பு சாதனம்.",
            "application": "குளியலறை, சமையலறை, தோட்டம் மற்றும் வெளிப்புற நீர்ப்பாசன பகுதிகள் (NEC 210.8 கட்டாயம்)."
        },
        "hindi": {
            "name": "जीएफसीआई सॉकेट (GFCI Receptacle)",
            "explanation": "पानी या नमी वाले स्थानों पर करंट लीक होने पर तुरंत बिजली काटकर इंसान को बिजली के झटके से बचाने वाला उपकरण।",
            "application": "बाथरूम, किचन और गीले क्षेत्र।"
        },
        "telugu": {
            "name": "జిఎఫ్ సిఐ సాకెట్ (GFCI Receptacle)",
            "explanation": "కరెంట్ లీకేజ్ జరిగినప్పుడు మిల్లీ సెకన్లలో విద్యుత్‌ను కత్తిరించి ప్రాణాలను రక్షించే రక్షణ ప్లగ్.",
            "application": "స్నానాల గదులు మరియు వంటశాలలు."
        }
    },
    {
        "id": "panelboard",
        "name": "Distribution Panelboard / Load Center",
        "category": "electrical_wiring",
        "category_name": "Electrical Power & Wiring",
        "nec_code": "NEC Article 408 (Switchboards and Panelboards)",
        "ieee_code": "IEEE 315 Sec. 18 / ANSI Y32.2",
        "symbol_type": "Architectural Blueprint",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><rect x="25" y="15" width="50" height="70" fill="none" stroke="currentColor" stroke-width="4"/><line x1="25" y1="15" x2="75" y2="85" stroke="currentColor" stroke-width="3"/><polygon points="25,15 75,15 75,85" fill="rgba(99,102,241,0.25)"/><text x="50" y="94" font-size="10" font-weight="bold" fill="#c7d2fe" text-anchor="middle">PANEL</text></svg>',
        "formula": "Working Space: 3 ft depth x 30 in width x 6.5 ft height (NEC 110.26)",
        "pinout_specs": "Main Lugs or Main Breaker (100A-400A), Busbars (Copper/Aluminum), Neutral bar, Ground bar",
        "english_desc": "Enclosure housing overcurrent protective devices (circuit breakers) for division of electrical power into branch circuits.",
        "tamil": {
            "name": "மின் பகிர்மான பெட்டி (Distribution Panelboard / DB Box)",
            "explanation": "பிரதான மின்சாரத்தை பெற்று, கட்டிடத்தின் பல்வேறு அறைகளுக்கு பாதுகாப்பாக பல துணை மின்சுற்றுகளாக (Branch Circuits) பிரித்தளிக்கும் பிரதான பிரேக்கர் கட்டுப்பாட்டு பலகை.",
            "application": "வீடுகள், பள்ளிகள், கல்லூரிகள் மற்றும் தொழிற்சாலைகளின் மெயின் போர்டு."
        },
        "hindi": {
            "name": "डिस्ट्रीब्यूशन पैनल (Panelboard)",
            "explanation": "मुख्य विद्युत आपूर्ति को घर के विभिन्न कमरों में सुरक्षित रूप से वितरित करने वाला मुख्य पैनल।",
            "application": "इमारतों का मुख्य विद्युत बोर्ड।"
        },
        "telugu": {
            "name": "డిస్ట్రిబ్యూషన్ ప్యానెల్ (Distribution Panelboard)",
            "explanation": "ప్రధాన విద్యుత్‌ను వివిధ గదులకు శాఖలుగా పంపిణీ చేసే విద్యుత్ కంట్రోల్ ప్యానెల్.",
            "application": "ప్రధాన సర్క్యూట్ బోర్డు."
        }
    },
    {
        "id": "transformer",
        "name": "Step-Down / Step-Up Transformer",
        "category": "electrical_wiring",
        "category_name": "Electrical Power & Wiring",
        "nec_code": "NEC Article 450 (Transformers and Vaults)",
        "ieee_code": "IEEE 315 Sec. 6.1 / IEC 60617-06-09-01",
        "symbol_type": "Schematic / Blueprint",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><path d="M 20 25 A 12 12 0 0 1 20 45 A 12 12 0 0 1 20 65 A 12 12 0 0 1 20 85" fill="none" stroke="currentColor" stroke-width="4"/><line x1="44" y1="20" x2="44" y2="85" stroke="currentColor" stroke-width="3"/><line x1="56" y1="20" x2="56" y2="85" stroke="currentColor" stroke-width="3"/><path d="M 80 25 A 12 12 0 0 0 80 45 A 12 12 0 0 0 80 65 A 12 12 0 0 0 80 85" fill="none" stroke="#06b6d4" stroke-width="4"/><line x1="8" y1="25" x2="20" y2="25" stroke="currentColor" stroke-width="3"/><line x1="8" y1="85" x2="20" y2="85" stroke="currentColor" stroke-width="3"/><line x1="80" y1="25" x2="92" y2="25" stroke="#06b6d4" stroke-width="3"/><line x1="80" y1="85" x2="92" y2="85" stroke="#06b6d4" stroke-width="3"/></svg>',
        "formula": "V_p / V_s = N_p / N_s = I_s / I_p  |  Efficiency = (P_out / P_in) * 100%",
        "pinout_specs": "Primary windings (H1, H2), Secondary windings (X1, X2, X3 Center-tap)",
        "english_desc": "A passive component that transfers electrical energy from one electrical circuit to another through mutual electromagnetic induction, stepping AC voltage up or down.",
        "tamil": {
            "name": "மின்மாற்றி (Transformer)",
            "explanation": "மின்காந்த தூண்டல் கொள்கையின்படி, அதிர்வெண்ணை மாற்றாமல் மாற்று மின்னழுத்தத்தை (AC Voltage) உயர்த்தவோ (Step-Up) அல்லது குறைக்கவோ (Step-Down) செய்யும் கருவி.",
            "application": "தெரு மின்மாற்றிகள் (11kV to 230V/415V), மொபைல் சார்ஜர்கள் மற்றும் பவர் சப்ளைகள்."
        },
        "hindi": {
            "name": "ट्रांसफार्मर (Transformer)",
            "explanation": "विद्युत चुम्बकीय प्रेरण द्वारा एसी वोल्टेज को घटाने या बढ़ाने वाला उपकरण।",
            "application": "विद्युत ग्रिड और पावर एडेप्टर।"
        },
        "telugu": {
            "name": "ట్రాన్స్‌ఫార్మర్ (Transformer)",
            "explanation": "విద్యుదయస్కాంత ప్రేరణ ద్వారా వోల్టేజ్‌ను పెంచే లేదా తగ్గించే పరికరం.",
            "application": "విద్యుత్ పంపిణీ మరియు పవర్ సప్లైలు."
        }
    },
    {
        "id": "induction_motor",
        "name": "Three-Phase Induction Motor",
        "category": "electrical_wiring",
        "category_name": "Electrical Power & Wiring",
        "nec_code": "NEC Article 430 (Motors, Motor Circuits, and Controllers)",
        "ieee_code": "IEEE 315 Sec. 2.2 / IEC 60617-06-01-01",
        "symbol_type": "Schematic / Blueprint",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><circle cx="50" cy="50" r="32" fill="none" stroke="currentColor" stroke-width="4"/><text x="50" y="58" font-size="24" font-weight="bold" fill="currentColor" text-anchor="middle">M</text><text x="68" y="42" font-size="12" font-weight="bold" fill="#f59e0b">3~</text><line x1="50" y1="5" x2="50" y2="18" stroke="currentColor" stroke-width="3"/><line x1="38" y1="8" x2="42" y2="18" stroke="currentColor" stroke-width="3"/><line x1="62" y1="8" x2="58" y2="18" stroke="currentColor" stroke-width="3"/></svg>',
        "formula": "Synchronous Speed: N_s = (120 * f) / P  |  Slip s = (N_s - N_r) / N_s",
        "pinout_specs": "Terminals: U1-U2, V1-V2, W1-W2 for Star (Y) or Delta (Δ) configuration",
        "english_desc": "An AC electric motor in which the electric current in the rotor needed to produce torque is obtained by electromagnetic induction from the magnetic field of the stator winding.",
        "tamil": {
            "name": "முக்கட்ட தூண்டல் மோட்டார் (3-Phase Induction Motor)",
            "explanation": "மின்னாற்றலை சுழலும் இயந்திர ஆற்றலாக மாற்றும் மோட்டார். சுழலும் காந்தப்புலத்தின் (RMF) தூண்டலால் ரோட்டார் சுழல்கிறது. அதிக ஆயுள் மற்றும் பிரஷ் இல்லாத எளிமையான அமைப்பு கொண்டது.",
            "application": "விவசாய பம்புசெட், லிப்ட், தொழிற்சாலை இயந்திரங்கள் மற்றும் மின்சார ரயில்கள்."
        },
        "hindi": {
            "name": "थ्री-फेज इंडक्शन मोटर (Induction Motor)",
            "explanation": "विद्युत ऊर्जा को यांत्रिक ऊर्जा में बदलने वाली मोटर जो औद्योगिक कार्यों में सबसे अधिक प्रयोग होती है।",
            "application": "वाटर पंप, कंप्रेसर और कारखाने।"
        },
        "telugu": {
            "name": "ఇండక్షన్ మోటార్ (Induction Motor)",
            "explanation": "విద్యుత్ శక్తిని యాంత్రిక శక్తిగా మార్చే మోటార్.",
            "application": "వ్యవసాయ పంపులు మరియు పరిశ్రమలు."
        }
    },

    # -------------------------------------------------------------------------
    # CATEGORY: ELECTRONICS & SEMICONDUCTORS (IEEE 315 / IEC STANDARDS)
    # -------------------------------------------------------------------------
    {
        "id": "resistor",
        "name": "Fixed Resistor",
        "category": "electronics",
        "category_name": "Electronics & Semiconductors",
        "nec_code": "IEEE Std 315 Clause 4.1 / IEC 60617-04-01-01",
        "ieee_code": "IEEE 315 / ANSI Y32.2 Zig-Zag Symbol",
        "symbol_type": "Schematic",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><line x1="10" y1="50" x2="25" y2="50" stroke="currentColor" stroke-width="4"/><path d="M 25 50 L 30 32 L 40 68 L 50 32 L 60 68 L 70 32 L 75 50" fill="none" stroke="currentColor" stroke-width="4" stroke-linejoin="round"/><line x1="75" y1="50" x2="90" y2="50" stroke="currentColor" stroke-width="4"/></svg>',
        "formula": "Ohm's Law: V = I * R  |  Power Dissipation: P = I^2 * R = V^2 / R",
        "pinout_specs": "Non-polarized 2-lead component; Standard values: E12 / E24 series (1 Ohm to 10M Ohm), 1/4W to 5W",
        "english_desc": "A passive two-terminal electrical component that implements electrical resistance as a circuit element to reduce current flow and divide voltages.",
        "tamil": {
            "name": "மின்தடை / மின்தடையாக்கி (Resistor)",
            "explanation": "மின்சுற்றில் பாயும் மின்னோட்டத்தின் (Current) வேகத்தைக் குறைத்து கட்டுப்படுத்தும் மற்றும் மின்னழுத்தத்தை பிரித்தளிக்கும் அடிப்படை மின்னணு பாகம். இது ஓம் விதியை (V = IR) பின்பற்றுகிறது.",
            "application": "LED பாதுகாப்பு மின்தடை, ஆடியோ வால்யூம் கட்டுப்பாடு மற்றும் மின்னழுத்த வகுப்பிகள் (Voltage Divider)."
        },
        "hindi": {
            "name": "प्रतिरोधक (Resistor)",
            "explanation": "सर्किट में करंट के प्रवाह को सीमित और नियंत्रित करने वाला निष्क्रिय घटक (V = IR)।",
            "application": "करंट लिमिटिंग और वोल्टेज डिवाइडर।"
        },
        "telugu": {
            "name": "నిరోధకం (Resistor)",
            "explanation": "సర్క్యూట్‌లో విద్యుత్ ప్రవాహాన్ని నియంత్రించే మరియు తగ్గించే పరికరం.",
            "application": "కరెంట్ లిమిటింగ్ మరియు ఎలక్ట్రానిక్స్."
        }
    },
    {
        "id": "capacitor_polarized",
        "name": "Electrolytic Polarized Capacitor",
        "category": "electronics",
        "category_name": "Electronics & Semiconductors",
        "nec_code": "IEEE Std 315 Clause 4.2 / IEC 60617-04-02-01",
        "ieee_code": "ANSI / IEEE Std 315 Curved Plate Symbol",
        "symbol_type": "Schematic",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><line x1="10" y1="50" x2="42" y2="50" stroke="currentColor" stroke-width="4"/><line x1="42" y1="20" x2="42" y2="80" stroke="currentColor" stroke-width="5"/><path d="M 58 20 Q 50 50 58 80" fill="none" stroke="#06b6d4" stroke-width="5"/><line x1="55" y1="50" x2="90" y2="50" stroke="#06b6d4" stroke-width="4"/><text x="30" y="32" font-size="20" font-weight="bold" fill="#10b981">+</text></svg>',
        "formula": "Q = C * V  |  Energy: E = 0.5 * C * V^2  |  Reactance: X_C = 1 / (2 * pi * f * C)",
        "pinout_specs": "Anode (+) longer lead, Cathode (-) marked with stripe; Voltage rating must exceed circuit peak by >=20%",
        "english_desc": "Stores electrical energy in an electrostatic field between two conductive plates separated by a dielectric. Blocks DC while passing AC signals.",
        "tamil": {
            "name": "மின்தேக்கி (Capacitor / Condenser)",
            "explanation": "மின்னாற்றலை மின்புல வடிவில் தற்காலிகமாக சேமித்து வைக்கும் சாதனம். இது நேர் மின்னோட்டத்தை (DC) தடுத்து, மாற்று மின்னோட்டத்தை (AC) கடத்துகிறது. மின்சார ஏற்றத்தாழ்வுகளை சீராக்குகிறது (Filter).",
            "application": "மின்விசிறி ஸ்டார்டர் (Capacitor Run), பவர் சப்ளை வடிகட்டி (Filter), மற்றும் ஆடியோ ஆஸிலேட்டர்கள்."
        },
        "hindi": {
            "name": "संधारित्र / कैपेसिटर (Capacitor)",
            "explanation": "विद्युत आवेश (चार्ज) और ऊर्जा को संग्रहीत करने वाला घटक। यह डीसी को रोकता है और एसी को जाने देता है।",
            "application": "फिल्टर सर्किट, पंखे का कंडेनसर और टाइमर।"
        },
        "telugu": {
            "name": "కెపాసిటర్ (Capacitor)",
            "explanation": "విద్యుత్ చార్జ్‌ను నిల్వ చేసే పరికరం. ఫిల్టర్ చేయడానికి మరియు ఫ్యాన్ స్టార్టింగ్‌కు ఉపయోగపడుతుంది.",
            "application": "ఫ్యాన్లు మరియు పవర్ సప్లైలు."
        }
    },
    {
        "id": "inductor",
        "name": "Inductor / Choke Coil",
        "category": "electronics",
        "category_name": "Electronics & Semiconductors",
        "nec_code": "IEEE Std 315 Clause 6.2 / IEC 60617-04-03-01",
        "ieee_code": "ANSI / IEEE Std 315 Arched Coil Symbol",
        "symbol_type": "Schematic",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><line x1="10" y1="50" x2="22" y2="50" stroke="currentColor" stroke-width="4"/><path d="M 22 50 A 9 9 0 0 1 40 50 A 9 9 0 0 1 58 50 A 9 9 0 0 1 76 50" fill="none" stroke="currentColor" stroke-width="4"/><line x1="76" y1="50" x2="90" y2="50" stroke="currentColor" stroke-width="4"/></svg>',
        "formula": "V_L = L * (di / dt)  |  Inductive Reactance: X_L = 2 * pi * f * L  |  Energy: E = 0.5 * L * I^2",
        "pinout_specs": "Values in microhenries (μH) to Henries (H); Core types: Air, Ferrite, Iron core",
        "english_desc": "A passive two-terminal electrical component that stores energy in a magnetic field when electric current flows through it. Opposes rapid changes in current.",
        "tamil": {
            "name": "மின்தூண்டி (Inductor / Choke)",
            "explanation": "மின்னோட்டம் பாயும்போது காந்தப்புல வடிவில் ஆற்றலை சேமிக்கும் கம்பிச்சுருள். இது மின்னோட்டத்தில் ஏற்படும் திடீர் மாற்றங்களை எதிர்க்கிறது (Lenz's Law). AC சிக்னலை தடுத்து DC-ஐ கடத்துகிறது.",
            "application": "டியூப்லைட் சோக், SMPS பவர் சப்ளை, ரேடியோ அதிர்வெண் ட்யூனிங் சுற்றுகள்."
        },
        "hindi": {
            "name": "प्रेरक / इंडक्टर (Inductor)",
            "explanation": "चुंबकीय क्षेत्र में ऊर्जा संग्रहीत करने वाली कॉइल जो करंट के अचानक बदलाव का विरोध करती है।",
            "application": "चोक कॉइल, रेडियो फिल्टर और कन्वर्टर।"
        },
        "telugu": {
            "name": "ఇండక్టర్ (Inductor)",
            "explanation": "అయస్కాంత క్షేత్రంలో శక్తిని నిల్వ చేసే కాయిల్. కరెంట్ మార్పులను నిరోధిస్తుంది.",
            "application": "చోక్ మరియు రేడియో సర్క్యూట్లు."
        }
    },
    {
        "id": "pn_diode",
        "name": "PN Junction Diode",
        "category": "electronics",
        "category_name": "Electronics & Semiconductors",
        "nec_code": "IEEE Std 315 Clause 8.1 / IEC 60617-05-01-01",
        "ieee_code": "ANSI / IEEE Std 315 Semiconductor Diode",
        "symbol_type": "Schematic",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><line x1="10" y1="50" x2="35" y2="50" stroke="currentColor" stroke-width="4"/><polygon points="35,25 35,75 65,50" fill="rgba(99,102,241,0.3)" stroke="currentColor" stroke-width="4"/><line x1="65" y1="25" x2="65" y2="75" stroke="#f43f5e" stroke-width="5"/><line x1="65" y1="50" x2="90" y2="50" stroke="currentColor" stroke-width="4"/><text x="25" y="25" font-size="12" fill="#cbd5e1">A</text><text x="72" y="25" font-size="12" fill="#cbd5e1">K</text></svg>',
        "formula": "Shockley Equation: I = I_s * (e^(V / (n*V_T)) - 1)  |  Forward Barrier: ~0.7V (Silicon)",
        "pinout_specs": "Anode (P-type positive), Cathode (N-type silver band); e.g., 1N4007 (1000V 1A)",
        "english_desc": "A semiconductor device that acts as a one-way valve for current, conducting easily in the forward direction while blocking reverse current.",
        "tamil": {
            "name": "இருமுனையம் / டையோடு (Diode)",
            "explanation": "மின்னோட்டத்தை ஒரே திசையில் (நேர்முக சார்பு - Forward Bias) மட்டும் அனுமதித்து, எதிர் திசையில் (Reverse Bias) தடுக்கும் ஒருவழி மின் வால்வு. AC மின்னோட்டத்தை DC ஆக மாற்ற (Rectifier) உதவுகிறது.",
            "application": "AC to DC ரெக்டிஃபையர் (மின்னோட்ட திருத்தி), சோலார் பேனல் ரிவர்ஸ் பாதுகாப்பு."
        },
        "hindi": {
            "name": "डायोड (Diode)",
            "explanation": "एक तरफा करंट प्रवाहित करने वाला सेमीकंडक्टर उपकरण। यह एसी को डीसी में बदलने के काम आता है।",
            "application": "दिष्टकारी (Rectifier) और रिवर्स पोलारिटी सुरक्षा।"
        },
        "telugu": {
            "name": "డయోడ్ (Diode)",
            "explanation": "కరెంట్‌ను ఒకే దిశలో ప్రవహింపజేసే సెమీకండక్టర్ పరికరం.",
            "application": "రెక్టిఫైయర్ మరియు పవర్ అడాప్టర్లు."
        }
    },
    {
        "id": "led",
        "name": "Light Emitting Diode (LED)",
        "category": "electronics",
        "category_name": "Electronics & Semiconductors",
        "nec_code": "IEEE Std 315 Clause 8.2 / IEC 60617-05-01-04",
        "ieee_code": "ANSI / IEEE Std 315 Optical Diode",
        "symbol_type": "Schematic",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><line x1="10" y1="50" x2="35" y2="50" stroke="currentColor" stroke-width="4"/><polygon points="35,25 35,75 65,50" fill="rgba(16,185,129,0.3)" stroke="currentColor" stroke-width="4"/><line x1="65" y1="25" x2="65" y2="75" stroke="#10b981" stroke-width="5"/><line x1="65" y1="50" x2="90" y2="50" stroke="currentColor" stroke-width="4"/><line x1="50" y1="20" x2="65" y2="5" stroke="#10b981" stroke-width="3"/><polygon points="62,5 68,5 65,11" fill="#10b981"/><line x1="62" y1="25" x2="77" y2="10" stroke="#10b981" stroke-width="3"/><polygon points="74,10 80,10 77,16" fill="#10b981"/></svg>',
        "formula": "Photon Energy: E = h * c / lambda  |  Series Resistor: R = (V_supply - V_f) / I_f",
        "pinout_specs": "Long leg = Anode (+), Flat notch = Cathode (-); V_f: Red ~1.8V, Blue/White ~3.2V at 20mA",
        "english_desc": "A semiconductor light source that emits light when current flows through it as electrons recombine with electron holes releasing photons.",
        "tamil": {
            "name": "ஒளி உமிழ் இருமுனையம் (LED)",
            "explanation": "மின்னாற்றலை நேரடியாக ஒளியாக மாற்றும் நவீன இருமுனையம். எலக்ட்ரான்கள் துளைகளுடன் இணையும் போது ஃபோட்டான்களாக ஒளியை உமிழ்கிறது. குறைந்த மின்சாரத்தில் அதிக ஒளி தருகிறது.",
            "application": "வீட்டு எல்இடி பல்புகள், மொபைல்/டிவி திரைகள், டிராஃபிக் சிக்னல்கள்."
        },
        "hindi": {
            "name": "एलईडी (Light Emitting Diode)",
            "explanation": "विद्युत ऊर्जा को सीधे प्रकाश में बदलने वाला अर्धचालक। अत्यंत कम ऊर्जा की खपत करता है।",
            "application": "एलईडी बल्ब, डिस्प्ले और संकेतक।"
        },
        "telugu": {
            "name": "ఎల్ఈడీ (Light Emitting Diode)",
            "explanation": "విద్యుత్‌ను కాంతిగా మార్చే చిన్న డయోడ్.",
            "application": "లైట్లు మరియు డిస్‌ప్లేలు."
        }
    },
    {
        "id": "npn_transistor",
        "name": "NPN BJT Transistor",
        "category": "electronics",
        "category_name": "Electronics & Semiconductors",
        "nec_code": "IEEE Std 315 Clause 8.3 / IEC 60617-05-03-01",
        "ieee_code": "ANSI / IEEE Std 315 Bipolar Junction Transistor",
        "symbol_type": "Schematic",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><circle cx="50" cy="50" r="38" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="4,4"/><line x1="10" y1="50" x2="38" y2="50" stroke="currentColor" stroke-width="4"/><line x1="38" y1="25" x2="38" y2="75" stroke="currentColor" stroke-width="6"/><line x1="38" y1="36" x2="70" y2="18" stroke="currentColor" stroke-width="4"/><line x1="70" y1="18" x2="90" y2="18" stroke="currentColor" stroke-width="4"/><line x1="38" y1="64" x2="70" y2="82" stroke="currentColor" stroke-width="4"/><line x1="70" y1="82" x2="90" y2="82" stroke="currentColor" stroke-width="4"/><polygon points="62,72 72,83 60,84" fill="#f59e0b"/><text x="18" y="42" font-size="12" fill="#cbd5e1">B</text><text x="75" y="14" font-size="12" fill="#cbd5e1">C</text><text x="75" y="98" font-size="12" fill="#cbd5e1">E</text></svg>',
        "formula": "I_e = I_b + I_c  |  I_c = Beta * I_b  |  V_be ≈ 0.7V (Active Region)",
        "pinout_specs": "Base (B), Collector (C), Emitter (E); Popular models: BC547, 2N2222, 2N3904",
        "english_desc": "A current-controlled three-terminal semiconductor device used to amplify electrical signals or act as an electronic switch.",
        "tamil": {
            "name": "NPN திரிதடையம் (NPN Transistor)",
            "explanation": "மின்னணு சுற்றுகளின் இதயம் போன்ற சாதனம். சிறிய பேஸ் (Base) மின்னோட்டத்தைக் கொண்டு பெரிய கலெக்டர் (Collector) மின்னோட்டத்தைக் கட்டுப்படுத்துகிறது. பெருக்கியாகவும் (Amplifier) அதிவேக சுவிட்சாகவும் செயல்படுகிறது.",
            "application": "ஆடியோ பெருக்கிகள் (Amplifier), மைக்ரோகண்ட்ரோலர் ரிலே டிரைவர், கணினி லாஜிக் சுற்றுகள்."
        },
        "hindi": {
            "name": "एनपीएन ट्रांजिस्टर (NPN Transistor)",
            "explanation": "करंट द्वारा नियंत्रित तीन-टर्मिनल उपकरण जिसका उपयोग सिग्नल बढ़ाने (एम्पलीफायर) या स्विच के रूप में होता है।",
            "application": "एम्पलीफायर और डिजिटल स्विच।"
        },
        "telugu": {
            "name": "ఎన్‌పిఎన్ ట్రాన్సిస్టర్ (NPN Transistor)",
            "explanation": "సిగ్నల్స్‌ను పెంచడానికి (యాంప్లిఫైయర్) లేదా వేగవంతమైన స్విచ్‌గా పనిచేసే పరికరం.",
            "application": "యాంప్లిఫైయర్లు మరియు సర్క్యూట్ స్విచ్‌లు."
        }
    },
    {
        "id": "opamp",
        "name": "Operational Amplifier (Op-Amp)",
        "category": "electronics",
        "category_name": "Electronics & Semiconductors",
        "nec_code": "IEEE Std 315 Clause 14.1 / IEC 60617-12-01-01",
        "ieee_code": "ANSI / IEEE Std 315 Triangle Amplifier Symbol",
        "symbol_type": "Schematic",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><polygon points="25,15 25,85 85,50" fill="rgba(99,102,241,0.15)" stroke="currentColor" stroke-width="4"/><line x1="5" y1="35" x2="25" y2="35" stroke="currentColor" stroke-width="4"/><line x1="5" y1="65" x2="25" y2="65" stroke="currentColor" stroke-width="4"/><line x1="85" y1="50" x2="98" y2="50" stroke="currentColor" stroke-width="4"/><text x="32" y="38" font-size="16" font-weight="bold" fill="#f43f5e">-</text><text x="30" y="70" font-size="16" font-weight="bold" fill="#10b981">+</text><text x="5" y="30" font-size="10" fill="#94a3b8">Inv</text><text x="5" y="80" font-size="10" fill="#94a3b8">Non-Inv</text><text x="86" y="44" font-size="10" fill="#06b6d4">Out</text></svg>',
        "formula": "V_out = A_ol * (V_+ - V_-)  |  Inverting Gain: A_v = -R_f / R_in",
        "pinout_specs": "Dual power supply (+Vcc, -Vee); High input impedance (M-Ohms), Low output impedance (<100 Ohms); IC 741 / LM358",
        "english_desc": "A high-gain electronic voltage amplifier with differential inputs and single-ended output, widely used for analog signal processing, filtering, and math operations.",
        "tamil": {
            "name": "செயல்பாட்டு பெருக்கி (Operational Amplifier - Op-Amp)",
            "explanation": "மிக அதிக மிகைப்புத்திறன் (High Gain) கொண்ட அனலாக் சிக்னல் பெருக்கி. கூட்டல், கழித்தல், தொகையீடு (Integration) போன்ற கணித செயல்பாடுகள் மற்றும் வடிகட்டிகள் (Filters) செய்யப் பயன்படுகிறது.",
            "application": "சென்சார் சிக்னல் பெருக்கி, ஆடியோ மிக்சர், அனலாக் கணினி சுற்றுகள் (IC 741)."
        },
        "hindi": {
            "name": "ऑपरेशनल एम्पलीफायर (Op-Amp)",
            "explanation": "उच्च गेन वाला वोल्टेज एम्पलीफायर जो गणितीय कार्यों और सिग्नल फ़िल्टरिंग के लिए उपयोग होता है।",
            "application": "सेंसर सर्किट और ऑडियो मिक्सर।"
        },
        "telugu": {
            "name": "ఆపరేషనల్ యాంప్లిఫైయర్ (Op-Amp)",
            "explanation": "అనలాగ్ సిగ్నల్స్‌ను ప్రాసెస్ చేయడానికి ఉపయోగించే హై-గెయిన్ యాంప్లిఫైయర్.",
            "application": "సెన్సార్లు మరియు ఆడియో సర్క్యూట్లు."
        }
    },

    # -------------------------------------------------------------------------
    # CATEGORY: DIGITAL LOGIC GATES (IEEE 91 / IEC 60617-12)
    # -------------------------------------------------------------------------
    {
        "id": "and_gate",
        "name": "AND Gate",
        "category": "logic_gates",
        "category_name": "Digital Logic Gates",
        "nec_code": "IEEE Std 91-1984 / ANSI Y32.14 / IEC 60617-12",
        "ieee_code": "IEEE Distinctive Shape Logic Symbol",
        "symbol_type": "Digital Schematic",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><line x1="8" y1="35" x2="30" y2="35" stroke="currentColor" stroke-width="4"/><line x1="8" y1="65" x2="30" y2="65" stroke="currentColor" stroke-width="4"/><path d="M 30 20 L 55 20 A 30 30 0 0 1 55 80 L 30 80 Z" fill="rgba(6,182,212,0.2)" stroke="currentColor" stroke-width="4"/><line x1="80" y1="50" x2="95" y2="50" stroke="currentColor" stroke-width="4"/><text x="4" y="38" font-size="10" fill="#94a3b8">A</text><text x="4" y="68" font-size="10" fill="#94a3b8">B</text><text x="86" y="44" font-size="10" fill="#06b6d4">Y</text></svg>',
        "formula": "Boolean: Y = A * B  |  Truth Table: 0&0=0, 0&1=0, 1&0=0, 1&1=1",
        "pinout_specs": "TTL 7408 Quad 2-Input AND Gate IC; CMOS 4081; Vcc = 5V",
        "english_desc": "Outputs HIGH (1) only if all of its inputs are HIGH (1). If any input is LOW (0), output is LOW.",
        "tamil": {
            "name": "மற்றும் வாசல் (AND Gate)",
            "explanation": "அனைத்து உள்ளீடுகளும் (Inputs) 1 (True) ஆக இருந்தால் மட்டுமே வெளியீடு (Output) 1 ஆக இருக்கும் தருக்க வாயில். ஏதேனும் ஒரு உள்ளீடு 0 ஆனால் வெளியீடு 0 ஆகும்.",
            "application": "பாதுகாப்பு பூட்டுகள் (இரு சாவிகளும் இருந்தால் மட்டுமே கதவு திறக்கும் முறை), கணினி ALU."
        },
        "hindi": {
            "name": "एंड गेट (AND Gate)",
            "explanation": "डिजिटल लॉजिक गेट जिसका आउटपुट 1 तभी होता है जब दोनों इनपुट 1 हों।",
            "application": "कंप्यूटर प्रोसेसर और सुरक्षा लॉक।"
        },
        "telugu": {
            "name": "అండ్ గేట్ (AND Gate)",
            "explanation": "రెండు ఇన్‌పుట్‌లు 1 అయినప్పుడు మాత్రమే అవుట్‌పుట్ 1 ఇచ్చే లాజిక్ గేట్.",
            "application": "డిజిటల్ కంప్యూటర్లు."
        }
    },
    {
        "id": "or_gate",
        "name": "OR Gate",
        "category": "logic_gates",
        "category_name": "Digital Logic Gates",
        "nec_code": "IEEE Std 91-1984 / ANSI Y32.14 / IEC 60617-12",
        "ieee_code": "IEEE Distinctive Shape Logic Symbol",
        "symbol_type": "Digital Schematic",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><line x1="8" y1="35" x2="32" y2="35" stroke="currentColor" stroke-width="4"/><line x1="8" y1="65" x2="32" y2="65" stroke="currentColor" stroke-width="4"/><path d="M 28 20 Q 42 50 28 80 Q 60 78 82 50 Q 60 22 28 20 Z" fill="rgba(168,85,247,0.2)" stroke="currentColor" stroke-width="4"/><line x1="82" y1="50" x2="95" y2="50" stroke="currentColor" stroke-width="4"/><text x="4" y="38" font-size="10" fill="#94a3b8">A</text><text x="4" y="68" font-size="10" fill="#94a3b8">B</text><text x="86" y="44" font-size="10" fill="#a855f7">Y</text></svg>',
        "formula": "Boolean: Y = A + B  |  Truth Table: 0|0=0, 0|1=1, 1|0=1, 1|1=1",
        "pinout_specs": "TTL 7432 Quad 2-Input OR Gate IC; CMOS 4071",
        "english_desc": "Outputs HIGH (1) if at least one of its inputs is HIGH (1). Output is LOW (0) only when all inputs are LOW.",
        "tamil": {
            "name": "அல்லது வாசல் (OR Gate)",
            "explanation": "ஏதேனும் ஒரு உள்ளீடு (Input) 1 ஆனாலும் வெளியீடு (Output) 1 ஆக மாறும் தருக்க வாயில். இரண்டு உள்ளீடுகளும் 0 ஆக இருந்தால் மட்டுமே வெளியீடு 0 ஆகும்.",
            "application": "தீ எச்சரிக்கை அலாரம் (முன் கதவு அல்லது பின் கதவு சென்சார் தூண்டப்பட்டால் அலாரம் ஒலிக்கும் அமைப்பு)."
        },
        "hindi": {
            "name": "ऑर गेट (OR Gate)",
            "explanation": "डिजिटल गेट जिसमें कोई भी एक इनपुट 1 होने पर आउटपुट 1 हो जाता है।",
            "application": "अलार्म सिस्टम और डिजिटल चयनकर्ता।"
        },
        "telugu": {
            "name": "ఆర్ గేట్ (OR Gate)",
            "explanation": "ఏదైనా ఒక ఇన్‌పుట్ 1 అయితే అవుట్‌పుట్ 1 ఇచ్చే లాజిక్ గేట్.",
            "application": "ఫైర్ అలారాలు."
        }
    },
    {
        "id": "not_gate",
        "name": "NOT Gate / Inverter",
        "category": "logic_gates",
        "category_name": "Digital Logic Gates",
        "nec_code": "IEEE Std 91-1984 / ANSI Y32.14 / IEC 60617-12",
        "ieee_code": "IEEE Distinctive Shape Logic Symbol",
        "symbol_type": "Digital Schematic",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><line x1="8" y1="50" x2="30" y2="50" stroke="currentColor" stroke-width="4"/><polygon points="30,22 30,78 70,50" fill="rgba(244,63,94,0.2)" stroke="currentColor" stroke-width="4"/><circle cx="76" cy="50" r="5" fill="none" stroke="currentColor" stroke-width="3"/><line x1="82" y1="50" x2="95" y2="50" stroke="currentColor" stroke-width="4"/><text x="4" y="44" font-size="10" fill="#94a3b8">A</text><text x="86" y="44" font-size="10" fill="#f43f5e">Y</text></svg>',
        "formula": "Boolean: Y = A' (NOT A)  |  Truth Table: 0 -> 1, 1 -> 0",
        "pinout_specs": "TTL 7404 Hex Inverter IC; CMOS 4049; Single input, single output",
        "english_desc": "Inverts the input signal: changes HIGH (1) to LOW (0), and LOW (0) to HIGH (1).",
        "tamil": {
            "name": "மறுப்பு வாசல் / இன்வெர்ட்டர் (NOT Gate / Inverter)",
            "explanation": "உள்ளீட்டை தலைகீழாக மாற்றும் வாயில். உள்ளீடு 1 ஆக இருந்தால் வெளியீடு 0 ஆகும்; உள்ளீடு 0 ஆக இருந்தால் வெளியீடு 1 ஆகும்.",
            "application": "தானியங்கி இரவு விளக்கு (பகலில் வெளிச்சம் = 1 -> விளக்கு அணைக்கப்படும் = 0)."
        },
        "hindi": {
            "name": "नॉट गेट (NOT Gate)",
            "explanation": "इनपुट को उलटने वाला गेट (0 को 1 और 1 को 0 बनाता है)।",
            "application": "स्वचालित नाइट लाइट और डिजिटल स्विच।"
        },
        "telugu": {
            "name": "నాట్ గేట్ (NOT Gate)",
            "explanation": "ఇన్‌పుట్‌ను వ్యతిరేకంగా మార్చే గేట్ (0 ని 1 గా, 1 ని 0 గా చేస్తుంది).",
            "application": "ఇన్వర్టర్లు."
        }
    },
    {
        "id": "nand_gate",
        "name": "NAND Gate (Universal Gate)",
        "category": "logic_gates",
        "category_name": "Digital Logic Gates",
        "nec_code": "IEEE Std 91-1984 / ANSI Y32.14 / IEC 60617-12",
        "ieee_code": "IEEE Universal Gate Standard",
        "symbol_type": "Digital Schematic",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><line x1="8" y1="35" x2="28" y2="35" stroke="currentColor" stroke-width="4"/><line x1="8" y1="65" x2="28" y2="65" stroke="currentColor" stroke-width="4"/><path d="M 28 20 L 52 20 A 30 30 0 0 1 52 80 L 28 80 Z" fill="rgba(245,158,11,0.2)" stroke="currentColor" stroke-width="4"/><circle cx="76" cy="50" r="5" fill="none" stroke="currentColor" stroke-width="3"/><line x1="82" y1="50" x2="95" y2="50" stroke="currentColor" stroke-width="4"/><text x="4" y="38" font-size="10" fill="#94a3b8">A</text><text x="4" y="68" font-size="10" fill="#94a3b8">B</text><text x="86" y="44" font-size="10" fill="#f59e0b">Y</text></svg>',
        "formula": "Boolean: Y = (A * B)'  |  Universal Gate (Can construct any logic circuit)",
        "pinout_specs": "TTL 7400 Quad 2-Input NAND IC; Flash memory cells are based on NAND architecture",
        "english_desc": "Outputs LOW (0) only when all inputs are HIGH (1). It is a universal gate capable of implementing any boolean function.",
        "tamil": {
            "name": "உலகளாவிய வாசல் (NAND Gate)",
            "explanation": "AND வாசலின் தலைகீழ் வடிவம். அனைத்து உள்ளீடுகளும் 1 ஆக இருந்தால் மட்டுமே வெளியீடு 0 ஆகும். இதை மட்டும் பயன்படுத்தி அனைத்து லாஜிக் சர்க்யூட்களையும் உருவாக்க முடியும் என்பதால் இது 'உலகளாவிய வாசல்' (Universal Gate) எனப்படுகிறது.",
            "application": "கணினி SSD மற்றும் பென் டிரைவ் நினைவகம் (NAND Flash Memory)."
        },
        "hindi": {
            "name": "नैंड गेट (NAND Gate)",
            "explanation": "सार्वभौमिक गेट जिससे अन्य सभी डिजिटल गेट बनाए जा सकते हैं।",
            "application": "एसएसडी और फ्लैश मेमोरी चिप्स।"
        },
        "telugu": {
            "name": "నాండ్ గేట్ (NAND Gate)",
            "explanation": "యూనివర్సల్ గేట్. దీనితో అన్ని రకాల సర్క్యూట్లను నిర్మించవచ్చు.",
            "application": "మెమరీ చిప్స్."
        }
    },
    {
        "id": "xor_gate",
        "name": "XOR Gate (Exclusive OR)",
        "category": "logic_gates",
        "category_name": "Digital Logic Gates",
        "nec_code": "IEEE Std 91-1984 / ANSI Y32.14 / IEC 60617-12",
        "ieee_code": "IEEE Distinctive Shape Logic Symbol",
        "symbol_type": "Digital Schematic",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><path d="M 18 20 Q 32 50 18 80" fill="none" stroke="currentColor" stroke-width="4"/><line x1="5" y1="35" x2="24" y2="35" stroke="currentColor" stroke-width="4"/><line x1="5" y1="65" x2="24" y2="65" stroke="currentColor" stroke-width="4"/><path d="M 28 20 Q 42 50 28 80 Q 60 78 82 50 Q 60 22 28 20 Z" fill="rgba(99,102,241,0.2)" stroke="currentColor" stroke-width="4"/><line x1="82" y1="50" x2="95" y2="50" stroke="currentColor" stroke-width="4"/><text x="86" y="44" font-size="10" fill="#818cf8">Y</text></svg>',
        "formula": "Boolean: Y = A ⊕ B = A'B + AB'  |  Odd parity detector: 0^0=0, 0^1=1, 1^0=1, 1^1=0",
        "pinout_specs": "TTL 7486 Quad 2-Input XOR IC; Core of Half Adder / Full Adder circuits",
        "english_desc": "Outputs HIGH (1) when inputs are different (one HIGH and one LOW). Outputs LOW (0) when both inputs are identical.",
        "tamil": {
            "name": "தனித்த அல்லது வாசல் (XOR Gate)",
            "explanation": "இரண்டு உள்ளீடுகளும் வெவ்வேறாக இருக்கும்போது (0,1 அல்லது 1,0) வெளியீடு 1 ஆக இருக்கும். இரண்டும் சமமாக இருந்தால் (0,0 அல்லது 1,1) வெளியீடு 0 ஆகும்.",
            "application": "பைனரி கூட்டல் சுற்றுகள் (Binary Adders), குறியாக்கவியல் (Cryptography / Data Encryption)."
        },
        "hindi": {
            "name": "एक्स-ऑर गेट (XOR Gate)",
            "explanation": "जब दोनों इनपुट अलग हों तो आउटपुट 1 देने वाला गेट। इसका उपयोग बाइनरी जोड़ने में होता है।",
            "application": "बाइनरी एडर और डेटा एन्क्रिप्शन।"
        },
        "telugu": {
            "name": "ఎక్స్-ఆర్ గేట్ (XOR Gate)",
            "explanation": "ఇన్‌పుట్‌లు భిన్నంగా ఉన్నప్పుడు 1 ఇచ్చే లాజిక్ గేట్.",
            "application": "బైనరీ సంకలనం."
        }
    },

    # -------------------------------------------------------------------------
    # CATEGORY: INSTRUMENTATION & SENSORS
    # -------------------------------------------------------------------------
    {
        "id": "voltmeter",
        "name": "Voltmeter",
        "category": "instrumentation",
        "category_name": "Sensors & Instrumentation",
        "nec_code": "IEEE Std 315 Sec. 10.1 / IEC 60617-08-02-01",
        "ieee_code": "ANSI / IEEE Std 315 Indicating Meter",
        "symbol_type": "Schematic",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><circle cx="50" cy="50" r="34" fill="none" stroke="currentColor" stroke-width="4"/><text x="50" y="58" font-size="26" font-weight="bold" fill="#06b6d4" text-anchor="middle">V</text><line x1="16" y1="50" x2="4" y2="50" stroke="currentColor" stroke-width="4"/><line x1="84" y1="50" x2="96" y2="50" stroke="currentColor" stroke-width="4"/></svg>',
        "formula": "Ideal Voltmeter: R_in = Infinity (Must be connected in PARALLEL)",
        "pinout_specs": "Positive (+) Red lead, Negative (-) Black COM lead; Input Impedance >= 10 M-Ohms on digital meters",
        "english_desc": "An instrument used for measuring electrical potential difference between two points in an electric circuit. Always connected in parallel across the component.",
        "tamil": {
            "name": "மின்னழுத்தமானி (Voltmeter)",
            "explanation": "மின்சுற்றில் உள்ள இரண்டு புள்ளிகளுக்கு இடையே உள்ள மின்னழுத்த வேறுபாட்டை (Voltage) அளவிடும் கருவி. இது எப்போதும் சுற்றில் பக்க இணைப்பில் (Parallel) மட்டுமே இணைக்கப்பட வேண்டும்.",
            "application": "பேட்டரி மற்றும் வீட்டின் 230V மெயின் மின்னழுத்தத்தை சரிபார்த்தல்."
        },
        "hindi": {
            "name": "वोल्टमीटर (Voltmeter)",
            "explanation": "सर्किट में किन्हीं दो बिंदुओं के बीच वोल्टेज मापने वाला उपकरण। इसे हमेशा समानांतर (Parallel) में जोड़ा जाता है।",
            "application": "वोल्टेज जांच और मल्टीमीटर।"
        },
        "telugu": {
            "name": "వోల్ట్‌మీటర్ (Voltmeter)",
            "explanation": "రెండు బిందువుల మధ్య వోల్టేజ్‌ను కొలిచే పరికరం. సమాంతరంగా కలుపుతారు.",
            "application": "వోల్టేజ్ కొలత."
        }
    },
    {
        "id": "ammeter",
        "name": "Ammeter",
        "category": "instrumentation",
        "category_name": "Sensors & Instrumentation",
        "nec_code": "IEEE Std 315 Sec. 10.2 / IEC 60617-08-02-02",
        "ieee_code": "ANSI / IEEE Std 315 Indicating Meter",
        "symbol_type": "Schematic",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><circle cx="50" cy="50" r="34" fill="none" stroke="currentColor" stroke-width="4"/><text x="50" y="58" font-size="26" font-weight="bold" fill="#f59e0b" text-anchor="middle">A</text><line x1="16" y1="50" x2="4" y2="50" stroke="currentColor" stroke-width="4"/><line x1="84" y1="50" x2="96" y2="50" stroke="currentColor" stroke-width="4"/></svg>',
        "formula": "Ideal Ammeter: R_internal ≈ 0 Ohms (Must be connected in SERIES)",
        "pinout_specs": "Series loop connection; Shunt resistor used for high current ranges (e.g., 0-50A)",
        "english_desc": "An instrument used to measure electric current in a circuit in Amperes. Must always be connected in series with the load to measure current passing through.",
        "tamil": {
            "name": "மின்னோட்டமானி (Ammeter)",
            "explanation": "மின்சுற்றில் பாயும் மின்னோட்டத்தின் அளவை (Current in Amperes) அளவிடும் கருவி. இது சுற்றின் தொடரிணைப்பில் (Series) மட்டுமே இணைக்கப்பட வேண்டும். பக்க இணைப்பில் இணைத்தால் ஷார்ட் சர்க்யூட் ஏற்படும்!",
            "application": "மோட்டார் எடுக்கும் மின்னோட்டம் (Amps) மற்றும் சோலார் பேனல் அவுட்புட் சோதனை."
        },
        "hindi": {
            "name": "एमीटर (Ammeter)",
            "explanation": "सर्किट में करंट (एम्पीयर) मापने वाला यंत्र। इसे हमेशा श्रेणी (Series) में जोड़ा जाता है।",
            "application": "लोड करंट मापन।"
        },
        "telugu": {
            "name": "అమ్మీటర్ (Ammeter)",
            "explanation": "కరెంట్‌ను (ఆంపియర్లు) కొలిచే పరికరం. శ్రేణిలో (సిరీస్) కలుపుతారు.",
            "application": "కరెంట్ కొలత."
        }
    },
    {
        "id": "relay",
        "name": "Electromechanical Relay",
        "category": "instrumentation",
        "category_name": "Sensors & Instrumentation",
        "nec_code": "IEEE Std 315 Sec. 13.3 / IEC 60617-07-13-01",
        "ieee_code": "ANSI / IEEE Std 315 SPDT Relay Symbol",
        "symbol_type": "Schematic",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><rect x="15" y="25" width="25" height="50" fill="none" stroke="currentColor" stroke-width="3"/><path d="M 27 25 L 27 75" stroke="#f59e0b" stroke-width="4"/><line x1="5" y1="25" x2="15" y2="25" stroke="currentColor" stroke-width="3"/><line x1="5" y1="75" x2="15" y2="75" stroke="currentColor" stroke-width="3"/><line x1="55" y1="50" x2="72" y2="35" stroke="currentColor" stroke-width="4"/><circle cx="55" cy="50" r="4" fill="currentColor"/><circle cx="75" cy="30" r="4" fill="none" stroke="currentColor" stroke-width="3"/><circle cx="75" cy="70" r="4" fill="currentColor"/><line x1="78" y1="30" x2="95" y2="30" stroke="currentColor" stroke-width="3"/><line x1="78" y1="70" x2="95" y2="70" stroke="currentColor" stroke-width="3"/><text x="80" y="22" font-size="10" fill="#94a3b8">NC</text><text x="80" y="85" font-size="10" fill="#94a3b8">NO</text></svg>',
        "formula": "Contact Rating: e.g., 250VAC 10A; Coil Voltage: 5VDC / 12VDC / 24VDC",
        "pinout_specs": "Coil (Pins 1 & 2), Common (COM), Normally Open (NO), Normally Closed (NC)",
        "english_desc": "An electrically operated switch. Uses an electromagnet to mechanically operate a switch mechanism, allowing a low-power microcontroller signal to control a high-power AC load safely.",
        "tamil": {
            "name": "மின்காந்த ரிலே (Electromechanical Relay)",
            "explanation": "மின்காந்தத்தால் இயங்கும் சுவிட்ச். சிறிய 5V சிக்னலைக் கொண்டு (எ.கா: ஆர்டுயினோ / மைக்ரோகண்ட்ரோலர்) பெரிய 230V வீட்டு விளக்குகள் அல்லது மோட்டார்களை பாதுகாப்பாக கட்டுப்படுத்த உதவுகிறது.",
            "application": "வீட்டு ஆட்டோமேஷன், வாகனங்களின் ஹாரன் மற்றும் ஸ்டார்டர் மோட்டார் சுற்றுகள்."
        },
        "hindi": {
            "name": "रिले (Electromechanical Relay)",
            "explanation": "कम वोल्टेज सिग्नल से उच्च वोल्टेज उपकरणों को नियंत्रित करने वाला विद्युत स्विच।",
            "application": "होम ऑटोमेशन और मोटर स्टार्टर।"
        },
        "telugu": {
            "name": "రిలే (Relay)",
            "explanation": "తక్కువ వోల్టేజ్ ద్వారా ఎక్కువ విద్యుత్ లోడ్లను ఆన్/ఆఫ్ చేసే స్విచ్.",
            "application": "ఆటోమేషన్ మరియు మోటార్ కంట్రోల్."
        }
    },

    # -------------------------------------------------------------------------
    # CATEGORY: MECHANICAL & PIPING (P&ID ISA-5.1)
    # -------------------------------------------------------------------------
    {
        "id": "centrifugal_pump",
        "name": "Centrifugal Pump",
        "category": "mechanical_pid",
        "category_name": "Mechanical & Piping (P&ID)",
        "nec_code": "ISA Standard 5.1 / ISO 14617 / ASME",
        "ieee_code": "Piping & Instrumentation Diagram Symbol",
        "symbol_type": "P&ID Schematic",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><circle cx="50" cy="50" r="32" fill="none" stroke="currentColor" stroke-width="4"/><polygon points="35,32 68,50 35,68" fill="rgba(6,182,212,0.3)" stroke="currentColor" stroke-width="3"/><line x1="18" y1="50" x2="4" y2="50" stroke="currentColor" stroke-width="4"/><line x1="50" y1="18" x2="50" y2="4" stroke="currentColor" stroke-width="4"/></svg>',
        "formula": "Hydraulic Power: P_h = (Q * rho * g * H) / 1000  (kW)  |  Affinity Laws: Q proportional to N",
        "pinout_specs": "Suction Port (Horizontal in), Discharge Port (Vertical top out); Impeller RPM: 1450 / 2900 RPM",
        "english_desc": "A rotodynamic machine that uses a rotating impeller to convert rotational kinetic energy into the hydrodynamic energy of a fluid flow.",
        "tamil": {
            "name": "மையவிலக்கு விசையியக்கக்குழாய் (Centrifugal Pump)",
            "explanation": "சுழலும் இம்பெல்லர் (Impeller) மூலம் மையவிலக்கு விசையை உருவாக்கி நீரை அல்லது திரவங்களை உறிஞ்சி அதிக அழுத்தத்துடன் வெளியேற்றும் இயந்திரம்.",
            "application": "விவசாய நீர்ப்பாசனம், வீடுகளின் மேல்நிலை தொட்டிக்கு தண்ணீர் ஏற்றுதல்."
        },
        "hindi": {
            "name": "सेंट्रीफ्यूगल पंप (Centrifugal Pump)",
            "explanation": "घूमने वाले पहिये (इम्पेलर) द्वारा तरल पदार्थ को ऊपर उठाने और प्रवाहित करने वाला पंप।",
            "application": "कृषि सिंचाई और जल आपूर्ति।"
        },
        "telugu": {
            "name": "సెంట్రిఫ్యూగల్ పంప్ (Centrifugal Pump)",
            "explanation": "భ్రమణ శక్తి ద్వారా నీటిని అధిక పీడనంతో పంపే పంపు.",
            "application": "వ్యవసాయం మరియు నీటి సరఫరా."
        }
    },
    {
        "id": "gate_valve",
        "name": "Gate Valve (Isolation Valve)",
        "category": "mechanical_pid",
        "category_name": "Mechanical & Piping (P&ID)",
        "nec_code": "ISA-5.1 / ANSI / ASME B16.34",
        "ieee_code": "P&ID Process Piping Symbol",
        "symbol_type": "P&ID Schematic",
        "svg": '<svg viewBox="0 0 100 100" class="eng-svg"><polygon points="15,30 50,50 15,70" fill="rgba(99,102,241,0.2)" stroke="currentColor" stroke-width="4"/><polygon points="85,30 50,50 85,70" fill="rgba(99,102,241,0.2)" stroke="currentColor" stroke-width="4"/><line x1="50" y1="50" x2="50" y2="20" stroke="currentColor" stroke-width="4"/><line x1="38" y1="20" x2="62" y2="20" stroke="#f59e0b" stroke-width="5"/></svg>',
        "formula": "Fully Open / Closed Isolation only (Not for throttling / flow regulation)",
        "pinout_specs": "Flanged or Threaded ends; Pressure classes: Class 150, 300, 600",
        "english_desc": "A linear-motion valve used to completely start or stop fluid flow through a pipe. Has minimal pressure drop when fully open.",
        "tamil": {
            "name": "கேட் வால்வு / தடுப்பு அடைப்பான் (Gate Valve)",
            "explanation": "குழாயில் செல்லும் திரவத்தின் ஓட்டத்தை முழுமையாக திறக்கவும் (ON) அல்லது முழுமையாக நிறுத்தவும் (OFF) பயன்படும் தடுப்பு வால்வு. திறந்திருக்கும் போது மிகக் குறைந்த அழுத்த இழப்பு ஏற்படும்.",
            "application": "நகராட்சி குடிநீர் விநியோக பிரதான குழாய்கள், பெட்ரோலிய குழாய்கள்."
        },
        "hindi": {
            "name": "गेट वाल्व (Gate Valve)",
            "explanation": "पाइपलाइन में तरल के प्रवाह को पूरी तरह चालू या बंद करने वाला वाल्व।",
            "application": "पानी की मुख्य लाइन और तेल पाइपलाइन।"
        },
        "telugu": {
            "name": "గేట్ వాల్వ్ (Gate Valve)",
            "explanation": "పైపులో నీటి ప్రవాహాన్ని పూర్తిగా ఆపడానికి లేదా తెరవడానికి ఉపయోగించే వాల్వ్.",
            "application": "ముఖ్య నీటి పైపులైన్లు."
        }
    }
]

# Lookup dictionary for fast search
SYMBOLS_BY_ID = {s["id"]: s for s in ENGINEERING_SYMBOLS_DB}


# ============================================================================
# SYMBOL ANALYSIS & DECODER ENGINE
# ============================================================================
def get_all_engineering_symbols(category: Optional[str] = None) -> List[Dict[str, Any]]:
    """Returns list of engineering symbols optionally filtered by category."""
    if not category or category.lower() == "all":
        return ENGINEERING_SYMBOLS_DB
    cat_lower = category.lower()
    return [s for s in ENGINEERING_SYMBOLS_DB if s["category"].lower() == cat_lower]


def analyze_uploaded_symbol_or_query(
    query_or_tag: str,
    target_language: str = "Tamil"
) -> Dict[str, Any]:
    """
    Analyzes an uploaded symbol identifier, query, or schematic tag.
    Returns matching symbol details, NEC standards, pinout specifications,
    formula calculations, and vernacular explanation in student's mother tongue.
    """
    clean = (query_or_tag or "").strip().lower()

    # Search keyword matchers
    matched_symbol = None

    # Check exact ID match first
    if clean in SYMBOLS_BY_ID:
        matched_symbol = SYMBOLS_BY_ID[clean]

    # Keyword heuristics
    if not matched_symbol:
        for sym in ENGINEERING_SYMBOLS_DB:
            name_lower = sym["name"].lower()
            id_lower = sym["id"].lower()
            nec_lower = sym["nec_code"].lower()
            if clean in name_lower or clean in id_lower or any(w in clean for w in name_lower.split()):
                matched_symbol = sym
                break

    # If still not found, check partial category or common synonyms
    if not matched_symbol:
        synonyms = {
            "ground": "earth_ground",
            "earthing": "earth_ground",
            "mcb": "circuit_breaker",
            "breaker": "circuit_breaker",
            "switch": "single_pole_switch",
            "socket": "duplex_receptacle",
            "plug": "duplex_receptacle",
            "gfi": "gfci_receptacle",
            "gfci": "gfci_receptacle",
            "board": "panelboard",
            "panel": "panelboard",
            "xformer": "transformer",
            "trans": "transformer",
            "motor": "induction_motor",
            "res": "resistor",
            "ohm": "resistor",
            "cap": "capacitor_polarized",
            "condenser": "capacitor_polarized",
            "coil": "inductor",
            "choke": "inductor",
            "diode": "pn_diode",
            "led": "led",
            "transistor": "npn_transistor",
            "bjt": "npn_transistor",
            "opamp": "opamp",
            "741": "opamp",
            "and": "and_gate",
            "or": "or_gate",
            "not": "not_gate",
            "invert": "not_gate",
            "nand": "nand_gate",
            "xor": "xor_gate",
            "volt": "voltmeter",
            "amp": "ammeter",
            "relay": "relay",
            "pump": "centrifugal_pump",
            "valve": "gate_valve"
        }
        for syn_k, sym_id in synonyms.items():
            if syn_k in clean and sym_id in SYMBOLS_BY_ID:
                matched_symbol = SYMBOLS_BY_ID[sym_id]
                break

    # Fallback to Earth Ground as demonstrative standard if no match
    if not matched_symbol:
        matched_symbol = SYMBOLS_BY_ID["earth_ground"]

    # Vernacular localized presentation
    lang_key = target_language.lower()
    vernacular_info = matched_symbol.get("tamil", {})
    if "hindi" in lang_key:
        vernacular_info = matched_symbol.get("hindi", vernacular_info)
    elif "telugu" in lang_key:
        vernacular_info = matched_symbol.get("telugu", vernacular_info)

    return {
        "found": True,
        "query": query_or_tag,
        "symbol": matched_symbol,
        "target_language": target_language,
        "vernacular_title": vernacular_info.get("name", matched_symbol["name"]),
        "vernacular_explanation": vernacular_info.get("explanation", matched_symbol["english_desc"]),
        "vernacular_application": vernacular_info.get("application", ""),
        "nec_compliance": {
            "standard_code": matched_symbol["nec_code"],
            "ieee_code": matched_symbol["ieee_code"],
            "formula": matched_symbol["formula"],
            "pinout": matched_symbol["pinout_specs"]
        }
    }


# ============================================================================
# ENGINEERING FORMULA CALCULATOR
# ============================================================================
def calculate_engineering_formula(
    formula_type: str,
    params: Dict[str, float]
) -> Dict[str, Any]:
    """
    Solves foundational electrical and electronics engineering calculations:
    - ohms_law: V = I * R, P = V * I
    - resonance: f_0 = 1 / (2 * pi * sqrt(L * C))
    - voltage_divider: V_out = V_in * (R2 / (R1 + R2))
    - transformer_ratio: V_s = V_p * (N_s / N_p)
    - inductive_reactance: X_L = 2 * pi * f * L
    - capacitive_reactance: X_C = 1 / (2 * pi * f * C)
    """
    f_type = (formula_type or "").lower().strip()

    try:
        if f_type == "ohms_law":
            v = params.get("voltage")
            i = params.get("current")
            r = params.get("resistance")

            if v is not None and i is not None and i != 0:
                calc_r = v / i
                calc_p = v * i
                return {
                    "formula": "Ohm's Law (V = I * R)",
                    "result": f"Resistance R = {round(calc_r, 4)} Ω | Power P = {round(calc_p, 4)} W",
                    "steps": [f"R = V / I = {v} / {i} = {round(calc_r, 4)} Ohms", f"P = V * I = {v} * {i} = {round(calc_p, 4)} Watts"]
                }
            elif i is not None and r is not None:
                calc_v = i * r
                calc_p = (i ** 2) * r
                return {
                    "formula": "Ohm's Law (V = I * R)",
                    "result": f"Voltage V = {round(calc_v, 4)} V | Power P = {round(calc_p, 4)} W",
                    "steps": [f"V = I * R = {i} * {r} = {round(calc_v, 4)} Volts", f"P = I² * R = {round(calc_p, 4)} Watts"]
                }
            elif v is not None and r is not None and r != 0:
                calc_i = v / r
                calc_p = (v ** 2) / r
                return {
                    "formula": "Ohm's Law (V = I * R)",
                    "result": f"Current I = {round(calc_i, 4)} A | Power P = {round(calc_p, 4)} W",
                    "steps": [f"I = V / R = {v} / {r} = {round(calc_i, 4)} Amperes", f"P = V² / R = {round(calc_p, 4)} Watts"]
                }

        elif f_type == "resonance":
            l = params.get("inductance", 0.001)  # in Henry
            c = params.get("capacitance", 0.000001)  # in Farad
            if l <= 0 or c <= 0:
                return {"error": "L and C must be positive non-zero numbers"}
            f0 = 1.0 / (2.0 * math.pi * math.sqrt(l * c))
            return {
                "formula": "LC Resonant Frequency: f₀ = 1 / (2π√(LC))",
                "result": f"Resonant Frequency f₀ = {round(f0, 2)} Hz ({round(f0/1000, 3)} kHz)",
                "steps": [
                    f"√(L × C) = √({l} × {c}) = {math.sqrt(l * c):.6e}",
                    f"2π√(LC) = {2 * math.pi * math.sqrt(l * c):.6e}",
                    f"f₀ = 1 / {2 * math.pi * math.sqrt(l * c):.6e} = {round(f0, 2)} Hz"
                ]
            }

        elif f_type == "voltage_divider":
            vin = params.get("vin", 12.0)
            r1 = params.get("r1", 1000.0)
            r2 = params.get("r2", 2000.0)
            if (r1 + r2) == 0:
                return {"error": "Sum of R1 and R2 cannot be zero"}
            vout = vin * (r2 / (r1 + r2))
            return {
                "formula": "Voltage Divider: V_out = V_in × (R₂ / (R₁ + R₂))",
                "result": f"Output Voltage V_out = {round(vout, 4)} V",
                "steps": [
                    f"Total Resistance R_total = {r1} + {r2} = {r1 + r2} Ω",
                    f"Divider Ratio = {r2} / {r1 + r2} = {round(r2 / (r1 + r2), 4)}",
                    f"V_out = {vin} × {round(r2 / (r1 + r2), 4)} = {round(vout, 4)} V"
                ]
            }

        elif f_type == "transformer_ratio":
            vp = params.get("vp", 230.0)
            np = params.get("np", 1000.0)
            ns = params.get("ns", 100.0)
            if np == 0:
                return {"error": "Primary turns cannot be zero"}
            vs = vp * (ns / np)
            turns_ratio = np / ns
            return {
                "formula": "Transformer Turns Ratio: V_s = V_p × (N_s / N_p)",
                "result": f"Secondary Voltage V_s = {round(vs, 2)} V (Turns Ratio N_p:N_s = {round(turns_ratio, 2)}:1)",
                "steps": [
                    f"Turns Ratio N_s / N_p = {ns} / {np} = {round(ns / np, 4)}",
                    f"V_s = {vp} × {round(ns / np, 4)} = {round(vs, 2)} V"
                ]
            }

    except Exception as e:
        return {"error": str(e)}

    return {"error": "Unsupported calculation parameters"}
