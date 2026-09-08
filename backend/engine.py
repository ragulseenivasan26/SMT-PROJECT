"""
AI-Powered Vernacular Pedagogy Engine & Multi-Tier Translation Hub
National Engineering College (Autonomous), Kovilpatti
SMT CO2 Team | 2024-2028 Batch
Unified with backend/models/translator.py for 51 supported languages and offline resilience.
"""

import os
import re
from typing import Dict, List, Any

# Import modular translation engine
try:
    from models.translator import (
        translate_text as _mod_translate,
        SUPPORTED_LANGUAGES,
        get_language_code,
        extract_key_vocabulary,
        generate_explanation as _mod_explain
    )
except ImportError:
    from .models.translator import (
        translate_text as _mod_translate,
        SUPPORTED_LANGUAGES,
        get_language_code,
        extract_key_vocabulary,
        generate_explanation as _mod_explain
    )

# 1. Complete Language Code Map (51 Languages)
LANG_CODES: Dict[str, str] = {
    lang["name"]: lang["code"] for lang in SUPPORTED_LANGUAGES
}

# 2. Comprehensive STEM, Engineering & Primary Educational Lexicon
DEMO: Dict[str, Dict[str, str]] = {
    # Engineering & Technology
    "computer": {
        "Tamil": "கணினி", "Hindi": "संगणक / कंप्यूटर", "Telugu": "కంప్యూటర్",
        "Malayalam": "കമ്പ്യൂട്ടർ", "Kannada": "ಗಣಕಯಂತ್ರ"
    },
    "algorithm": {
        "Tamil": "படிமுறைத் தீர்வு (அல்காரிதம்)", "Hindi": "कलन विधि (एल्गोरिदम)", "Telugu": "అల్గారిథమ్",
        "Malayalam": "അൽഗോരിതം", "Kannada": "ಕ್ರಮಾವಳಿ"
    },
    "energy": {
        "Tamil": "ஆற்றல் (எனர்ஜி)", "Hindi": "ऊर्जा", "Telugu": "శక్తి",
        "Malayalam": "ഊർജ്ജം", "Kannada": "ಶಕ್ತಿ"
    },
    "electricity": {
        "Tamil": "மின்சாரம்", "Hindi": "विद्युत / बिजली", "Telugu": "విద్యుత్",
        "Malayalam": "വൈദ്യുതി", "Kannada": "ವಿದ್ಯುತ್"
    },
    "force": {
        "Tamil": "விசை", "Hindi": "बल", "Telugu": "బలం",
        "Malayalam": "ബലം", "Kannada": "ಬಲ"
    },
    "gravity": {
        "Tamil": "ஈர்ப்பு விசை", "Hindi": "गुरुत्वाकर्षण", "Telugu": "గురుత్వాకర్షణ",
        "Malayalam": "ഗുരുത്വാകർഷണം", "Kannada": "ಗುರುತ್ವಾಕರ್ಷಣೆ"
    },
    "atom": {
        "Tamil": "அணு", "Hindi": "परमाणु", "Telugu": "పరమాణువు",
        "Malayalam": "അണു", "Kannada": "ಪರಮಾಣು"
    },
    "molecule": {
        "Tamil": "மூலக்கூறு", "Hindi": "अणु", "Telugu": "అణువు",
        "Malayalam": "തന്മാത്ര", "Kannada": "ಅಣು"
    },
    "oxygen": {
        "Tamil": "ஆக்ஸிஜன் (உயிர்வளி)", "Hindi": "ऑक्सीजन", "Telugu": "ఆక్సిజన్",
        "Malayalam": "ഓക്സിജൻ", "Kannada": "ಆಮ್ಲಜನಕ"
    },
    "water": {
        "Tamil": "தண்ணீர்", "Hindi": "पानी", "Telugu": "నీరు",
        "Malayalam": "വെള്ളം", "Kannada": "ನೀರು"
    },
    "sun": {
        "Tamil": "சூரியன்", "Hindi": "सूर्य", "Telugu": "సూర్యుడు",
        "Malayalam": "സൂര്യൻ", "Kannada": "ಸೂರ್ಯ"
    },
    "tree": {
        "Tamil": "மரம்", "Hindi": "पेड़", "Telugu": "చెట్టు",
        "Malayalam": "മരം", "Kannada": "ಮರ"
    },
    "school": {
        "Tamil": "பள்ளி", "Hindi": "विद्यालय", "Telugu": "పాఠశాల",
        "Malayalam": "സ്കൂൾ", "Kannada": "ಶಾಲೆ"
    },
    "book": {
        "Tamil": "புத்தகம்", "Hindi": "किताब", "Telugu": "పుస్తకం",
        "Malayalam": "പുസ്തകം", "Kannada": "ಪುಸ್ತಕ"
    },
    "rain": {
        "Tamil": "மழை", "Hindi": "बारिश", "Telugu": "వర్షం",
        "Malayalam": "മഴ", "Kannada": "ಮಳೆ"
    },
    "earth": {
        "Tamil": "பூமி", "Hindi": "पृथ्वी", "Telugu": "భూమి",
        "Malayalam": "ഭൂമി", "Kannada": "ಭೂಮಿ"
    },
    "moon": {
        "Tamil": "நிலா", "Hindi": "चंद्रमा", "Telugu": "చంద్రుడు",
        "Malayalam": "ചന്ദ്രൻ", "Kannada": "ಚಂದ್ರ"
    },
    "star": {
        "Tamil": "நட்சத்திரம்", "Hindi": "तारा", "Telugu": "నక్షత్రం",
        "Malayalam": "നക്ഷത്രം", "Kannada": "ನಕ್ಷತ್ರ"
    },
    "plant": {
        "Tamil": "செடி", "Hindi": "पौधा", "Telugu": "మొక్క",
        "Malayalam": "ചെടി", "Kannada": "ಸಸ್ಯ"
    },
    "flower": {
        "Tamil": "பூ", "Hindi": "फूल", "Telugu": "పువ్వు",
        "Malayalam": "പൂവ്", "Kannada": "ಹೂವು"
    },
    "fruit": {
        "Tamil": "பழம்", "Hindi": "फल", "Telugu": "పండు",
        "Malayalam": "പഴം", "Kannada": "ಹಣ್ಣು"
    },
    "leaf": {
        "Tamil": "இலை", "Hindi": "पत्ता", "Telugu": "ఆకు",
        "Malayalam": "இல", "Kannada": "ಎಲೆ"
    },
    "air": {
        "Tamil": "காற்று", "Hindi": "हवा", "Telugu": "గాలి",
        "Malayalam": "കാറ്റ്", "Kannada": "ಗಾಳಿ"
    },
    "teacher": {
        "Tamil": "ஆசிரியர்", "Hindi": "शिक्षक", "Telugu": "ఉపాధ్యాయుడు",
        "Malayalam": "അധ്യാപകൻ", "Kannada": "ಶಿಕ್ಷಕ"
    },
    "student": {
        "Tamil": "மாணவர்", "Hindi": "छात्र", "Telugu": "విద్యార్థి",
        "Malayalam": "വിദ്യാർത്ഥി", "Kannada": "ವಿದ್ಯಾರ್ಥಿ"
    },
    "animal": {
        "Tamil": "விலங்கு", "Hindi": "जानवर", "Telugu": "జంతువు",
        "Malayalam": "മൃഗം", "Kannada": "ಪ್ರಾಣಿ"
    },
    "bird": {
        "Tamil": "பறவை", "Hindi": "पक्षी", "Telugu": "పక్షి",
        "Malayalam": "പക്ഷി", "Kannada": "ಹಕ್ಕಿ"
    },
    "river": {
        "Tamil": "ஆறு", "Hindi": "नदी", "Telugu": "నది",
        "Malayalam": "നദി", "Kannada": "ನದಿ"
    },
    "light": {
        "Tamil": "ஒளி", "Hindi": "प्रकाश", "Telugu": "వెలుగు",
        "Malayalam": "വെളിച്ചം", "Kannada": "ಬೆಳಕು"
    },
    "food": {
        "Tamil": "உணவு", "Hindi": "भोजन", "Telugu": "ఆహారం",
        "Malayalam": "ഭക്ഷണം", "Kannada": "ಆಹಾರ"
    },
    "the sun gives us light": {
        "Tamil": "சூரியன் நமக்கு ஒளியை வழங்குகிறது",
        "Hindi": "सूर्य हमें प्रकाश देता है",
        "Telugu": "సూర్యుడు మనకు వెలుతురును ఇస్తాడు",
        "Malayalam": "സൂര്യൻ നമുക്ക് പ്രകാശം നൽകുന്നു",
        "Kannada": "ಸೂರ್ಯನು ನಮಗೆ ಬೆಳಕನ್ನು ನೀಡುತ್ತಾನೆ"
    },
    "water is important for life": {
        "Tamil": "நீர் வாழ்விற்கு மிகவும் முக்கியமானது",
        "Hindi": "जल जीवन के लिए महत्वपूर्ण है",
        "Telugu": "జీవితానికి నీరు చాలా ముఖ్యం",
        "Malayalam": "ജീവന് ജലം വളരെ പ്രധാനമാണ്",
        "Kannada": "ಜೀವನಕ್ಕೆ ನೀರು ಬಹಳ ಮುಖ್ಯವಾಗಿದೆ"
    },
    "plants need sunlight and water": {
        "Tamil": "செடிகளுக்கு சூரிய ஒளியும் தண்ணீரும் தேவை",
        "Hindi": "पौधों को धूप और पानी की आवश्यकता होती है",
        "Telugu": "మొక్కలకు సూర్యకాంతి మరియు నీరు అవసరం",
        "Malayalam": "ചെടികൾക്ക് സൂര്യപ്രകാശവും വെള്ളവും ആവശ്യമാണ്",
        "Kannada": "ಸಸ್ಯಗಳಿಗೆ ಸೂರ್ಯನ ಬೆಳಕು ಮತ್ತು ನೀರು ಬೇಕು"
    },
    "trees give us oxygen": {
        "Tamil": "மரங்கள் நமக்கு ஆக்ஸிஜனை தருகின்றன",
        "Hindi": "पेड़ हमें ऑक्सीजन देते हैं",
        "Telugu": "చెట్లు మనకు ఆక్సిజన్ ఇస్తాయి",
        "Malayalam": "മരങ്ങൾ നമുക്ക് ഓക്സിജൻ നൽകുന്നു",
        "Kannada": "ಮರಗಳು ನಮಗೆ ಆಮ್ಲಜನಕವನ್ನು ನೀಡುತ್ತವೆ"
    }
}

