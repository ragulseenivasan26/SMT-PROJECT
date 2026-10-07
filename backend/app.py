import os
import io
import json
from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, List, Any

import database
from models.translator import (
    translate_text,
    translate_multi_target,
    SUPPORTED_LANGUAGES,
    get_language_code,
    extract_key_vocabulary,
    generate_explanation,
    generate_mini_quiz,
    answer_student_doubt
)
from models.cinema_studio import get_cinema_scenes, translate_scene, generate_srt_file
from models.report_generator import generate_report_data, generate_markdown_report
from models.chatbot import generate_chat_response
from models.government_schemes import get_all_schemes, check_student_eligibility
from models.video_translator import process_video_translation, EDUCATIONAL_VIDEO_PRESETS
from models.live_vision import analyze_camera_frame

# Backward compatibility with engine if needed
try:
    from engine import generate_lesson, explain_topic, vocabulary
except ImportError:
    generate_lesson = None
    explain_topic = None
    vocabulary = None

app = FastAPI(
    title="AI Vernacular Pedagogy",
    description="AI-Powered Vernacular Pedagogy & Real-Time Translation Platform",
    version="3.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "frontend"))

if os.path.exists(FRONTEND_DIR):
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

database.init_db()

# --- Request Models ---
class TranslateReq(BaseModel):
    text: str
    source: Optional[str] = "English"
    target: Optional[str] = "Tamil"

class BroadcastReq(BaseModel):
    text: str
    source: Optional[str] = "English"
    targets: Optional[List[str]] = ["Tamil", "Hindi", "Telugu", "Malayalam"]

class AskDoubtReq(BaseModel):
    lesson: Optional[str] = ""
    context: Optional[str] = ""
    question: str
    target: Optional[str] = "Tamil"
    target_lang: Optional[str] = None

class ChatReq(BaseModel):
    message: str
    history: Optional[List[Any]] = []
    language: Optional[str] = None
    target: Optional[str] = None

class CinemaTranslateReq(BaseModel):
    scene_id: Optional[str] = "pursuit_of_happyness"
    target: Optional[str] = "Tamil"

class LessonReq(BaseModel):
    topic: str
    language: Optional[str] = "Tamil"
    grade: Optional[int] = 3

class ExplainReq(BaseModel):
    topic: str
    language: Optional[str] = "Tamil"
    grade: Optional[int] = 3

class SchemesEligibilityReq(BaseModel):
    grade: str = "9"
    gender: Optional[str] = "All"
    school_type: Optional[str] = "Government"
    family_income: Optional[float] = None

class VideoTranslateReq(BaseModel):
    video_input: Optional[str] = "solar_system"
    target_language: Optional[str] = "Tamil"
    custom_script: Optional[str] = None

class LiveVisionReq(BaseModel):
    detected_text: Optional[str] = ""
    mode: Optional[str] = "book_scanner"
    target_language: Optional[str] = "Tamil"

# --- Routes ---
@app.get("/")
def home():
    index_file = os.path.join(FRONTEND_DIR, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "Vernacular AI Platform is running"}

@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "service": "Vernacular AI Student Platform",
        "languages_count": len(SUPPORTED_LANGUAGES),
        "database": database.get_db_info()
    }

@app.get("/api/languages")
def get_languages():
    return {
        "languages": SUPPORTED_LANGUAGES,
        "total": len(SUPPORTED_LANGUAGES)
    }

@app.post("/api/translate")
def api_translate(req: TranslateReq):
    text = (req.text or "").strip()
    source = req.source or "English"
    target = req.target or "Tamil"

    if not text:
        raise HTTPException(status_code=400, detail="Please enter educational text or a question.")

    result = translate_text(text, source, target)

    record_id = None
    try:
        record_id = database.save_translation(
            source_lang=source,
            target_lang=target,
            source_text=text,
            translated_text=result
        )
    except Exception as e:
        print(f"Database save error: {e}")

    vocab = []
    explanation = ""
    quiz = []
    try:
        vocab = extract_key_vocabulary(text, source=source, target=target)
        explanation = generate_explanation(text, target=target)
        quiz = generate_mini_quiz(text, result, target=target)
    except Exception as e:
        print(f"Pedagogy pack generation error: {e}")

    return {
        "id": record_id,
        "source": source,
        "target": target,
        "source_code": get_language_code(source),
        "target_code": get_language_code(target),
        "translation": result,
        "vocabulary": vocab,
        "explanation": explanation,
        "quiz": quiz,
        "model": "Multi-Vernacular Pedagogical Engine"
    }

