import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anmol@359",
    database="finance_system"
)

cursor = conn.cursor()