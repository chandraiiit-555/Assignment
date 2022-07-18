"""
We are using MySQL connected python library to establish a connection between Python code and mysql database.
"""
import mysql.connector # importing the mysql connector, will give ImportError if not installed in the machine.

DB_HOST_NAME = "localhost" # Database host name ( Please mention your database host here)
DB_USERNAME = "chandra" # Database username ( Please mention your mysql database username)
DB_PASSWORD = "Chandra$123" # Database password ( Please mention your mysql database password)

db_conn = mysql.connector.connect(host=DB_HOST_NAME,user=DB_USERNAME,password=DB_PASSWORD)
db_cursor = db_conn.cursor()

# create database
db_cursor.execute("CREATE DATABASE assignment")

#db_cursor.execute("SHOW DATABASES")

# create table
#db_cursor.execute("CREATE TABLE Tasks (task_id INT AUTO_INCREMENT PRIMARY KEY, task_name VARCHAR(255))")


