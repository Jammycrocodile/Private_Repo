use hundundco;
insert into clients (vorname,nachname,ort, mail, telefonnummer, aboanzahl, hundename) values 
('Franziska', 'Oberholzer', 'ZH', NULL, NULL, NULL, NULL),
('Christina', 'Pollina-Roos', 'ZH', NULL, NULL, NULL, NULL),
('Krisztina', 'Barath', 'ZH', NULL, NULL, NULL, NULL),
('Ursi', 'Herren', 'ZH', 'ursi.herren@gmx.ch', '+41788626911', NULL, NULL),
('Claudia', 'Walz', 'ZH', NULL, NULL, 6, NULL),
('Patricia', 'Suter', 'ZH', 'patricia_suter14@hotmail.com', '+41797411880', NULL, NULL),
('Erika', 'Ehing', 'ZH', 'erika.ehing@gewandhaus.ch', '+41787785040', NULL, NULL),
('Michaela', 'Götze', 'ZH', NULL, NULL, 2, NULL),
('Nina', 'Schweizer', 'ZH', 'nina.schweizer@gmx.ch', NULL, NULL, NULL),
('Fabienne', 'Brunner', 'ZH', NULL, NULL, NULL, NULL),
('Sonja', 'Hoffmann', 'ZH', 'Sonja_hofmann@hotmail.com', '+41786464106', 8, NULL),
('Giada', 'Schiavone', 'ZH', NULL, NULL, 1, NULL),
('Achim', 'Halm', 'ZH', NULL, NULL, NULL, NULL),
('veronica', 'Villanueva Pereira', 'ZH', NULL, '+41799123849', NULL, NULL),
('Shouq', 'Hussein', 'ZH', NULL, NULL, NULL, NULL),
('Manuela', 'Miksa', 'ZH', 'manumiksa@proton.me', '+41763069754', 8, NULL),
('Maya', 'Matzenauer','ZH', NULL, NULL, NULL, NULL),
('Alexandra', 'Walker', 'ZH', NULL, NULL, 1, NULL),
('Claudia', 'Schwager', 'ZH', NULL, NULL, 2, NULL),
('Petra', 'Jenzer', 'ZH', 'p_jenzer@yahoo.de', '+41797286233', 3, NULL),
('Kate', 'Kosten', 'ZH', NULL, NULL, 5, NULL),
('Michial', 'Klootwijk', 'ZH', NULL, NULL, NULL, NULL),
('Wakatsuki', 'Manami', 'ZH', NULL, NULL, NULL, NULL),
('Amy', 'Ellmalavany', 'ZH', 'amy_jonhson@hotmail.com', '+41765170703', 10, NULL),
('Stefano', '', 'ZH', NULL, NULL, NULL, NULL),
('Rahel', 'Hotz', 'ZH', NULL, NULL, 3, NULL),
('Sonia', 'Canelada', 'ZH', NULL, NULL, NULL, NULL),
('Cristina', 'Poiata', 'ZH', NULL, '+41798305813', NULL, NULL),
('Manuela', 'Leinberger', 'ZH', NULL, '+41793260484', NULL, NULL),
('Adriana', '', 'ZH', NULL, '+41763754556', NULL, NULL),
('Katja', 'Schlösser', 'ZH', NULL, NULL, NULL, NULL),
('Karin', 'Wenger', 'ZH', 'karinwenger@gmx.net', '+41797569269', NULL, NULL),
('Luisa', 'Heine', 'ZH', NULL, NULL, 2, NULL),
('Michele', 'Seligmann', 'ZH', NULL, NULL, NULL, NULL),
('Michaela', 'Heinzelmann', 'ZH', 'michaela0507@gmx.ch', '+41794575254', NULL, NULL),
('Dalila', 'Anker', 'ZH', NULL, '+41772655425', NULL, NULL),
('Vera', 'Maag', 'ZH', NULL, NULL, NULL, NULL),
('Ilksen', 'Kirmizikaya', 'ZH', NULL, NULL, NULL, NULL),
('Josephine', 'Heinzelmann', 'ZH', 'josephine.heinzelmann@gmail.com', '+41787702009', NULL, NULL),
('Maya', '', 'ZH', NULL, '+41775366586', NULL, NULL),
('Nadja', 'Stickl', 'ZH', NULL, NULL, NULL, NULL),
('Linda', '', 'ZH', NULL, '+41786710869', NULL, NULL);