# 3. Curated Engineering & Primary STEM Topics
TOPIC_KNOWLEDGE: Dict[str, Dict[str, Dict[str, Any]]] = {
    "water cycle": {
        "Tamil": {
            "title": "நீர் சுழற்சி (Water Cycle)",
            "intro": "பூமியில் உள்ள தண்ணீர் ஆவியாகி மேகமாகி மீண்டும் மழையாகப் பொழியும் தொடர் சுழற்சியே 'நீர் சுழற்சி' எனப்படும்.",
            "steps": [
                "1. ஆவியாதல் (Evaporation): சூரிய வெப்பத்தால் ஏரி, கடல் நீர் நீராவியாக மாறுகிறது.",
                "2. ஒடுக்கம் (Condensation): நீராவி மேலே சென்று குளிர்ந்து மேகங்களாக மாறுகிறது.",
                "3. மழைப்பொழிவு (Precipitation): மேகங்கள் குளிர்ந்து மழையாகப் பெய்கிறது.",
                "4. சேகரிப்பு (Collection): மழைநீர் ஆறுகளிலும் கடலிலும் மீண்டும் வந்து சேர்கிறது."
            ],
            "activity": "ஒரு கிண்ணத்தில் தண்ணீர் வைத்து வெயிலில் வைத்து அது எப்படி குறைகிறது என்பதைக் கவனியுங்கள்.",
            "explanation": "சூரியன் தண்ணீரை சூடாக்கி மேலே அனுப்புகிறது, வானில் அது குளிர்ந்து மழையாக பூமிக்கு திரும்புகிறது.",
            "example": "நாம் துணி காய வைக்கும் போது தண்ணீர் காற்றில் மறைந்து போவதைப் போன்றது இது."
        },
        "Hindi": {
            "title": "जल चक्र (Water Cycle)",
            "intro": "पृथ्वी पर पानी भाप बनकर बादल बनता है और फिर वर्षा के रूप में नीचे आता है, इसे 'जल चक्र' कहते हैं।",
            "steps": [
                "1. वाष्पीकरण: सूर्य की गर्मी से पानी भाप बनकर ऊपर उठता है।",
                "2. संघनन: भाप ऊपर जाकर ठंडी होकर बादल बनाती है।",
                "3. वर्षण: बादल घने होकर वर्षा के रूप में बरसते हैं।",
                "4. संग्रहण: बारिश का पानी नदियों और समुद्र में फिर से इकट्ठा होता है।"
            ],
            "activity": "एक बर्तन में थोड़ा पानी धूप में रखें और देखें कि वह कैसे कम होता है।",
            "explanation": "सूरज पानी को गर्म करके भाप बनाता है, वह ऊपर जाकर बादल बनता है और बारिश बनकर वापस आता है।",
            "example": "गीले कपड़े धूप में सूखते हैं क्योंकि पानी वाष्प बन जाता है।"
        },
        "Telugu": {
            "title": "నీటి చక్రం (Water Cycle)",
            "intro": "భూమిపై నీరు ఆవిరై మేఘాలుగా మారి మళ్లీ వర్షంగా కురిసే నిరంతర ప్రక్రియను 'నీటి చక్రం' అంటారు.",
            "steps": [
                "1. బాష్పీభవనం: సూర్యరశ్మి వల్ల నీరు ఆవిరై పైకి వెళ్తుంది.",
                "2. సాంద్రీకరణం: ఆవిరి చల్లబడి మేఘాలుగా మారుతుంది.",
                "3. వర్షపాతం: మేఘాలు చల్లబడి వర్షంలా కురుస్తాయి.",
                "4. సేకరణ: వర్షపు నీరు మళ్లీ నదులు, సముద్రాలలో చేరుతుంది."
            ],
            "activity": "ఒక గిన్నెలో నీరు పోసి ఎండలో ఉంచి, నీరు ఎలా ఆవిరవుతుందో పరిశీలించండి.",
            "explanation": "సూర్యుడు నీటిని ఆవిరి చేసి పైకి పంపుతాడు, అది మేఘమై చల్లబడి వర్షంగా మారుతుంది.",
            "example": "ఎండలో ఆరబెట్టిన బట్టలు ఆరిపోవడం కూడా బాష్పీభవనమే."
        },
        "Malayalam": {
            "title": "ജലചക്രം (Water Cycle)",
            "intro": "ഭൂമിയിലെ വെള്ളം നീരാവിയായി മേഘമായി വീണ്ടും മഴയായി പെയ്യുന്ന പ്രക്രിയയാണ് 'ജലചക്രം'.",
            "steps": [
                "1. ബാഷ്പീകരണം: സൂര്യന്റെ ചൂടേറ്റ് വെള്ളം നീരാവിയായി മാറുന്നു.",
                "2. ഘനീഭവനം: നീരാവി മുകളിലേക്ക് ഉയർന്ന് തണുത്ത് മേഘങ്ങളാകുന്നു.",
                "3. വർഷണം: മേഘങ്ങൾ തണുത്ത് മഴയായി പെയ്യുന്നു.",
                "4. ശേഖരണം: മഴവെള്ളം നദികളിലേക്കും കടലുകളിലേക്കും തിരിച്ചെത്തുന്നു."
            ],
            "activity": "ഒരു പാത്രത്തിൽ വെള്ളമെടുത്ത് വെയിലത്ത് വെച്ച് അത് എങ്ങനെ കുറയുന്നു എന്ന് നിരീക്ഷിക്കുക.",
            "explanation": "സൂര്യൻ വെള്ളത്തെ നീരാവിയാക്കി ആകാശത്തിലേക്ക് അയക്കുന്നു, അത് തണുത്ത് മഴയായി തിരിച്ചെത്തുന്നു.",
            "example": "നനഞ്ഞ തുണികൾ വെയിലിൽ ഉണങ്ങുന്നത് നീരാവിയാകുന്നത് കൊണ്ടാണ്."
        },
        "Kannada": {
            "title": "ಜಲ ಚಕ್ರ (Water Cycle)",
            "intro": "ಭೂಮಿಯ ಮೇಲಿನ ನೀರು ಆವಿಯಾಗಿ ಮೋಡವಾಗಿ ಮತ್ತೆ ಮಳೆಯಾಗಿ ಸುರಿಯುವ ಪ್ರಕ್ರಿಯೆಯೇ 'ಜಲ ಚಕ್ರ'.",
            "steps": [
                "1. ಆವಿಯಾಗುವಿಕೆ: ಸೂರ್ಯನ ಶಾಖದಿಂದ ನೀರು ಆವಿಯಾಗಿ ಮೇಲಕ್ಕೆ ಹೋಗುತ್ತದೆ.",
                "2. ಸಾಂದ್ರೀಕರಣ: ಆವಿ ತಂಪಾಗಿ ಮೋಡಗಳಾಗಿ ಬದಲಾಗುತ್ತದೆ.",
                "3. ಮಳೆ ಸುರಿಯುವಿಕೆ: ಮೋಡಗಳು ತಂಪಾಗಿ ಮಳೆಯಾಗಿ ಸುರಿಯುತ್ತವೆ.",
                "4. ಸಂಗ್ರಹಣೆ: ಮಳೆನೀರು ಮತ್ತೆ ನದಿ ಮತ್ತು ಸಮುದ್ರಗಳನ್ನು ಸೇರುತ್ತದೆ."
            ],
            "activity": "ಒಂದು ಬಟ್ಟಲಿನಲ್ಲಿ ನೀರು ಇಟ್ಟು ಬಿಸಿಲಿನಲ್ಲಿಡಿ, ನೀರು ಹೇಗೆ ಕಡಿಮೆಯಾಗುತ್ತದೆ ಎಂಬುದನ್ನು ಗಮನಿಸಿ.",
            "explanation": "ಸೂರ್ಯನು ನೀರನ್ನು ಆವಿ ಮಾಡಿ ಮೇಲೆ ಕಳುಹಿಸುತ್ತಾನೆ, ಅದು ತಂಪಾಗಿ ಮಳೆಯಾಗಿ ಭೂಮಿಗೆ ಮರಳುತ್ತದೆ.",
            "example": "ಬಿಸಿಲಿನಲ್ಲಿ ಒಣಗಲು ಹಾಕಿದ ಬಟ್ಟೆಗಳು ಒಣಗುವುದು ಆವಿಯಾಗುವಿಕೆಗೆ ಉದಾಹರಣೆ."
        },
        "English": {
            "title": "Water Cycle",
            "intro": "The water cycle is the journey water takes as it circulates between oceans, atmosphere, and land.",
            "steps": [
                "1. Evaporation: Heat from the sun turns liquid water into invisible vapor.",
                "2. Condensation: Vapor rises into the colder sky and cools into clouds.",
                "3. Precipitation: Dense clouds release water droplets as rainfall.",
                "4. Collection: Runoff streams back to reservoirs and oceans."
            ],
            "activity": "Place a cup of water under the sun and measure the water level change over 4 hours.",
            "explanation": "Solar energy warms surface water, lifting moisture into clouds that recycle back as life-giving rain.",
            "example": "Just as wet clothes dry quickly on a sunny day through natural evaporation."
        }
    },
    "plants": {
        "Tamil": {
            "title": "தாவரங்கள் (Plants & Photosynthesis)",
            "intro": "தாவரங்கள் நமக்கு தூய காற்று (ஆக்ஸிஜன்), உணவு, நிழல் தரும் இயற்கையின் வரப்பிரசாதம்.",
            "steps": [
                "1. வேர் (Roots): மண்ணிலிருந்து நீரையும் ஊட்டச்சத்துக்களையும் உறிஞ்சுகிறது.",
                "2. தண்டு (Stem): தாவரத்தை நிமிர்த்தி நீரைக் கடத்துகிறது.",
                "3. இலைகள் (Leaves): சூரிய ஒளியைப் பயன்படுத்தி ஒளிச்சேர்க்கை (Photosynthesis) செய்கிறது.",
                "4. மலர்கள் (Flowers): விதைகளை உருவாக்கி புதிய செடிகளை உருவாக்குகிறது."
            ],
            "activity": "ஒரு செடியின் இலையை எடுத்து அதன் நரம்புகளை வரைந்து பாகங்களைக் குறியுங்கள்.",
            "explanation": "செடிகள் சூரிய ஒளி, கார்பன் டை ஆக்சைடு மற்றும் நீரைக் கொண்டு சுயமாக உணவு தயாரிக்கின்றன.",
            "example": "செடிக்கு தினமும் தண்ணீர் ஊற்றினால் அது பசுமையாக வளர்வதைக் காணலாம்."
        },
        "Hindi": {
            "title": "पौधे (Plants)",
            "intro": "पौधे हमारे पर्यावरण के सच्चे मित्र हैं जो हमें ताज़ा हवा और भोजन देते हैं।",
            "steps": [
                "1. जड़: मिट्टी से पानी और खनिज लवण सोखती है।",
                "2. तना: पौधे को सहारा देता है और भोजन-पानी पहुँचाता है।",
                "3. पत्तियां: धूप और क्लोरोफिल की मदद से भोजन बनाती हैं।",
                "4. फूल और फल: नए बीज उत्पन्न करते हैं।"
            ],
            "activity": "किसी पौधे की पत्ती को देखकर उसका चित्र अपनी कॉपी में बनाइए।",
            "explanation": "पौधे धूप, पानी और हवा से अपना भोजन स्वयं बनाते हैं और हमें ऑक्सीजन देते हैं।",
            "example": "जैसे हमें ऊर्जा के लिए भोजन चाहिए, वैसे ही पौधों को धूप और पानी चाहिए।"
        },
        "Telugu": {
            "title": "మొక్కలు (Plants)",
            "intro": "మొక్కలు మనకు స్వచ్ఛమైన గాలిని, ఆహారాన్ని అందించే ప్రకృతి వరం.",
            "steps": [
                "1. వేర్లు: నేల నుండి నీరు, పోషకాలను పీల్చుకుంటాయి.",
                "2. కాండం: మొక్కను నిలబెట్టి ఆకులకు నీటిని చేరవేస్తుంది.",
                "3. ఆకులు: కిరణజన్య సంయోగక్రియ ద్వారా ఆహారాన్ని తయారు చేస్తాయి.",
                "4. పువ్వులు: విత్తనాలను ఉత్పత్తి చేసి కొత్త మొక్కలను ఇస్తాయి."
            ],
            "activity": "ఒక చిన్న మొక్కను పరిశీలించి దాని భాగాల చిత్రం గీయండి.",
            "explanation": "మొక్కలు సూర్యకాంతి, నీరు, గాలిని ఉపయోగించి ఆహారం తయారు చేస్తూ మనకు ప్రాణవాయువును అందిస్తాయి.",
            "example": "రోజూ మొక్కకు నీరు పోస్తే అది పచ్చగా ఎలా పెరుగుతుందో గమనించండి."
        },
        "Malayalam": {
            "title": "സസ്യങ്ങൾ (Plants)",
            "intro": "സസ്യങ്ങൾ നമുക്ക് ശുദ്ധവായുവും ഭക്ഷണവും തണലും നൽകുന്ന ജീവന്റെ ഉറവിടമാണ്.",
            "steps": [
                "1. വേര്: മണ്ണിൽ നിന്ന് വെള്ളവും പോഷകങ്ങളും വലിച്ചെടുക്കുന്നു.",
                "2. തണ്ട്: ചെടിയെ നേരെ നിർത്തുകയും ജലമെത്തിക്കുകയും ചെയ്യുന്നു.",
                "3. ഇലകൾ: പ്രകാശസംശ്ലേഷണത്തിലൂടെ ഭക്ഷണം നിർമ്മിക്കുന്നു.",
                "4. പൂക്കൾ: പുതിയ വിത്തുകൾ ഉണ്ടാക്കുന്നു."
            ],
            "activity": "ഒരു ഇല ശേഖരിച്ച് അതിന്റെ പ്രധാന ഭാഗങ്ങൾ വരയ്ക്കുക.",
            "explanation": "സസ്യങ്ങൾ സൂര്യപ്രകാശവും വെള്ളവും വായുവും ഉപയോഗിച്ച് സ്വന്തമായി ഭക്ഷണം ഉണ്ടാക്കുന്നു.",
            "example": "ചെടികൾക്ക് വെള്ളം ഒഴിക്കുമ്പോൾ അവ തഴച്ചുവളരുന്നത് കാണാം."
        },
        "Kannada": {
            "title": "ಸಸ್ಯಗಳು (Plants)",
            "intro": "ಸಸ್ಯಗಳು ನಮಗೆ ಶುದ್ಧ ಗಾಳಿ, ಆಹಾರ ಮತ್ತು ನೆರಳನ್ನು ನೀಡುವ ಪ್ರಕೃತಿಯ ಕೊಡುಗೆ.",
            "steps": [
                "1. ಬೇರು: ಮಣ್ಣಿನಿಂದ ನೀರು ಮತ್ತು ಪೋಷಕಾಂಶಗಳನ್ನು ಹೀರಿಕೊಳ್ಳುತ್ತದೆ.",
                "2. ಕಾಂಡ: ಸಸ್ಯವನ್ನು ನೇರವಾಗಿ ನಿಲ್ಲಿಸುತ್ತದೆ ಮತ್ತು ನೀರನ್ನು ಸಾಗಿಸುತ್ತದೆ.",
                "3. ಎಲೆಗಳು: ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆಯಿಂದ ಆಹಾರ ತಯಾರಿಸುತ್ತವೆ.",
                "4. ಹೂವು: ಹೊಸ ಬೀಜಗಳನ್ನು ಉತ್ಪಾದಿಸುತ್ತವೆ."
            ],
            "activity": "ಒಂದು ಗಿಡವನ್ನು ಗಮನಿಸಿ ಅದರ ಭಾಗಗಳ ಚಿತ್ರ ಬಿಡಿಸಿ.",
            "explanation": "ಸಸ್ಯಗಳು ಸೂರ್ಯನ ಬೆಳಕು, ನೀರು ಮತ್ತು ಗಾಳಿಯನ್ನು ಬಳಸಿ ಆಹಾರ ತಯಾರಿಸಿ ನಮಗೆ ಆಮ್ಲಜನಕ ನೀಡುತ್ತವೆ.",
            "example": "ಪ್ರತಿದಿನ ಗಿಡಕ್ಕೆ ನೀರು ಹಾಕಿದರೆ ಅದು ಹಸಿರಾಗಿ ಬೆಳೆಯುವುದನ್ನು ನೋಡಬಹುದು."
        },
        "English": {
            "title": "Plants & Botany",
            "intro": "Plants are primary producers that convert sunlight into chemical energy and produce oxygen for our planet.",
            "steps": [
                "1. Roots: Anchor the plant and draw water/minerals from soil.",
                "2. Stem: Provides structural support and transports sap.",
                "3. Leaves: Perform photosynthesis using chlorophyll and sunlight.",
                "4. Flowers: Reproductive organs producing seeds and fruits."
            ],
            "activity": "Sketch a flowering plant in your notebook and label its vascular stem and veins.",
            "explanation": "Through photosynthesis, green plants synthesize glucose from sunlight and carbon dioxide, releasing oxygen.",
            "example": "Observe how a potted seedling grows toward sunlight on a windowsill."
        }
    }
}

