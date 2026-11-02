CREATE DATABASE IF NOT EXISTS college;
USE college;

DROP TABLE IF EXISTS Faculty;
CREATE TABLE Faculty (
    FacultyID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Salary INT
);

INSERT INTO Faculty VALUES
(1,'Asha','Computer',50000),
(2,'Ravi','IT',55000),
(3,'Neha','Computer',60000),
(4,'Kiran','Electronics',52000),
(5,'Meera','IT',58000);

SELECT * FROM Faculty;
