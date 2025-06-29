-- setup_mysql_test.sql
-- SQL script to set up the test database and user for AirBnB clone v2

DROP DATABASE IF EXISTS hbnb_test_db;
CREATE DATABASE hbnb_test_db;
USE hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