# 4. Translation Function
def translate_text(text: str, source: str = "English", target: str = "Tamil") -> Dict[str, Any]:
    """Unified multi-tier translation wrapper."""
    if not text or not text.strip():
        return {"translation": "", "mode": "empty", "source": source, "target": target}

    # Direct model lookup
    res_text = _mod_translate(text, source=source, target=target)
    return {
        "translation": res_text,
        "mode": "multi-tier-engine",
        "source": source,
        "target": target
    }

# 5. Lesson Generation Function
def generate_lesson(topic: str, language: str = "Tamil", grade: int = 3) -> Dict[str, Any]:
    """Generates structured pedagogical lesson plans for Grades 1 to 5."""
    norm_topic = re.sub(r'[^\w\s]', '', topic.lower()).strip()

    for k, lang_dict in TOPIC_KNOWLEDGE.items():
        if k in norm_topic or norm_topic in k:
            if language in lang_dict:
                item = lang_dict[language]
                return {
                    "topic": topic,
                    "language": language,
                    "grade": grade,
                    "intro": item["intro"],
                    "steps": item["steps"],
                    "activity": item["activity"]
                }

    # Dynamic grade-aware templates
    templates = {
        "Tamil": {
            "intro": f"வகுப்பு {grade} மாணவர்களே! இன்று நாம் “{topic}” பற்றி எளிமையாகக் கற்றுக்கொள்வோம்.",
            "steps": [
                f"1. தலைப்பின் பொருள்: “{topic}” என்றால் என்ன என்பதை எளிமையாகப் புரிந்துகொள்வோம்.",
                "2. அறிவியல் தத்துவம்: அன்றாட நிஜ வாழ்க்கையுடன் இதனை தொடர்புபடுத்துவோம்.",
                "3. முக்கிய கருத்துகள்: எளிய வினா-விடை மூலம் அடிப்படைக் கருத்துக்களை நினைவுகூர்வோம்.",
                "4. தாய்மொழி விளக்கம்: மாணவர் தன் சொந்த வார்த்தைகளில் இதனை விளக்கிச் சொல்ல வேண்டும்."
            ],
            "activity": f"“{topic}” தொடர்பான ஒரு அழகான வரைபடம் வரைந்து, வகுப்பில் இரண்டு வரிகள் பேசுங்கள்."
        },
        "Hindi": {
            "intro": f"कक्षा {grade} के प्यारे विद्यार्थियों! आज हम “{topic}” को सरल रूप से सीखेंगे।",
            "steps": [
                f"1. अर्थ समझें: “{topic}” का वास्तविक अर्थ जानें।",
                "2. दैनिक जीवन का संबंध: इसे अपने पर्यावरण से जोड़कर देखें।",
                "3. मुख्य बिंदु: महत्वपूर्ण तथ्यों को मातृभाषा में याद करें।",
                "4. अपने शब्दों में अभ्यास: सीखी हुई बात को बोलकर समझाएं।"
            ],
            "activity": f"“{topic}” का एक चित्र बनाकर कक्षा में दो वाक्य बोलिए।"
        },
        "Telugu": {
            "intro": f"తరగతి {grade} విద్యార్థులారా! ఈరోజు మనం “{topic}” గురించి సులభంగా నేర్చుకుందాం.",
            "steps": [
                f"1. అర్థం తెలుసుకోవడం: “{topic}” అంటే ఏమిటో మొదట అర్థం చేసుకుందాం.",
                "2. నిత్యజీవిత అనుసంధానం: మన పరిసరాలతో దీనిని సరిపోల్చుకుందాం.",
                "3. ముఖ్యాంశాలు: పాఠం యొక్క కీలక విషయాలను గుర్తుచేసుకుందాం.",
                "4. సొంత మాటల్లో చెప్పడం: విద్యార్థి తన మాతృభాషలో దీనిని వివరించాలి."
            ],
            "activity": f"“{topic}” పై ఒక చక్కని చిత్రం గీసి, దాని గురించి మాట్లాడండి."
        },
        "Malayalam": {
            "intro": f"ക്ലാസ് {grade}-ലെ കുട്ടികളെ! ഇന്ന് നമുക്ക് “{topic}” എന്നതിനെക്കുറിച്ച് വളരെ ലളിതമായി പഠിക്കാം.",
            "steps": [
                f"1. ആശയം മനസ്സിലാക്കുക: “{topic}” എന്താണെന്ന് ലളിതമായി അറിയുക.",
                "2. നിത്യജീവിത ഉദാഹരണം: പ്രകൃതിയുമായി ഇതിനെ ബന്ധിപ്പിക്കുക.",
                "3. പ്രധാന ആശയങ്ങൾ: അടിസ്ഥാന കാര്യങ്ങൾ ഓർമ്മിക്കുക.",
                "4. സ്വന്തം വാക്കുകളിൽ പറയുക: മാതൃഭാഷയിൽ ലളിതമായി വിശദീകരിക്കുക."
            ],
            "activity": f"“{topic}” എന്നതിനെ ആസ്പദമാക്കി ഒരു ചിത്രം വരച്ച് രണ്ട് വാക്യം പറയുക."
        },
        "Kannada": {
            "intro": f"ತರಗತಿ {grade}ಯ ವಿದ್ಯಾರ್ಥಿಗಳೇ! ಇಂದು ನಾವು “{topic}” ಬಗ್ಗೆ ಸುಲಭವಾಗಿ ಅರ್ಥಮಾಡಿಕೊಳ್ಳೋಣ.",
            "steps": [
                f"1. ಅರ್ಥ ತಿಳಿದುಕೊಳ್ಳಿ: “{topic}” ಎಂದರೇನು ಎಂಬುದನ್ನು ಮೊದಲು ತಿಳಿಯಿರಿ.",
                "2. ದೈನಂದಿನ ಜೀವನದ ಉದಾಹರಣೆ: ನಮ್ಮ ಪರಿಸರಕ್ಕೆ ಇದನ್ನು ಹೋಲಿಸಿ ನೋಡಿ.",
                "3. ಮುಖ್ಯ ಅಂಶಗಳು: ಪ್ರಮುಖ ವಿಷಯಗಳನ್ನು ಸರಳವಾಗಿ ನೆನಪಿಟ್ಟುಕೊಳ್ಳಿ.",
                "4. ಸ್ವಂತ ಮಾತುಗಳಲ್ಲಿ ಹೇಳಿ: ವಿದ್ಯಾರ್ಥಿ ತನ್ನ ತಾಯ್ನುಡಿಯಲ್ಲಿ ಇದನ್ನು ವಿವರಿಸಿ ಹೇಳಬೇಕು."
            ],
            "activity": f"“{topic}” ಬಗ್ಗೆ ಒಂದು ಸುಂದರವಾದ ಚಿತ್ರ ಬಿಡಿಸಿ, ಅದರ ಬಗ್ಗೆ ಎರಡು ವಾಕ್ಯಗಳನ್ನು ಹೇಳಿ."
        },
        "English": {
            "intro": f"Grade {grade} learners! Today we explore “{topic}” with real-world applications.",
            "steps": [
                f"1. Conceptual Clarity: Learn the foundational definition of “{topic}”.",
                "2. Real-World Analogy: Connect the theory with everyday observations.",
                "3. Key Takeaways: Memorize primary scientific principles step-by-step.",
                "4. Active Recall: Explain the concept back in your native words."
            ],
            "activity": f"Draw a diagram representing “{topic}” and share two observations."
        }
    }

    data = templates.get(language, templates["English"])
    return {
        "topic": topic,
        "language": language,
        "grade": grade,
        "intro": data["intro"],
        "steps": data["steps"],
        "activity": data["activity"]
    }

# 6. Conceptual Explanation Function
def explain_topic(topic: str, language: str = "Tamil", grade: int = 3) -> Dict[str, Any]:
    norm_topic = re.sub(r'[^\w\s]', '', topic.lower()).strip()
    for k, lang_dict in TOPIC_KNOWLEDGE.items():
        if k in norm_topic or norm_topic in k:
            if language in lang_dict:
                item = lang_dict[language]
                return {
                    "explanation": item["explanation"],
                    "example": item["example"],
                    "grade": grade
                }

    lesson = generate_lesson(topic, language, grade)
    return {
        "explanation": lesson["intro"],
        "example": lesson["activity"],
        "grade": grade
    }

# 7. Vocabulary Glossary Function
def vocabulary(language: str = "Tamil") -> List[Dict[str, str]]:
    items = []
    for eng, langs in DEMO.items():
        if " " not in eng and language in langs:
            items.append({"english": eng.title(), "vernacular": langs[language]})
    return items
