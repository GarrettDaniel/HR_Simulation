DROP TABLE IF EXISTS Employees;
CREATE TABLE Employees (
Employee_ID varchar(30) PRIMARY KEY NOT NULL,
First_Name varchar(30),
Last_Name varchar(30),
Address varchar(30),
Role varchar(30),
Role_Type varchar(30),
Salary integer,
Age integer,
Years_at_Company decimal,
Current_Employee BOOLEAN
);

DROP TABLE IF EXISTS Responses;
CREATE TABLE Responses (
Response_ID varchar(30) PRIMARY KEY NOT NULL,
Question_ID varchar(30) NOT NULL,
Employee_ID varchar(30) NOT NULL,
Response varchar(30)
);

DROP TABLE IF EXISTS Questions;
CREATE TABLE Questions(
Question_ID varchar(50) PRIMARY KEY NOT NULL,
Question varchar (150) NOT NULL
);