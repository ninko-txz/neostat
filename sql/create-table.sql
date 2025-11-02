CREATE TABLE IF NOT EXISTS count (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    page_name TEXT,
    created_at TEXT,
    remote_addr TEXT,
    user_agent TEXT,
    languages TEXT,
    referrer TEXT
)