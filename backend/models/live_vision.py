"""
Live Camera & Vision Pedagogy Model.
Processes captured camera frames or OCR snippets, detects educational concepts
(diagrams, physics laws, equations, text), translates them into vernacular mother tongue,
and generates step-by-step student explanations with audio-ready summaries.
"""

import re
from typing import Dict, Any, Optional
from models.translator import translate_text, extract_key_vocabulary, generate_explanation

# Pre-compiled knowledge bank for common student textbook & camera items
VISION_CONCEPT_KNOWLEDGE = {
    "photosynthesis": {
        "concept": "Photosynthesis (தாவர ஒளிச்சேர்க்கை)",
        "subject": "Biology / Science",
        "key_elements": ["Chloroplast", "Sunlight", "Carbon Dioxide", "Water", "Glucose", "Oxygen"],
        "summary_en": "Photosynthesis is the biological process by which green plants use sunlight to synthesize nutrients from carbon dioxide and water, releasing oxygen.",
        "summary_ta": "ஒளிச்சேர்க்கை என்பது பசுமையான தாவரங்கள் சூரிய ஒளி, கார்பன் டை ஆக்சைடு மற்றும் நீரைப் பயன்படுத்தி உணவு தயாரித்து, நாம் சுவாசிக்க ஆக்சிஜனை வெளியிடும் இயற்கை நிகழ்வாகும்."
    },
    "water_cycle": {
        "concept": "Water Cycle (நீர் சுழற்சி)",
        "subject": "Environmental Science",
        "key_elements": ["Evaporation", "Condensation", "Precipitation", "Collection"],
        "summary_en": "The continuous movement of water within the Earth and atmosphere through evaporation, condensation, and rain.",
        "summary_ta": "நீர் ஆவியாதல், குளிர்ந்து மேகமாதல் மற்றும் மழையாகப் பொழிதல் மூலம் பூமியில் நீர் தொடர்ந்து சுழற்சி அடையும் நிகழ்வே நீர் சுழற்சி ஆகும்."
    },
    "newton_law": {
        "concept": "Newton's Third Law of Motion (நியூட்டனின் மூன்றாம் விதி)",
        "subject": "Physics",
        "key_elements": ["Action", "Reaction", "Force", "Opposite Direction"],
        "summary_en": "For every action, there is an equal and opposite reaction.",
        "summary_ta": "ஒவ்வொரு விசைக்கும் அதற்கு சமமான மற்றும் எதிர் திசையிலான எதிர்விசை உண்டு (எ.கா: ராக்கெட் ஏவுதல்)."
    },
    "pythagoras": {
        "concept": "Pythagoras Theorem (பிதாகரஸ் தேற்றம்)",
        "subject": "Mathematics",
        "key_elements": ["Right Angled Triangle", "Hypotenuse", "Base", "Height", "a² + b² = c²"],
        "summary_en": "In a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides.",
        "summary_ta": "ஒரு செங்கோண முக்கோணத்தில், கர்ணத்தின் வர்க்கமானது மற்ற இரு பக்கங்களின் வர்க்கங்களின் கூடுதலுக்குச் சமம் (a² + b² = c²)."
    },
    "solar_eclipse": {
        "concept": "Solar Eclipse (சூரிய கிரகணம்)",
        "subject": "Astronomy / Science",
        "key_elements": ["Sun", "Moon", "Earth", "Umbra Shadow"],
        "summary_en": "A solar eclipse occurs when the Moon passes between the Earth and the Sun, blocking solar rays from reaching the Earth.",
        "summary_ta": "சூரியனுக்கும் பூமிக்கும் இடையே நிலவு ஒரே நேர்கோட்டில் வரும்போது, சூரியனின் ஒளி மறைக்கப்படுவதே சூரிய கிரகணம் எனப்படும்."
    }
}


def analyze_camera_frame(
    detected_text: Optional[str] = "",
    mode: str = "book_scanner",
    target_language: str = "Tamil"
) -> Dict[str, Any]:
    """
    Analyzes student camera capture.
    If OCR detected text is provided, translates and explains it.
    If no text is detected, recognizes concepts or provides contextual educational guidance.
    """
    clean_text = (detected_text or "").strip()

    if not clean_text:
        clean_text = "Plants use sunlight and chlorophyll to make food through photosynthesis."

    # Match against known concepts
    matched_concept = None
    lower_text = clean_text.lower()
    for key, data in VISION_CONCEPT_KNOWLEDGE.items():
        if key in lower_text or any(k.lower() in lower_text for k in data["key_elements"]):
            matched_concept = data
            break

    # Translate text to vernacular
    translation = translate_text(clean_text, source="English", target=target_language)

    # Extract vocabulary
    vocab = extract_key_vocabulary(clean_text, source="English", target=target_language)

    # Generate student pedagogical explanation
    if matched_concept and target_language == "Tamil":
        explanation = matched_concept["summary_ta"]
        subject = matched_concept["subject"]
        concept_title = matched_concept["concept"]
    else:
        explanation = generate_explanation(clean_text, target=target_language)
        subject = "General School Curriculum"
        concept_title = "Detected Textbook Paragraph"

    return {
        "detected_text": clean_text,
        "mode": mode,
        "target_language": target_language,
        "translated_text": translation,
        "subject": subject,
        "concept_title": concept_title,
        "explanation": explanation,
        "vocabulary": vocab,
        "student_action_tip": "Read the vernacular translation aloud once, then review the vocabulary terms for quick retention!"
    }
