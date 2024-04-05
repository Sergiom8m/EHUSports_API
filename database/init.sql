CREATE TABLE users (
    username VARCHAR(255),
    password VARCHAR(255),
    PRIMARY KEY(username)
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    distance FLOAT,
    init_point VARCHAR(255),
    grade FLOAT,
    difficulty VARCHAR(255),
    type VARCHAR(255),
    user_id VARCHAR(255)
);

