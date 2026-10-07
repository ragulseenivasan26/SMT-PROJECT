"""
SQLite Database Layer for Vernacular AI.
Manages persistent translation history, student study bookmarks,
application configuration / API keys, and custom SQL cursor querying.
"""

import sqlite3
import os
import csv
import io
from datetime import datetime
from typing import List, Dict, Any, Optional

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vernacular_ai.db")


def get_connection():
    """Returns an active SQLite connection with row factory configured."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initializes tables and indexes if they do not exist."""
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # 1. Translations table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS translations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_lang TEXT NOT NULL,
                target_lang TEXT NOT NULL,
                source_text TEXT NOT NULL,
                translated_text TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_favorite INTEGER DEFAULT 0,
                category TEXT DEFAULT 'general'
            )
        """)
        # Ensure category column exists in case of existing older databases
        cursor.execute("PRAGMA table_info(translations)")
        columns = [col[1] for col in cursor.fetchall()]
        if "category" not in columns:
            cursor.execute("ALTER TABLE translations ADD COLUMN category TEXT DEFAULT 'general'")

        # Performance index for fast offline cache lookups
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_trans_lookup 
            ON translations(source_text, target_lang)
        """)

        # 2. Settings table (for API key, mode: online/offline/auto, provider)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS app_settings (
                key TEXT PRIMARY KEY,
                value TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # 3. Student Notes table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS student_notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                target_lang TEXT DEFAULT 'Tamil',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Default settings initialization if not present
        cursor.execute("SELECT value FROM app_settings WHERE key = 'network_mode'")
        if not cursor.fetchone():
            cursor.execute("INSERT OR REPLACE INTO app_settings (key, value) VALUES ('network_mode', 'auto')")
            cursor.execute("INSERT OR REPLACE INTO app_settings (key, value) VALUES ('gemini_api_key', '')")
            cursor.execute("INSERT OR REPLACE INTO app_settings (key, value) VALUES ('translator_provider', 'auto')")

        conn.commit()


# --- Translations Operations ---

def save_translation(source_lang: str, target_lang: str, source_text: str, translated_text: str, category: str = "general") -> int:
    """Saves a new translation entry into SQLite database."""
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO translations (source_lang, target_lang, source_text, translated_text, category)
            VALUES (?, ?, ?, ?, ?)
        """, (source_lang, target_lang, source_text, translated_text, category))
        conn.commit()
        return cursor.lastrowid


def get_history(limit: int = 50, search: Optional[str] = None) -> List[Dict[str, Any]]:
    """Fetches translation history with optional search filtering."""
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        if search and search.strip():
            query_term = f"%{search.strip()}%"
            cursor.execute("""
                SELECT id, source_lang, target_lang, source_text, translated_text, created_at, is_favorite, category
                FROM translations
                WHERE source_text LIKE ? OR translated_text LIKE ?
                ORDER BY created_at DESC, id DESC
                LIMIT ?
            """, (query_term, query_term, limit))
        else:
            cursor.execute("""
                SELECT id, source_lang, target_lang, source_text, translated_text, created_at, is_favorite, category
                FROM translations
                ORDER BY created_at DESC, id DESC
                LIMIT ?
            """, (limit,))
        rows = cursor.fetchall()
        return [dict(row) for row in rows]


def get_all_rows() -> List[Dict[str, Any]]:
    """Returns all rows for export."""
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, source_lang, target_lang, source_text, translated_text, created_at, is_favorite, category
            FROM translations
            ORDER BY id ASC
        """)
        return [dict(row) for row in cursor.fetchall()]


def delete_history_item(item_id: int) -> bool:
    """Deletes a specific history item by ID."""
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM translations WHERE id = ?", (item_id,))
        conn.commit()
        return cursor.rowcount > 0


def clear_all_history() -> bool:
    """Clears all translation history."""
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM translations")
        conn.commit()
        return True


