CREATE DATABASE dog_database;

USE dog_database;

CREATE TABLE dog_information (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    d_name VARCHAR(50) NOT NULL,
    d_breed VARCHAR(50) NOT NULL,
    d_age VARCHAR(30) NOT NULL,
    d_add VARCHAR(100) NOT NULL,
    d_color VARCHAR(30) NOT NULL,
    d_height VARCHAR(30) NOT NULL,
    d_weight VARCHAR(30) NOT NULL
);