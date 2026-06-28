CREATE TABLE settings (
    setting_id     INTEGER PRIMARY KEY,
    parameter_name TEXT NOT NULL UNIQUE,
    language_id    INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY(language_id) REFERENCES languages(language_id)
);
