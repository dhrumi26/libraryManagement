import mysql.connector
# import main
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="root123")
# print(connection)
mycursor= connection.cursor()
mycursor.execute("Create database testnew")
mycursor.execute("Create table total1(name varchar(50), bookname int(60)")
mycursor.execute("Create table total2(name varchar(100), bname varchar(100))")
