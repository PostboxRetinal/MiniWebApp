CREATE DATABASE myflaskapp;
use myflaskapp;

CREATE TABLE users (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(255),
    email varchar(255),
    username varchar(255),
    password varchar(255)
);

CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
);

INSERT INTO users VALUES(null, "juan", "juan@gmail.com", "juan", "123"),
    (null, "maria", "maria@gmail.com", "maria", "456");

INSERT INTO product (name, description, price) VALUES
    ('openSUSE', 'Una distro de Linux muy god', 5000),
    ('Debian', 'Una distro de Linux muy estable', 3500),
    ('Manjaro', 'Una distro de Linux muy amigable', 3100);