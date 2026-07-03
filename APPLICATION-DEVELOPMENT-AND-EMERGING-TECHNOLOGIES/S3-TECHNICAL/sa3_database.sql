CREATE DATABASE sa3_database;

USE sa3_database;

CREATE TABLE users (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    birthday VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    contact VARCHAR(20) NOT NULL
);