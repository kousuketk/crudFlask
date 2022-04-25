DROP DATABASE IF EXISTS testdb;
CREATE DATABASE testdb;
USE testdb;

DROP TABLE IF EXISTS users;
CREATE TABLE users(
  id int NOT NULL AUTO_INCREMENT,
  name varchar(255) NOT NULL,
  email varchar(255) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO users(id, name, email) VALUES(1, 'test_user1', 'test_email1');
INSERT INTO users(id, name, email) VALUES(2, 'test_user2', 'test_email2');