-- setup_mysql_test.sql
-- SQL script to set up the test database and user for AirBnB clone v2

DROP DATABASE IF EXISTS hbnb_test_db;
CREATE DATABASE hbnb_test_db;
USE hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

-- Create 'places' table for testing
CREATE TABLE IF NOT EXISTS places (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    city_id VARCHAR(60) NOT NULL,
    user_id VARCHAR(60) NOT NULL,
    name VARCHAR(128) NOT NULL,
    description VARCHAR(1024),
    number_rooms INT DEFAULT 0,
    number_bathrooms INT DEFAULT 0,
    max_guest INT DEFAULT 0,
    price_by_night INT DEFAULT 0,
    latitude FLOAT,
    longitude FLOAT,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);
