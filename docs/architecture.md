# Architecture

```text
Teacher / Student
       |
       v
Responsive Web UI (HTML/CSS/JavaScript)
       |
       v
FastAPI REST API
   |        |        |
   v        v        v
Translation Lesson  Explanation
Engine      Engine     Engine
   |
   +--> Optional LibreTranslate server
   |
   +--> Offline educational fallback
```

The prototype is intentionally lightweight so students can demonstrate the complete workflow without needing paid APIs.
