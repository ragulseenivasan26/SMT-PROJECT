"""
Government Schemes & Scholarships Knowledge Engine for School and College Students.
Includes Tamil Nadu State and Government of India Central Schemes with
eligibility matching, vernacular translations, and application guidelines.
"""

from typing import List, Dict, Any, Optional

GOVERNMENT_SCHEMES: List[Dict[str, Any]] = [
    {
        "id": "pudhumai_penn",
        "name": "Pudhumai Penn Scheme (Moovalur Ramamirtham Higher Education)",
        "name_ta": "புதுமைப் பெண் திட்டம் (மூவலூர் ராமாமிர்தம் உயர்கல்வி உறுதித் திட்டம்)",
        "state": "Tamil Nadu",
        "level": "State",
        "target_audience": "Female Students (Classes 6-12 Govt School Alumnae)",
        "target_grades": ["11", "12", "College", "Diploma", "ITI"],
        "gender": "Female",
        "school_type": "Government",
        "financial_benefit": "₹1,000 per month (₹12,000 / year) directly into bank account",
        "summary": "Financial assistance of ₹1,000 every month for girl students who studied Classes 6 to 12 in Government Schools, until they complete their undergraduate degree, diploma, or ITI course.",
        "summary_ta": "அரசுப் பள்ளிகளில் 6 முதல் 12-ஆம் வகுப்பு வரை பயின்ற மாணவிகள் உயர்கல்வி (பட்டப்படிப்பு / டிப்ளமோ / ITI) முடிக்கும் வரை மாதம் ₹1,000 அவர்களின் வங்கிக் கணக்கில் நேரடியாக வழங்கப்படுகிறது.",
        "eligibility_criteria": [
            "Must be a girl student",
            "Must have studied from Class 6 to 12 in Tamil Nadu Government Schools",
            "Must be currently enrolled in an recognized Undergraduate, Diploma, or ITI course"
        ],
        "documents_required": [
            "Aadhaar Card",
            "School Transfer Certificate (TC) or 6-12th Bonafide Certificate",
            "College Admission Receipt / ID Card",
            "Active Student Bank Account Passbook"
        ],
        "official_portal": "https://penkalvi.tn.gov.in",
        "category": "Higher Education & Gender Empowerment",
        "badge": "Top TN State Scheme"
    },
    {
        "id": "tamil_pudhalvan",
        "name": "Tamil Pudhalvan Scheme (Boys Higher Education Assistance)",
        "name_ta": "தமிழ்ப் புதல்வன் திட்டம் (மாணவர் உயர்கல்வி உதவித்தொகை)",
        "state": "Tamil Nadu",
        "level": "State",
        "target_audience": "Male Students (Classes 6-12 Govt School Alumnae)",
        "target_grades": ["11", "12", "College", "Diploma", "ITI"],
        "gender": "Male",
        "school_type": "Government",
        "financial_benefit": "₹1,000 per month directly deposited into student bank account",
        "summary": "Monthly financial aid of ₹1,000 to boy students who studied classes 6 to 12 in Tamil Nadu Government schools upon enrolling into higher education to purchase books and study materials.",
        "summary_ta": "தமிழ்நாடு அரசுப் பள்ளிகளில் 6 முதல் 12-ஆம் வகுப்பு வரை பயின்று கல்லூரி அல்லது தொழிற்கல்வியில் சேரும் மாணவர்களுக்கு மாதம் ₹1,000 கல்வி உதவித்தொகை வழங்கப்படுகிறது.",
        "eligibility_criteria": [
            "Must be a male student",
            "Must have completed schooling (Classes 6-12) in TN Government schools",
            "Admitted to recognized college, university, or polytechnic institution"
        ],
        "documents_required": [
            "Aadhaar Card",
            "6th-12th School Bonafide Certificate",
            "College Enrollment Proof",
            "Bank Account linked with Aadhaar"
        ],
        "official_portal": "https://tamilpudhalvan.tn.gov.in",
        "category": "Higher Education Support",
        "badge": "New TN Scheme"
    },
    {
        "id": "cm_breakfast_scheme",
        "name": "Chief Minister's Breakfast Scheme (Mudhalvarin Kaalai Unavu Thittam)",
        "name_ta": "முதலமைச்சரின் காலை உணவுத் திட்டம்",
        "state": "Tamil Nadu",
        "level": "State",
        "target_audience": "Primary School Students (Classes 1 to 5)",
        "target_grades": ["1", "2", "3", "4", "5"],
        "gender": "All",
        "school_type": "Government",
        "financial_benefit": "100% Free nutritious hot cooked breakfast on all school days",
        "summary": "Provides fresh hot nutritious breakfast (Upma, Pongal, Kichadi, Sambar) every morning to all primary students in Government schools to eliminate morning hunger and improve learning energy.",
        "summary_ta": "அனைத்து அரசு தொடக்கப் பள்ளி மாணவர்களுக்கும் (1 முதல் 5-ஆம் வகுப்பு வரை) பள்ளி நாட்களில் சுவையான சத்துமிக்க காலை உணவு இலவசமாக வழங்கப்படுகிறது.",
        "eligibility_criteria": [
            "Students enrolled in Classes 1 to 5 in Government Schools across Tamil Nadu"
        ],
        "documents_required": [
            "School admission record (No separate application needed)"
        ],
        "official_portal": "https://www.tn.gov.in/scheme/data_view/68832",
        "category": "Nutrition & School Health",
        "badge": "Nutrition Flagship"
    },
    {
        "id": "free_laptop_scheme",
        "name": "Tamil Nadu Free Laptop Scheme for Students",
        "name_ta": "தமிழ்நாடு விலையில்லா மடிக்கணினி திட்டம்",
        "state": "Tamil Nadu",
        "level": "State",
        "target_audience": "Class 11 & 12 and Polytechnic College Students",
        "target_grades": ["11", "12", "Diploma"],
        "gender": "All",
        "school_type": "Government / Govt-Aided",
        "financial_benefit": "Free brand-new laptop equipped with learning software",
        "summary": "Supplies laptops with pre-loaded digital curriculum and educational resources to bridge the digital divide for students in Government and Government-aided higher secondary schools.",
        "summary_ta": "அரசு மற்றும் அரசு உதவிபெறும் மேல்நிலைப் பள்ளி மாணவர்களுக்கு டிஜிட்டல் கல்வி அறிவை வளர்க்க விலையில்லா நவீன லேப்டாப் வழங்கப்படுகிறது.",
        "eligibility_criteria": [
            "Enrolled in Class 11/12 in TN Government or Government-Aided Schools",
            "Regular student with valid attendance"
        ],
        "documents_required": [
            "School ID Card",
            "EMIS Number (Educational Management Information System)",
            "Aadhaar Card"
        ],
        "official_portal": "https://tnschools.gov.in",
        "category": "Digital Education Access",
        "badge": "Digital Empowerment"
    },
    {
        "id": "free_bicycle_scheme",
        "name": "Free Bicycle Scheme for Higher Secondary Students",
        "name_ta": "விலையில்லா மிதிவண்டி (சைக்கிள்) திட்டம்",
        "state": "Tamil Nadu",
        "level": "State",
        "target_audience": "Class 11 Students",
        "target_grades": ["11"],
        "gender": "All",
        "school_type": "Government / Govt-Aided",
        "financial_benefit": "Free brand new standard bicycle",
        "summary": "Distributes bicycles free of cost to all students entering Class 11 in Government and Government-aided schools, minimizing dropout rates due to distance and commute issues in rural areas.",
        "summary_ta": "11-ஆம் வகுப்பு பயிலும் மாணவ, மாணவியர் பள்ளிக்கு தடையின்றி எளிதாக வர இலவச மிதிவண்டி வழங்கப்படுகிறது.",
        "eligibility_criteria": [
            "Students studying in Class 11 in TN Govt and Govt-Aided Schools"
        ],
        "documents_required": [
            "School Bonafide Certificate",
            "Aadhaar Number"
        ],
        "official_portal": "https://www.tn.gov.in",
        "category": "Mobility & Rural Education",
        "badge": "Essential Commute"
    },
    {
        "id": "free_bus_pass",
        "name": "Free Bus Pass Scheme for School & College Students",
        "name_ta": "மாணவர்களுக்கான கட்டணமில்லா பேருந்து பயண அட்டை",
        "state": "Tamil Nadu",
        "level": "State",
        "target_audience": "School Students (Classes 1 to 12) & College Students",
        "target_grades": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "College"],
        "gender": "All",
        "school_type": "All (Govt / Aided / Recognized)",
        "financial_benefit": "100% Free daily bus transport on TNSTC buses",
        "summary": "Provides zero-cost bus travel smart passes between student's residence and school/college across Tamil Nadu State Transport Corporation routes.",
        "summary_ta": "பள்ளி மற்றும் கல்லூரி மாணவர்கள் தங்கள் வீட்டிலிருந்து கல்வி நிலையத்திற்கு செல்ல இலவச பேருந்து பயண அட்டை வழங்கப்படுகிறது.",
        "eligibility_criteria": [
            "Any student pursuing schooling or higher education in recognized institutions in Tamil Nadu"
        ],
        "documents_required": [
            "Institution Application Form signed by Headmaster/Principal",
            "Passport Size Photograph",
            "Address Proof (Ration Card/Aadhaar)"
        ],
        "official_portal": "https://www.tnstc.in",
        "category": "Mobility & Transport",
        "badge": "100% Free Commute"
    },
    {
        "id": "tn_7_5_reservation",
        "name": "7.5% Preferential Reservation for Govt School Students in Professional Courses",
        "name_ta": "அரசுப் பள்ளி மாணவர்களுக்கான 7.5% சிறப்பு உள்ஒதுக்கீடு",
        "state": "Tamil Nadu",
        "level": "State",
        "target_audience": "Govt School Students aspiring for MBBS, BDS, Engineering, Law, Agri",
        "target_grades": ["12", "College"],
        "gender": "All",
        "school_type": "Government",
        "financial_benefit": "7.5% quota in premier seats + 100% Tuition, Hostel & Counseling Fees paid by Govt",
        "summary": "Offers 7.5% horizontal reservation for government school students in medical (NEET-UG), engineering (TNEA), agriculture (TNAU), law, and veterinary colleges. Government pays entire tuition, hostel, and development fees.",
        "summary_ta": "அரசுப் பள்ளி மாணவர்களுக்கு மருத்துவம் மற்றும் பொறியியல் உள்ளிட்ட தொழிற்கல்வி படிப்புகளில் 7.5% உள்ஒதுக்கீடு மற்றும் முழு கல்லூரி கல்விக் கட்டணம், விடுதிக் கட்டணத்தை அரசே ஏற்கிறது.",
        "eligibility_criteria": [
            "Must have studied continuously from Class 6 to 12 in Tamil Nadu Government Schools"
        ],
        "documents_required": [
            "Bonafide Certificate from Chief Educational Officer (CEO)",
            "Class 10 & 12 Marksheets",
            "Entrance exam scorecard (NEET/TNEA registration)"
        ],
        "official_portal": "https://www.tneaonline.org",
        "category": "Professional Higher Education",
        "badge": "Life Changing Quota"
    },
    {
        "id": "nmms_scholarship",
        "name": "National Means-cum-Merit Scholarship Scheme (NMMS)",
        "name_ta": "தேசிய வருவாய் வழி மற்றும் திறன் படிப்புதவித் தொகை திட்டம் (NMMS)",
        "state": "All India",
        "level": "Central",
        "target_audience": "Meritorious Class 8 Students transitioning to 9-12",
        "target_grades": ["8", "9", "10", "11", "12"],
        "gender": "All",
        "school_type": "Government / Govt-Aided",
        "financial_benefit": "₹12,000 per year (₹1,000 per month) for 4 consecutive years",
        "summary": "Centrally sponsored scheme by the Ministry of Education to award scholarships to meritorious students of economically weaker sections to arrest dropout at Class 8 and encourage higher secondary study.",
        "summary_ta": "பொருளாதாரத்தில் பின்தங்கிய திறமையான மாணவர்கள் இடைநிற்றலைத் தடுக்க 9 முதல் 12-ஆம் வகுப்பு வரை ஆண்டுக்கு ₹12,000 (மாதம் ₹1,000) உதவித்தொகை வழங்கப்படுகிறது.",
        "eligibility_criteria": [
            "Appeared in NMMS exam while in Class 8",
            "Minimum 55% marks in Class 7 exam (50% for SC/ST)",
            "Parental annual income less than ₹3,50,000 per annum"
        ],
        "documents_required": [
            "NMMS Exam Hall Ticket & Scorecard",
            "Income Certificate (under ₹3.5 Lakhs)",
            "Caste Certificate",
            "Student Bank Account Details"
        ],
        "official_portal": "https://scholarships.gov.in",
        "category": "National Merit Scholarship",
        "badge": "National Central Scheme"
    },
    {
        "id": "pm_yasasvi",
        "name": "PM YASASVI Scholarship Scheme for Young Achievers",
        "name_ta": "பிரதம மந்திரி யசஸ்வி உதவித்தொகை திட்டம்",
        "state": "All India",
        "level": "Central",
        "target_audience": "OBC, EBC, DNT Students of Class 9 & Class 11",
        "target_grades": ["9", "10", "11", "12"],
        "gender": "All",
        "school_type": "Top Identified Schools",
        "financial_benefit": "₹75,000/year for Class 9-10; ₹1,25,000/year for Class 11-12",
        "summary": "Top-class education scholarship scheme administered by the Ministry of Social Justice and Empowerment for students belonging to Other Backward Classes, Economically Backward Classes, and Nomadic Tribes.",
        "summary_ta": "OBC/EBC/DNT பிரிவு மாணவர்களுக்கு 9 மற்றும் 10-ஆம் வகுப்பிற்கு ஆண்டுக்கு ₹75,000; 11 மற்றும் 12-ஆம் வகுப்பிற்கு ஆண்டுக்கு ₹1,25,000 வரை உயர் கல்வி உதவித்தொகை வழங்கப்படுகிறது.",
        "eligibility_criteria": [
            "Belongs to OBC / EBC / DNT categories",
            "Parental income less than ₹2.5 Lakhs per year",
            "Studying in nominated top schools"
        ],
        "documents_required": [
            "Income Certificate",
            "Community / Caste Certificate",
            "School Bonafide",
            "Aadhaar Card"
        ],
        "official_portal": "https://yet.nta.ac.in",
        "category": "High Value National Scholarship",
        "badge": "Up to ₹1.25 Lakhs"
    },
    {
        "id": "inspire_manak",
        "name": "INSPIRE Awards - MANAK (Million Minds Augmenting National Aspiration)",
        "name_ta": "இன்ஸ்பயர் மானக் புத்தாக்க அறிவியல் விருது",
        "state": "All India",
        "level": "Central",
        "target_audience": "Students of Classes 6 to 10 with Science Project Ideas",
        "target_grades": ["6", "7", "8", "9", "10"],
        "gender": "All",
        "school_type": "All Schools",
        "financial_benefit": "₹10,000 one-time grant to build scientific prototype model",
        "summary": "Flagship scheme of the Department of Science & Technology (DST) to foster a culture of creative thinking and innovation among school students. Selected innovative project ideas receive ₹10,000 directly to construct their working model.",
        "summary_ta": "அறிவியல் படைப்பாற்றல் மிக்க 6 முதல் 10-ஆம் வகுப்பு பள்ளி மாணவர்களின் புதிய கண்டுபிடிப்புகளுக்கு ₹10,000 நிதி உதவி மற்றும் தேசிய கண்காட்சி வாய்ப்பு வழங்கப்படுகிறது.",
        "eligibility_criteria": [
            "Students aged 10-15 years studying in Classes 6 to 10",
            "Nominated by school with an original creative science/societal innovation idea"
        ],
        "documents_required": [
            "Project synopsis & sketch",
            "School Headmaster nomination",
            "Student Bank Account"
        ],
        "official_portal": "https://www.inspireawards-dst.gov.in",
        "category": "Science & Innovation",
        "badge": "Science Award"
    },
    {
        "id": "samagra_shiksha_supplies",
        "name": "Samagra Shiksha - 100% Free Books, Uniforms & Learning Kits",
        "name_ta": "சமக்ர சிக்ஷா - இலவச பாடப்புத்தகங்கள், சீருடைகள் மற்றும் உபகரணங்கள்",
        "state": "Tamil Nadu & Pan-India",
        "level": "Joint State-Central",
        "target_audience": "Students in Classes 1 to 8",
        "target_grades": ["1", "2", "3", "4", "5", "6", "7", "8"],
        "gender": "All",
        "school_type": "Government",
        "financial_benefit": "Free 4 sets of uniforms, all textbooks, notebooks, school bag, geometry box & footwear",
        "summary": "Ensures no child is denied education due to economic barriers by providing every essential learning item free of cost directly at the beginning of each academic term in government schools.",
        "summary_ta": "அரசுப் பள்ளி மாணவர்களுக்கு 4 செட் சீருடைகள், பாடப்புத்தகங்கள், நோட்டுப் புத்தகங்கள், புத்தகப் பை, காலணிகள் உள்ளிட்ட 14 வகையான பொருட்கள் முழுமையாக இலவசமாக வழங்கப்படுகிறது.",
        "eligibility_criteria": [
            "All children studying in Government schools from Classes 1 to 8"
        ],
        "documents_required": [
            "Automatic entitlement through school enrollment"
        ],
        "official_portal": "https://samagra.education.gov.in",
        "category": "School Essentials",
        "badge": "Universal Entitlement"
    },
    {
        "id": "begum_hazrat_mahal",
        "name": "Begum Hazrat Mahal National Scholarship for Minority Girls",
        "name_ta": "பேகம் ஹசரத் மஹால் சிறுபான்மையினர் மாணவிகள் தேசிய உதவித்தொகை",
        "state": "All India",
        "level": "Central",
        "target_audience": "Minority Girl Students of Classes 9 to 12",
        "target_grades": ["9", "10", "11", "12"],
        "gender": "Female",
        "school_type": "All Recognized Schools",
        "financial_benefit": "₹5,000/year for Class 9-10; ₹6,000/year for Class 11-12",
        "summary": "Financial support awarded to meritorious girl students belonging to national minority communities (Muslim, Christian, Sikh, Buddhist, Jain, Parsi) to continue their secondary and higher secondary schooling.",
        "summary_ta": "சிறுபான்மை சமூகங்களைச் சேர்ந்த மாணவிகள் தங்களின் பள்ளிப் படிப்பைத் தொடர ஆண்டுதோறும் உதவித்தொகை வழங்கப்படுகிறது.",
        "eligibility_criteria": [
            "Girl student belonging to notified minority communities",
            "Minimum 50% marks in previous exam",
            "Annual family income not exceeding ₹2,00,000"
        ],
        "documents_required": [
            "Self-attested minority community certificate",
            "Income certificate",
            "Marksheet of previous class",
            "Bank passbook"
        ],
        "official_portal": "https://scholarships.gov.in",
        "category": "Minority Girls Education",
        "badge": "Minority Empowerment"
    }
]


