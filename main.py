# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
import json

listbooks=[]
addeddict={}
lenddict={}
lended_books={}
listlend=[]
listadd=[]
print(listlend)
# listlend= list(lended_books.items())
# if __name__ == '__main__':
class library:
    def __init__(self,name,list):
        self.name=name
        self.books=list


    def display_book(self):
        print(allthebook)
    def lend_book(self):
        print("enter your name")
        a=input()
        print("enter the book you want to lend")
        b=input()
        count1=b in lended_books.values()
        if(count1=="True"):
            print("sorry,you canot lend this book")
        else:
            lended_books.update({a:b})
            in1=int(allthebook.index(b))
            allthebook.pop(in1)
            lenddict.update({a:b})
                #print(lenddict)
    def return_book(self):
        print("enter your name")
        a=input()
        print("enter the book name you want to return")
        c=input()
        count2=listlend.count(c)
        if(count2>0):
            pop_item=int(lended_books.index(c))
            lended_books.pop(pop_item)
            allthebook.append(c)
            lenddict.pop(a)
                #print(dict)
        else:
            listbooks.append(c)
                #print(listbooks)
            allthebook.extend(listbooks)
            addeddict.update({a:c})
            print(addeddict)
                #print(dict)
               # print(allthebook)
            print("thank you for returning")
    def add_book(self):
        print("enter your name")
        a=input()
        print("enter the book name you want to add")
        d=input()
        listbooks.append(d)
            #print(listbooks)
        allthebook.extend(listbooks)
            #print(allthebook)
        addeddict.update({a:d})
        print(addeddict)
        print("thank you for adding the book")
allthebook=["romeo","juliet","heer","ranja","sirin","farhad","jodha","akbar"]




dhru= library("Dhrumi",["romeo","juliet","heer","ranja"])
dhrum=library("dhrum",["sirin","farhad","jodha","akbar"])

i=0
while(i==0):
        print("********WELCOME TO MY LIBRARY********")
        print("choose one of your favourable option")
        print(" 1. take a look on all the books\n 2. lend a book\n 3. return a book\n 4. add a book")
        print("input your number for your option")
        a= int(input())
        if(a==1):
            dhrum.display_book()
        elif(a==2):
            dhrum.lend_book()
        elif(a==3):
            dhrum.return_book()
        elif(a==4):
            dhrum.add_book()
        else:
            print("enter a valid input")
        print("type 0 to continue and 1 to exit")
        i=int(input())


print("thank you for using my library")
print(lended_books)
listlend= list(lended_books.items())
listadd= list(addeddict.items())
total1=(("Dhrumi","romeo"),("Dhrumi","juliet"),("Dhrumi","heer"),("Dhrumi","ranja"),)



def func1(listlend):
    print(listlend)
func1(listlend)

# def func2(a,c):
#     print(a,c)
# func2()

def func3(listadd):
    print(listadd)
func3(listadd)
# Press the green button in the gutter to run the script.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
