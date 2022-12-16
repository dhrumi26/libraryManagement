import mysql.connector
import main
connection = mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="root123",
                                         database="library")
print(connection)
mycursor= connection.cursor()
main.func2()
s1= "DELETE FROM lend WHERE name=@a and bname=@b"

