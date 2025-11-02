CREATE TABLE IF NOT EXISTS count (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    page_name TEXT,
    created_at TEXT,
    x_forwarded TEXT,
    country TEXT,
    user_agent TEXT,
    languages TEXT,
    referrer TEXT
)