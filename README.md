# 🌐 Vernacular AI — Multimodal Vernacular Education & Cinema Dubbing Platform

## 2024–2028 Batch | SMT CO2 Team

A unified, next-generation multilingual AI platform supporting **51 Languages** (26 Indian regional languages + 25 global languages), bridging educational and linguistic divides under **NEP 2020 (Sections 4.11 & 4.13)**.

---

## 🌟 Modules & Dedicated Pages

1. **🏠 Overview & Platform Dashboard**
   - System KPIs, language breakdown, NEP 2020 compliance metrics, and live engine status.

2. **🔄 Mother-Tongue Translation & Pedagogy Deconstructor** (`models/translator.py`)
   - Translates lessons, extracts **Scientific Vocabulary Glossaries**, generates **Child-Friendly Explanations**, and builds interactive **Comprehension Mini-Quizzes**.

3. **📚 Vernacular Lesson Generator** (`engine.py`)
   - Grade 1–5 curriculum lesson planner with concept steps, cultural analogies, and classroom activities.

4. **💬 Luthar AI (லூதர் AI) — Universal Multilingual Intelligence** (`models/chatbot.py`)
   - Understands English, Tamil, and Tanglish. Provides step-by-step math calculations, code generation, STEM tutoring, and cinema trivia.

5. **🎬 English Cinema Vernacular Dubbing & Subtitle Studio** (`models/cinema_studio.py`)
   - Synchronized subtitles, AI voice dubbing, cultural idiom decoding (e.g. *"Period"*, *"Don't ever let somebody tell you"*), and standard `.srt` subtitle export.

6. **📡 4-Language Simultaneous Regional Broadcast Grid** (`models/translator.py`)
   - Concurrent real-time broadcast of a single lesson into Tamil, Hindi, Telugu, and Malayalam in parallel.

7. **🔤 Bilingual Primary Vocabulary Word Bank**
   - Curated bilingual STEM flashcards with instant speech pronunciation in native accents.

8. **📑 Academic & Technical Project Report Generator** (`models/report_generator.py`)
   - Publication-grade IEEE/ACM-style academic evaluation reports in printable format and downloadable Markdown.

9. **🗄️ SQLite Database & History Explorer** (`database.py`)
   - Zero-config local persistence stored at `backend/vernacular_ai.db` with star bookmarks, search, and CSV/JSON export.

10. **⚡ Engineering NEC Symbols & Blueprint Studio** (`models/engineering_symbols.py`)
   - Standardized 45+ technical schematic symbols conforming to **NEC 2023 / NFPA 70**, **IEEE 315**, and **IEC 60617** standards.
   - **Upload Symbol / Schematic Vision Inspector**: Upload blueprint snippets or circuit drawings to extract NEC articles, pinouts, working formulas, and mother-tongue pedagogical explanations (Tamil, Hindi, Telugu, English).
   - **Interactive Circuit Calculators**: Real-time Ohm's Law solver ($V=IR, P=VI$), LC Resonant Frequency ($f_0=\frac{1}{2\pi\sqrt{LC}}$), Voltage Divider, and interactive Digital Logic Gate Simulator (AND, OR, NOT, NAND, NOR, XOR, XNOR) with dynamic live Truth Tables.
   - **4 Study Theme System & Pomodoro Focus Timer**: Deep Study Academy (floating calculus formulas), Blueprint CAD (drafting grids & circuits), Cyber Vernacular, and Cozy Library themes with ambient background canvas.


---

## 🚀 Quick Run

Double-click [`run_project.bat`](run_project.bat) or run:

```bash
cd backend
python -m pip install -r requirements.txt
python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

Open: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🏗️ Project Structure

```
├── backend/
│   ├── app.py                     # FastAPI REST server & routing
│   ├── database.py                # SQLite 3 local persistence
│   ├── engine.py                  # Primary grade lesson generator
│   ├── requirements.txt           # Python dependencies
│   ├── vernacular_ai.db           # Embedded local SQLite database
│   └── models/
│       ├── __init__.py
│       ├── translator.py          # 51-lang multi-tier translation & pedagogy
│       ├── chatbot.py             # Luthar AI multilingual tutor
│       ├── cinema_studio.py       # Film dubbing & SRT generator
│       └── report_generator.py    # Academic IEEE report generator
├── frontend/
│   └── index.html                 # Multi-page SPA with animated vernacular canvas
├── docs/                          # Documentation & progress tracking
└── run_project.bat                # 1-Click launcher
```
