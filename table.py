import mysql.connector
import main
# import db
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="root123",
                                         database="library")
print(connection)
mycursor= connection.cursor()
mycursor.execute("Create table total(name varchar(200), bookname varchar(200))")
# sqlform= "INSERT INTO total (name,bookname) values (%s,%s)"
# total1=(("Dhrumi","romeo"),("Dhrumi","juliet"),("Dhrumi","heer"),("Dhrumi","ranja"),)
# mycursor.executemany(sqlform,total1)
# a= mycursor.execute("Show tables")
# for a in mycursor:
#     print(a)