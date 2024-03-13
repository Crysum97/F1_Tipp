CREATE TABLE IF NOT EXISTS user (
    id INTEGER primary key AUTOINCREMENT,
    name VARCHAR unique,
    pass_hash VARCHAR(256),
    salt VARCHAR,
    last_login DATETIME
);

CREATE TABLE IF NOT EXISTS team (
    id INTEGER primary key AUTOINCREMENT,
    name VARCHAR unique
);

CREATE TABLE IF NOT EXISTS driver (
    id INTEGER primary key AUTOINCREMENT,
    first_name VARCHAR,
    last_name VARCHAR,
    fk_team INTEGER,
    FOREIGN KEY(fk_team) REFERENCES team(id)
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
INSERT INTO team (name) VALUES ("Williams");

DELETE FROM driver;

INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Charles", "Leclerc", 1);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Carlos", "Sainz", 1);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Lewis", "Hamilton", 2);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("George", "Russel", 2);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Max", "Verstappen", 3);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Sergio", "Perez", 3);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Lando", "Norris", 4);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Oscar", "Pisatri", 4);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Fernando", "Alonso", 5);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Lance", "Stroll", 5);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Pierre", "Gasly", 6);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Esteban", "Ocon", 6);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Daniel", "Ricciardo", 7);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Yuki", "Tsunoda", 7);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Valtteri", "Bottas", 8);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Guanyu", "Zhou", 8);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Nico", "Hülkenberg", 9);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Kevin", "Magnussen", 9);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Alexander", "Albon", 10);
INSERT INTO driver (first_name, last_name, fk_team) VALUES ("Logan", "Sargeant", 10);
