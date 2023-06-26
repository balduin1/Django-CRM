import psycopg2

database = psycopg2.connect(
    host="localhost",
    database="dbdcrm",
    user="postgres",
    password="ingenieria1*",
    port="5433"
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE dbdcrm")

print("all done")