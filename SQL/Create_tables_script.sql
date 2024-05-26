USE hundundco;


DROP TABLE IF EXISTS kursbesuch;
DROP TABLE IF EXISTS abokauf;
DROP TABLE IF EXISTS rechnungen;
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS kurse;


CREATE TABLE clients
(
    client_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    vorname	VARCHAR(30) NOT NULL,
    nachname VARCHAR(30),
    ort Enum('ZH','AG') NOT NULL,
    aboanzahl INT UNSIGNED DEFAULT NULL,
    mail varchar(255) UNIQUE,
    hundename varchar(30),
    telefonnummer VARCHAR(30)
);

CREATE TABLE kurse
(
	kurs_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    kurse CHAR (20) NOT NULL,
    preis DECIMAL(10, 2) UNSIGNED NOT NULL
);

CREATE TABLE kursbesuch
(
	kursbesuch_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    client_id INT UNSIGNED NOT NULL,
	kurs_id INT UNSIGNED NOT NULL,
    kursdatum DATETIME NOT NULL,
    kursdauer_in_min INT NOT NULL DEFAULT 60,
    kursbezahlt BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (client_id) REFERENCES clients (client_id),
    FOREIGN KEY (kurs_id) REFERENCES kurse (kurs_id)
);

CREATE TABLE abokauf

(
	abokauf_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    client_id INT UNSIGNED NOT NULL,
    eingekauft INT UNSIGNED NOT NULL,
    abobezahlt BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (client_id) REFERENCES clients (client_id),
    CHECK (eingekauft IN (5, 10))
);

CREATE TABLE rechnungen
(
	rechnungs_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    client_id INT UNSIGNED NOT NULL,
	rechnungsdatum DATE NOT NULL,
    rechnung_bezahlt BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (client_id) REFERENCES clients (client_id)
);