def get_all_schemes(state: Optional[str] = None, grade: Optional[str] = None, gender: Optional[str] = None) -> List[Dict[str, Any]]:
    """Retrieve schemes with optional filtering."""
    results = GOVERNMENT_SCHEMES
    if state and state.lower() != "all":
        results = [s for s in results if s["state"].lower() == state.lower() or s["level"].lower() == "central"]
    if grade and grade.lower() != "all":
        results = [s for s in results if str(grade) in s["target_grades"]]
    if gender and gender.lower() != "all":
        results = [s for s in results if s["gender"] in [gender, "All"]]
    return results


def check_student_eligibility(
    grade: str,
    gender: str = "All",
    school_type: str = "Government",
    family_income: Optional[float] = None
) -> Dict[str, Any]:
    """Smart eligibility checker for a student based on profile."""
    eligible = []
    other_opportunities = []

    for scheme in GOVERNMENT_SCHEMES:
        match = True
        
        # Check grade
        if grade not in scheme["target_grades"] and "College" not in scheme["target_grades"]:
            match = False
            
        # Check gender
        if scheme["gender"] != "All" and gender != "All" and scheme["gender"].lower() != gender.lower():
            match = False

        # Check school type
        if "Government" in scheme["school_type"] and school_type.lower() == "private":
            if scheme["school_type"] == "Government":
                match = False

        if match:
            eligible.append(scheme)
        else:
            other_opportunities.append(scheme)

    return {
        "student_profile": {
            "grade": grade,
            "gender": gender,
            "school_type": school_type,
            "family_income": family_income
        },
        "total_eligible": len(eligible),
        "eligible_schemes": eligible,
        "other_schemes": other_opportunities[:4],
        "guidance_note": f"Great news! We found {len(eligible)} government schemes & scholarships matching your profile. Check the application portals to apply."
    }
