DROP TABLE IF EXISTS Employees;
CREATE TABLE Employees (
Employee_ID varchar(50) PRIMARY KEY NOT NULL,
First_Name varchar(30),
Last_Name varchar(30),
Street_Address varchar(50),
City varchar(30),
State_Code varchar(30),
Zip_Code varchar(30),
Role varchar(30),
Role_Type varchar(30),
Salary integer,
Age integer,
Years_at_Company decimal,
Benefit_401k BOOLEAN,
Contribution_401k decimal,
Benefit_Dental BOOLEAN,
Benefit_Vision BOOLEAN,
Benefit_Medical BOOLEAN,
Miles_to_Work decimal,
Remote_Employee BOOLEAN,
Current_Employee BOOLEAN
);

DROP TABLE IF EXISTS Responses;
CREATE TABLE Responses (
Response_ID varchar(50) PRIMARY KEY NOT NULL,
Question_ID varchar(50) NOT NULL,
Employee_ID varchar(50) NOT NULL,
Response integer
);

DROP TABLE IF EXISTS Questions;
CREATE TABLE Questions(
Question_ID varchar(50) PRIMARY KEY NOT NULL,
Question varchar (150) NOT NULL
);