@app.post("/api/translate/broadcast")
def api_broadcast(req: BroadcastReq):
    text = (req.text or "").strip()
    source = req.source or "English"
    targets = req.targets or ["Tamil", "Hindi", "Telugu", "Malayalam"]

    if not text:
        raise HTTPException(status_code=400, detail="Text is required for broadcast.")

    translations = translate_multi_target(text, source=source, targets=targets)
    return {
        "source": source,
        "text": text,
        "broadcast": translations
    }

@app.post("/api/ask_doubt")
def api_ask_doubt(req: AskDoubtReq):
    lesson = (req.lesson or req.context or "").strip()
    question = (req.question or "").strip()
    target = req.target or req.target_lang or "Tamil"

    if not question:
        raise HTTPException(status_code=400, detail="Doubt question is required.")

    answer = answer_student_doubt(lesson, question, target=target)
    return {
        "question": question,
        "target": target,
        "answer": answer
    }

@app.post("/api/chat")
def api_chat(req: ChatReq):
    message = (req.message or "").strip()
    history = req.history or []
    lang_input = req.language or req.target
    target_language = None if (not lang_input or str(lang_input).lower() == "auto") else lang_input
    
    result = generate_chat_response(message, history=history, target_language=target_language)
    return result

# --- Government Schemes Endpoints ---
@app.get("/api/schemes")
def api_get_schemes(state: Optional[str] = None, grade: Optional[str] = None, gender: Optional[str] = None):
    schemes = get_all_schemes(state=state, grade=grade, gender=gender)
    return {
        "total": len(schemes),
        "schemes": schemes
    }

@app.post("/api/schemes/check_eligibility")
def api_check_schemes_eligibility(req: SchemesEligibilityReq):
    result = check_student_eligibility(
        grade=req.grade,
        gender=req.gender or "All",
        school_type=req.school_type or "Government",
        family_income=req.family_income
    )
    return result

# --- Video Translation & Subtitles Endpoints ---
@app.get("/api/video/presets")
def api_video_presets():
    return {
        "presets": EDUCATIONAL_VIDEO_PRESETS
    }

@app.post("/api/video/translate")
def api_video_translate(req: VideoTranslateReq):
    result = process_video_translation(
        video_input=req.video_input or "solar_system",
        target_language=req.target_language or "Tamil",
        custom_script=req.custom_script
    )
    return result

@app.post("/api/video/export_srt")
async def api_video_export_srt(request: Request):
    data = await request.json()
    srt_content = data.get("srt_content", "")
    target_lang = data.get("target_language", "vernacular")
    filename = f"education_subtitles_{target_lang}.srt"
    return Response(
        content=srt_content,
        media_type="text/plain; charset=utf-8",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )

# --- Live Camera & Vision Endpoint ---
@app.post("/api/vision/analyze")
def api_vision_analyze(req: LiveVisionReq):
    result = analyze_camera_frame(
        detected_text=req.detected_text or "",
        mode=req.mode or "book_scanner",
        target_language=req.target_language or "Tamil"
    )
    return result

# --- Cinema Studio Endpoints ---
@app.get("/api/cinema/scenes")
def api_cinema_scenes():
    return {"scenes": get_cinema_scenes()}

@app.post("/api/cinema/translate")
def api_cinema_translate(req: CinemaTranslateReq):
    scene_id = req.scene_id or "pursuit_of_happyness"
    target = req.target or "Tamil"
    result = translate_scene(scene_id, target=target)
    if not result:
        raise HTTPException(status_code=404, detail="Scene not found")
    return result

@app.post("/api/cinema/export_srt")
async def api_cinema_export_srt(request: Request):
    data = await request.json()
    srt_content = generate_srt_file(data)
    filename = f"{data.get('scene_id', 'subtitle')}_{data.get('target_language', 'vernacular')}.srt"
    return Response(
        content=srt_content,
        media_type="text/plain; charset=utf-8",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )

# --- Project Academic Report Endpoints ---
@app.get("/api/project/report")
def api_project_report():
    return generate_report_data()

@app.get("/api/project/report/download")
def api_project_report_download():
    md = generate_markdown_report()
    return Response(
        content=md,
        media_type="text/markdown; charset=utf-8",
        headers={"Content-Disposition": "attachment; filename=Vernacular_AI_Project_Report.md"}
    )

