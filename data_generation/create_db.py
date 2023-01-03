import psycopg2
import pandas as pd
import boto3

## Get DB Credentials from SSM

ssm = boto3.client('ssm')

DB_NAME = ssm.get_parameter(Name='DB_NAME')['Parameter']['Value'] 
DB_ENDPOINT = ssm.get_parameter(Name='DB_ENDPOINT')['Parameter']['Value']
DB_USER = ssm.get_parameter(Name='DB_USER')['Parameter']['Value']
DB_PASS = ssm.get_parameter(Name='DB_PASS')['Parameter']['Value']
PORT = 5432

## Create DB Connection to RDS PostgreSQL DB

connection = psycopg2.connect(
    host = DB_ENDPOINT,
    port = PORT,
    user = DB_USER,
    password = DB_PASS,
    database = DB_NAME
)

cursor = connection.cursor()

## Create Tables using separate SQL file

base_filepath = "/home/ec2-user/environment/hr_survey_simulation/data_generation/"
filename = "create_tables.sql"
sql_filename = base_filepath + filename

with open(sql_filename, 'r') as sql_file:
    cursor.execute(sql_file.read())
    
connection.commit()

## Add data from the dataframes or CSVs into the database tables
## Use this as ref: https://towardsdatascience.com/amazon-rds-step-by-step-guide-14f9f3087d28

base_data_filepath = "/home/ec2-user/environment/hr_survey_simulation/data/"

## Part 1: Add data to employees table

employees_csv = "employees.csv"
employees_filepath = base_data_filepath + employees_csv

with open(employees_filepath, 'r') as employees:
    next(employees)
    cursor.copy_from(employees, 'employees', sep=',')

## Part 2: Add data to responses table

responses_csv = "responses.csv"
responses_filepath = base_data_filepath + responses_csv

with open(responses_filepath, 'r') as responses:
    next(responses)
    cursor.copy_from(responses, 'responses', sep=',')

## Part 3: Add data to questions table

questions_csv = "questions.csv"
questions_filepath = base_data_filepath + questions_csv

with open(questions_filepath, 'r') as questions:
    next(questions)
    cursor.copy_from(questions, 'questions', sep=',')
    
connection.commit()

connection.close()