import mysql.connector
from mysql.connector import Error

# database is only available to code running on pythonanywhere
try:
    connection = mysql.connector.connect(host='Kyber.mysql.pythonanywhere-services.com',

                                         database='Kyber$default',
                                         user='Kyber',
                                         password='5iQItY4$MPWNH!Y')
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
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")