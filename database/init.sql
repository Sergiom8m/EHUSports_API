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