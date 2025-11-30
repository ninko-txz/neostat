CREATE TABLE IF NOT EXISTS count (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT,
    path TEXT,
    x_forwarded TEXT,
    country TEXT,
    user_agent TEXT,
    languages TEXT
)