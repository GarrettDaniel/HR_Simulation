import psycopg2
import pandas as pd
import boto3

## Get DB Credentials from SSM

ssm = boto3.client('ssm')

DB_NAME = ssm.get_parameter(Name='DB_NAME')['Parameter']['Value'] ## Figure out what went wrong here
DB_ENDPOINT = ssm.get_parameter(Name='DB_ENDPOINT')['Parameter']['Value']
DB_USER = ssm.get_parameter(Name='DB_USER')['Parameter']['Value']
DB_PASS = ssm.get_parameter(Name='DB_PASS')['Parameter']['Value']
PORT = 5432

connection = psycopg2.connect(
    host = DB_ENDPOINT,
    port = PORT,
    user = DB_USER,
    password = DB_PASS,
    database = DB_NAME
)

cursor = connection.cursor()