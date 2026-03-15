CREATE TABLE tags (
    tag_id        INTEGER PRIMARY KEY,
    tag_key       TEXT NOT NULL UNIQUE,
    created_at    TEXT,
    updated_at    TEXT,
    deleted_at    TEXT
);