def toggle_favorite(item_id: int) -> Optional[int]:
    """Toggles bookmark/favorite status."""
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE translations
            SET is_favorite = CASE WHEN is_favorite = 1 THEN 0 ELSE 1 END
            WHERE id = ?
        """, (item_id,))
        conn.commit()
        
        cursor.execute("SELECT is_favorite FROM translations WHERE id = ?", (item_id,))
        row = cursor.fetchone()
        return row["is_favorite"] if row else None


def find_cached_translation(source_text: str, source_lang: str = "English", target_lang: str = "Tamil") -> Optional[str]:
    """Finds a previously saved translation from SQLite cache (essential for zero-latency offline mode)."""
    if not source_text:
        return None
    init_db()
    cleaned = str(source_text).strip()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT translated_text FROM translations
            WHERE LOWER(TRIM(source_text)) = LOWER(?)
              AND (LOWER(target_lang) = LOWER(?) OR target_lang = ?)
            ORDER BY id DESC LIMIT 1
        """, (cleaned, target_lang, target_lang))
        row = cursor.fetchone()
        return row["translated_text"] if row else None


# --- Settings & API Key Operations ---

def get_setting(key: str, default: str = "") -> str:
    """Retrieves a persistent setting value."""
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM app_settings WHERE key = ?", (key,))
        row = cursor.fetchone()
        return row["value"] if row else default


def set_setting(key: str, value: str):
    """Sets a persistent configuration key-value pair."""
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO app_settings (key, value, updated_at)
            VALUES (?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(key) DO UPDATE SET value = excluded.value, updated_at = CURRENT_TIMESTAMP
        """, (key, value))
        conn.commit()


def get_all_settings() -> Dict[str, str]:
    """Returns all settings with masked API key for security."""
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT key, value FROM app_settings")
        raw = {row["key"]: row["value"] for row in cursor.fetchall()}
    
    # Mask API key if set
    api_key = raw.get("gemini_api_key", "")
    masked_key = ""
    if api_key:
        masked_key = f"{api_key[:6]}...{api_key[-4:]}" if len(api_key) > 10 else "******"

    return {
        "network_mode": raw.get("network_mode", "auto"),
        "has_api_key": bool(api_key),
        "masked_api_key": masked_key,
        "translator_provider": raw.get("translator_provider", "auto")
    }


# --- Safe Interactive SQL Query Studio ---

def run_custom_query(sql_query: str, params: Optional[tuple] = None) -> Dict[str, Any]:
    """
    Executes a SELECT SQL query with a SQLite cursor.
    Restricted to read-only statements for safety.
    """
    init_db()
    cleaned = (sql_query or "").strip()
    
    # Security check: Only allow SELECT, EXPLAIN, or PRAGMA statements
    upper = cleaned.upper()
    if not (upper.startswith("SELECT") or upper.startswith("PRAGMA") or upper.startswith("EXPLAIN")):
        return {
            "success": False,
            "error": "Security restriction: Only read-only SELECT or PRAGMA queries are permitted in the SQL Studio.",
            "columns": [],
            "rows": [],
            "row_count": 0
        }

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(cleaned, params or ())
            
            columns = [desc[0] for desc in cursor.description] if cursor.description else []
            rows = cursor.fetchall()
            
            data = []
            for r in rows:
                row_dict = {}
                for idx, col in enumerate(columns):
                    row_dict[col] = r[idx]
                data.append(row_dict)

            return {
                "success": True,
                "columns": columns,
                "rows": data[:100],  # safety limit 100 rows
                "row_count": len(rows),
                "query": cleaned
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "columns": [],
            "rows": [],
            "row_count": 0
        }


# --- Database Diagnostics & CSV Export ---

def get_db_info() -> Dict[str, Any]:
    """Returns database size, table statistics, and active connection info."""
    init_db()
    file_size = 0
    if os.path.exists(DB_PATH):
        file_size = os.path.getsize(DB_PATH)

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM translations")
        total_rows = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM translations WHERE is_favorite = 1")
        starred_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(DISTINCT target_lang) FROM translations")
        languages_count = cursor.fetchone()[0]

        cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='translations'")
        schema_row = cursor.fetchone()
        schema_sql = schema_row[0] if schema_row else ""

        # Check total tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
        tables = [r[0] for r in cursor.fetchall()]

    return {
        "database_file": os.path.abspath(DB_PATH),
        "database_engine": "SQLite 3",
        "file_size_bytes": file_size,
        "file_size_kb": round(file_size / 1024, 2),
        "total_records": total_rows,
        "starred_records": starred_count,
        "distinct_target_languages": languages_count,
        "tables": tables,
        "schema_sql": schema_sql
    }


def export_as_csv() -> str:
    """Exports all rows as a CSV formatted string."""
    rows = get_all_rows()
    output = io.StringIO()
    if rows:
        writer = csv.DictWriter(output, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    return output.getvalue()