insert into kurse (kurse, preis) values
('Gruppenkurs', 45),
('Privatkurs', 120),
('Rückruftraining', 20),
('Verhaltenstherapie', 150),
('Hausbesuch', 120),
('Online Kurs', 120);

insert into kursbesuch (client_id, kurs_id, kursdatum, kursbezahlt, kursdauer_in_min) values
(2, 1, '2024-04-03 00:00:00', FALSE, 60), #Christina
(3, 1, '2024-02-07 00:00:00', FALSE, 60), #Krisztina Barath
(3, 1, '2024-03-06 00:00:00', FALSE, 60), #Krisztina Barath
(3, 1, '2024-03-08 00:00:00', FALSE, 60), #Krisztina Barath
(3, 1, '2024-03-20 00:00:00', FALSE, 60), #Krisztina Barath
(3, 1, '2024-04-03 00:00:00', FALSE, 60), #Krisztina Barath
(4, 1, '2024-04-03 00:00:00', FALSE, 60), #Ursi Herren
(6, 1, '2024-03-08 00:00:00', FALSE, 60), #Patricia Suter
(6, 1, '2024-04-03 00:00:00', FALSE, 60), #Patricia Suter
(6, 1, '2024-04-05 00:00:00', FALSE, 60), #Patricia Suter
(7, 1, '2024-03-20 00:00:00', FALSE, 60), #Erika Ehing
(17, 2, '2024-01-29 00:00:00', FALSE, 75), #Maya Matzenauer
(17, 2, '2024-04-06 00:00:00', FALSE, 120), #Maya Matzenauer
(17, 2, '2024-04-25 00:00:00', FALSE, 65), #Maya Matzenauer
(17, 1, '2024-03-05 00:00:00', FALSE, 60), #Maya Matzenauer (Gruppenkurs)
(17, 1, '2024-04-09 00:00:00', FALSE, 60), #Maya Matzenauer (Gruppenkurs)
(27, 1, '2024-09-19 00:00:00', FALSE, 60), #Sonia Canelada
(28, 4, '2024-01-30 00:00:00', FALSE, 60), #Cristina
(28, 4, '2024-04-23 00:00:00', FALSE, 120), #Cristina
(36, 2, '2024-02-14 00:00:00', FALSE, 60), #Dalila Anker
(37, 4, '2024-02-14 00:00:00', FALSE, 60), #Vera Maag
(37, 4, '2024-03-17 00:00:00', FALSE, 60), #Vera Maag
(39, 1, '2024-04-09 00:00:00', FALSE, 60), #Josephine Heinzelmann
(40, 5, '2024-03-12 00:00:00', FALSE, 20), #Maya (Online)
(41, 4, '2024-03-13 00:00:00', FALSE, 60), #Nadja Stickl
(42, 5, '2024-03-15 00:00:00', FALSE, 60), #Linda
(42, 2, '2024-03-18 00:00:00', FALSE, 90), #Linda
(42, 2, '2024-04-02 00:00:00', FALSE, 75), #Linda
(42, 2, '2024-04-11 00:00:00', FALSE, 75), #Linda
(42, 2, '2024-04-26 00:00:00', FALSE, 60), #Linda
(42, 1, '2024-04-03 00:00:00', FALSE, 60); #Linda (Gruppenkurs)

insert into rechnungen (client_id, rechnungsdatum, rechnung_bezahlt) values
(3, '2024-04-26', FALSE), #Krisztina
(6, '2024-04-26', FALSE), #Patricia
(17, '2024-04-26', FALSE), #Maya Matzenauer
(28, '2024-04-26', FALSE), #Cristina
(36, '2024-04-26', FALSE), #Dalila
(37, '2024-04-26', FALSE), #Vera Maag
(39, '2024-04-26', FALSE), #Josephie Heinzelmann
(40, '2024-04-26', FALSE), #Maya (Online)
(41, '2024-04-26', FALSE), #Nadja Stickl
(42, '2024-04-26', FALSE); #Linda



