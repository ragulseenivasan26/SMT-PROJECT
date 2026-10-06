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
from models.engineering_symbols import (
    get_all_engineering_symbols,
    analyze_uploaded_symbol_or_query,
    calculate_engineering_formula
)

# Backward compatibility with engine if needed
try:
    from engine import generate_lesson, explain_topic, vocabulary
except ImportError:
    generate_lesson = None
    explain_topic = None
    vocabulary = None

app = FastAPI(
    title="Vernacular AI Platform",
    description="Multimodal Vernacular Education, Real-Time Translation & Cinema Dubbing Platform",
    version="2.0.0"
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

class AnalyzeSymbolReq(BaseModel):
    query: Optional[str] = ""
    image_data: Optional[str] = None
    target_language: Optional[str] = "Tamil"

class CalculateFormulaReq(BaseModel):
    formula_type: str
    params: dict

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
        "service": "Vernacular AI Platform",
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

# --- Backward-compatible Lesson & Vocabulary endpoints ---
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
            translate_text("1. Fundamental definition", "English", req.language),
            translate_text("2. Real world connection", "English", req.language),
            translate_text("3. Active vernacular recall", "English", req.language)
        ],
        "activity": translate_text("Draw a diagram and speak two sentences about it.", "English", req.language)
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

# --- Engineering NEC Symbols & Blueprint Studio Endpoints ---
@app.get("/api/engineering/symbols")
def api_engineering_symbols(category: Optional[str] = None):
    symbols = get_all_engineering_symbols(category=category)
    return {
        "total": len(symbols),
        "category": category or "all",
        "symbols": symbols
    }

@app.post("/api/engineering/analyze_symbol")
def api_analyze_symbol(req: AnalyzeSymbolReq):
    query = (req.query or "earth_ground").strip()
    result = analyze_uploaded_symbol_or_query(
        query_or_tag=query,
        target_language=req.target_language or "Tamil"
    )
    return result

@app.post("/api/engineering/calculate")
def api_engineering_calculate(req: CalculateFormulaReq):
    result = calculate_engineering_formula(req.formula_type, req.params or {})
    return result

