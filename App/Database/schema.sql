CREATE TABLE IF NOT EXISTS user (
    id INTEGER primary key AUTOINCREMENT,
    name VARCHAR unique,
    pass_hash VARCHAR(256),
    salt VARCHAR,
    last_login DATETIME
);

CREATE TABLE IF NOT EXISTS team (
    id INTEGER primary key AUTOINCREMENT,
    name VARECHAR unique
);

DELETE FROM team;

INSERT INTO team (name) VALUES ("Ferrari");
INSERT INTO team (name) VALUES ("Mercedes");
INSERT INTO team (name) VALUES ("Red Bull");
INSERT INTO team (name) VALUES ("McLaren");
INSERT INTO team (name) VALUES ("Aston Martin");
INSERT INTO team (name) VALUES ("Alpine");
INSERT INTO team (name) VALUES ("Racing Bulls");
INSERT INTO team (name) VALUES ("Sauber");
INSERT INTO team (name) VALUES ("Haas");
