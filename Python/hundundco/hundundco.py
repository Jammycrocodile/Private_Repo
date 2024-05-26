#Mysql connection modules
import mysql.connector
from mysql.connector import Error

# Try-catch block for testing the connection to the database
try:
    connection = mysql.connector.connect(
        host='172.19.158.26',
        database='hundundco',
        user='admin',
        password='Cr3ative'
    )

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    


