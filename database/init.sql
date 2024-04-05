CREATE TABLE users (
    username VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255)
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    distance FLOAT,
    init_point VARCHAR(255),
    grade FLOAT,
    difficulty VARCHAR(255),
    type VARCHAR(255),
    user_id VARCHAR(255) REFERENCES users(username)
);


INSERT INTO users (username, password) VALUES
('usuario1', 'password1'),
('usuario2', 'password2'),
('usuario3', 'password3'),
('usuario4', 'password4'),
('usuario5', 'password5'),
('usuario6', 'password6');


INSERT INTO activities (name, distance, init_point, grade, difficulty, type, user_id) VALUES
('Correr en el parque', 5.0, 'Parque Central', 4.5, 'Moderada', 'Correr', 'usuario1'),
('Caminar por la playa', 3.0, 'Playa Principal', 3.8, 'Fácil', 'Caminar', 'usuario2'),
('Bicicleta en la montaña', 10.0, 'Ruta de la Montaña', 4.2, 'Moderada', 'Bicicleta', 'usuario3'),
('Senderismo en el bosque', 8.0, 'Sendero Principal', 4.7, 'Difícil', 'Senderismo', 'usuario4'),
('Natación en la piscina', 1.5, 'Piscina Municipal', 4.0, 'Moderada', 'Natación', 'usuario5'),
('Entrenamiento en el gimnasio', 0.0, 'Gimnasio Local', 3.5, 'Fácil', 'Entrenamiento', 'usuario6');