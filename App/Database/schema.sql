CREATE TABLE IF NOT EXISTS user (
    id INTEGER primary key AUTOINCREMENT,
    name VARCHAR unique,
    pass_hash VARCHAR(256),
    salt VARCHAR,
    last_login DATETIME
);