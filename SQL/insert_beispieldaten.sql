use hundundco;

-- Beispieldaten für die Tabelle clients
INSERT INTO clients (vorname, nachname, ort, aboanzahl, telefonnummer) VALUES
('Max', 'Mustermann', 'ZH', 2, '0123456789'),
('Anna', 'Schmidt', 'AG', NULL, '9876543210'),
('Peter', 'Meier', 'ZH', 1, '1234567890');

-- Beispieldaten für die Tabelle kurse
INSERT INTO kurse (kurse, preis) VALUES
('Yoga-Kurs', 50.00),
('Pilates-Kurs', 40.00),
('Fitness-Kurs', 60.00);

-- Beispieldaten für die Tabelle Kursbesuch
INSERT INTO kursbesuch (client_id, kurs_id, reservationsdatum, kursdatum, kursbezahlt) VALUES
(1, 1, '2024-05-01 10:00:00', '2024-05-01 10:30:00', TRUE),
(1, 2, '2024-05-02 11:00:00', '2024-05-02 11:30:00', FALSE),
(2, 1, '2024-05-03 10:00:00', '2024-05-03 10:30:00', TRUE),
(3, 3, '2024-05-04 09:00:00', '2024-05-04 09:30:00', FALSE);

-- Beispieldaten für die Tabelle abokauf
INSERT INTO abokauf (client_id, eingekauft, abobezahlt) VALUES
(1, 5, FALSE),
(2, 10, TRUE),
(3, 5, FALSE);

INSERT INTO rechnungen (client_id, rechnungsdatum, rechnung_bezahlt) VALUES
(1, '2024-05-01 10:00:00', FALSE),
(1, '2024-05-10 11:00:00', FALSE),
(2, '2024-05-15 09:00:00', TRUE),
(3, '2024-05-20 08:00:00', FALSE),
(3, '2024-05-25 14:00:00', FALSE),
(3, '2024-05-30 12:00:00', TRUE);
