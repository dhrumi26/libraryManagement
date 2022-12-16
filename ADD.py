import mysql.connector
from main import lended_books
from main import listlend
import main
# import db
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="root123",
                                         database="library")
print(connection)
mycursor= connection.cursor()
# sqlform= "INSERT INTO total (name,bookname) values (%s,%s)"
# total1=(("Dhrumi","romeo"),("Dhrumi","juliet"),("Dhrumi","heer"),("Dhrumi","ranja"),)
# mycursor.executemany(sqlform,total1)


main.func1(listlend)

sqlform= "INSERT INTO lend(name,bname) VALUES (%s,%s)"
print(listlend)
mycursor.executemany(sqlform,listlend)

connection.commit()
# a= mycursor.execute("Show tables")
# for a in mycursor:
#     print(a)