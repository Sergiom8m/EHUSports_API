CREATE TABLE users (
    username VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255),
    profile_image TEXT
);

CREATE TABLE activities (
    id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    distance FLOAT,
    init_point VARCHAR(255),
    grade FLOAT,
    difficulty VARCHAR(255),
    type VARCHAR(255),
    user_id VARCHAR(255) REFERENCES users(username)
);

CREATE TABLE tokens (
    token VARCHAR(255) PRIMARY KEY
);

INSERT INTO users (username, password) VALUES
('ehuser', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
('sergio', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92');

INSERT INTO activities (id, name, distance, init_point, grade, difficulty, type, user_id) VALUES
('1', 'Argalario desde La Arboleda', 5.2, 'La Arboleda', 123, 'Easy', 'Walking', 'ehuser'),
('2', 'El Regato', 15.2, 'Plaza de Cruces', 53, 'Easy', 'Walking', 'ehuser'),
('3', 'Eretza', 17.67, 'Sodupe', 1012, 'Hard', 'Walking', 'ehuser'),
('4', 'Ruta del Nervión', 30.5, 'Bilbao', 210, 'Moderate', 'Walking', 'ehuser'),
('5', 'Paseo por el Casco Viejo', 3.1, 'Plaza Nueva', 50, 'Easy', 'Walking', 'ehuser'),
('6', 'Ruta del Flysch', 25.6, 'Zumaia', 320, 'Moderate', 'Walking', 'ehuser'),
('7', 'Ruta de los Acantilados', 12.8, 'San Sebastián', 180, 'Moderate', 'Walking', 'ehuser'),
('8', 'Sendero de la Costa de Gijón', 8.7, 'Playa de San Lorenzo', 120, 'Moderate', 'Walking', 'ehuser'),
('9', 'Ruta de los 7 Puentes', 10.2, 'Puente de los Tirantes', 85, 'Easy', 'Walking', 'ehuser'),
('10', 'Caminata por el Parque Natural de Urkiola', 15.5, 'Centro de Interpretación de Urkiola', 300, 'Moderate', 'Walking', 'ehuser'),

('11', 'Usansolo desde Bilbao', 42.8, 'Plaza de Moyua', 57, 'Hard', 'Cycling', 'sergio'),
('12', 'La Arena hondartza', 22.4, 'Portugalete', 88, 'Easy', 'Cycling', 'ehuser'),
('13', 'Galdames desde Ortuella', 34.7, 'Ortuella', 124, 'Moderate', 'Cycling', 'ehuser'),
('14', 'Vía Verde de Plazaola', 45.3, 'Irún', 430, 'Moderate', 'Cycling', 'sergio'),
('15', 'Recorrido por la Ría de Bilbao', 18.7, 'Museo Guggenheim', 75, 'Moderate', 'Cycling', 'sergio'),
('16', 'Circuito por el Parque de Doña Casilda', 6.5, 'Parque de Doña Casilda', 40, 'Easy', 'Cycling', 'sergio'),
('17', 'Ruta de los Molinos de Viento', 35.2, 'Donostia-San Sebastián', 480, 'Hard', 'Cycling', 'ehuser'),

('18', 'Gallaraga desde la Quadra', 9.77, 'La Quadra', 998, 'Hard', 'Running', 'ehuser'),
('19', 'Mendibil + Argalario', 17.32, 'Trapagaran', 554, 'Moderate', 'Running', 'ehuser'),
('20', 'Pico La Cruz', 9.77, 'Ekoetxea, Peñas Negras', 432, 'Moderate', 'Running', 'sergio'),
('21', 'Subida al Txindoki', 8.2, 'Lizarrusti', 756, 'Hard', 'Running', 'sergio'),
('22', 'Ascensión al Monte Gorbea', 17.9, 'Murua', 920, 'Hard', 'Running', 'sergio'),
('23', 'Ruta por el Monte Artxanda', 10.4, 'Funicular de Artxanda', 180, 'Moderate', 'Running', 'sergio'),
('24', 'Carrera en el Parque de Etxebarria', 5.2, 'Parque de Etxebarria', 60, 'Easy', 'Running', 'ehuser');
