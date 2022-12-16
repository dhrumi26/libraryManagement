import mysql.connector
from main import listadd
import main
connection = mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="root123",
                                         database="library")
print(connection)
mycursor= connection.cursor()
main.func3(listadd)
sql="INSERT into total(name,bookname) values(%s,%s)"
mycursor.executemany(sql,listadd)
connection.commit()