# --- History & Database Endpoints ---
@app.get("/api/history")
def api_get_history(limit: int = 50):
    items = database.get_history(limit=limit)
    return {"history": items}

@app.delete("/api/history/{item_id}")
def api_delete_history(item_id: int):
    success = database.delete_history_item(item_id)
    return {"success": success}

@app.delete("/api/history")
def api_clear_history():
    database.clear_all_history()
    return {"success": True, "message": "History cleared successfully."}

@app.post("/api/favorite/{item_id}")
def api_toggle_favorite(item_id: int):
    new_status = database.toggle_favorite(item_id)
    return {"id": item_id, "is_favorite": new_status}

@app.get("/api/database/info")
def api_database_info():
    return database.get_db_info()

class SqlQueryReq(BaseModel):
    sql_query: str

@app.post("/api/database/query")
def api_database_query(req: SqlQueryReq):
    """Executes a custom SELECT SQL query via SQLite cursor."""
    return database.run_custom_query(req.sql_query)

class SettingsReq(BaseModel):
    network_mode: Optional[str] = "auto"
    gemini_api_key: Optional[str] = None
    translator_provider: Optional[str] = "auto"

@app.get("/api/settings")
def api_get_settings():
    return database.get_all_settings()

@app.post("/api/settings")
def api_update_settings(req: SettingsReq):
    if req.network_mode:
        database.set_setting("network_mode", req.network_mode.lower())
    if req.gemini_api_key is not None:
        database.set_setting("gemini_api_key", req.gemini_api_key.strip())
    if req.translator_provider:
        database.set_setting("translator_provider", req.translator_provider.lower())
    return {
        "success": True,
        "message": "Settings updated successfully.",
        "settings": database.get_all_settings()
    }

@app.post("/api/settings/test_key")
def api_test_key(req: SettingsReq):
    key = req.gemini_api_key or database.get_setting("gemini_api_key", "")
    if not key:
        raise HTTPException(status_code=400, detail="No API Key provided to test.")
    try:
        import requests
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key.strip()}"
        res = requests.post(
            url,
            json={"contents": [{"parts": [{"text": "Hello, respond with: OK"}]}]},
            timeout=7
        )
        if res.status_code == 200:
            return {"valid": True, "message": "API Key is valid and active! 🟢"}
        else:
            return {"valid": False, "status_code": res.status_code, "message": f"API Error: {res.text[:100]}"}
    except Exception as e:
        return {"valid": False, "message": f"Connection error: {str(e)}"}

@app.get("/api/database/export")
def api_database_export(format: str = "json"):
    if format.lower() == "csv":
        csv_data = database.export_as_csv()
        return Response(
            content=csv_data,
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=vernacular_ai_database.csv"}
        )
    rows = database.get_all_rows()
    return {"database_export": rows, "total": len(rows)}

# --- Universal Student Learning Package JSON Export ---
@app.get("/api/export/all_data")
def api_export_all_data():
    rows = database.get_all_rows()
    schemes = get_all_schemes()
    return {
        "project": "Vernacular AI Student Platform",
        "description": "Comprehensive student pedagogical dataset, translation records, and government scholarship information",
        "total_translations": len(rows),
        "translation_history": rows,
        "supported_languages": SUPPORTED_LANGUAGES,
        "government_schemes": schemes,
        "status": "ready"
    }

# --- Lessons & Explainers ---
@app.post("/api/lesson")
def api_lesson(req: LessonReq):
    if generate_lesson:
        return generate_lesson(req.topic, req.language, req.grade)
    trans = translate_text(f"Lesson on {req.topic}", "English", req.language)
    return {
        "topic": req.topic,
        "language": req.language,
        "grade": req.grade,
        "intro": trans,
        "steps": [
            translate_text("1. Fundamental concept definition", "English", req.language),
            translate_text("2. Real world daily life example", "English", req.language),
            translate_text("3. Active vernacular recall and question", "English", req.language)
        ],
        "activity": translate_text("Draw a diagram and write two key takeaways in your notebook.", "English", req.language)
    }

@app.post("/api/explain")
def api_explain(req: ExplainReq):
    if explain_topic:
        return explain_topic(req.topic, req.language, req.grade)
    trans = translate_text(f"Easy explanation of {req.topic}", "English", req.language)
    return {"explanation": trans, "example": "Real world analogy", "grade": req.grade}

@app.get("/api/vocabulary")
def api_vocabulary(language: str = "Tamil"):
    if vocabulary:
        return {"language": language, "items": vocabulary(language)}
    return {"language": language, "items": []}
