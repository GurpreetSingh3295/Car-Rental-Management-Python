import mysql.connector
from tabulate import tabulate
#program for the file Car_Menu.py

def Id():
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database='Carrental')
    my_cursor=mydb.cursor()
    ID=int(input('Enter the id-'))
    my_cursor.execute("SELECT* FROM booking where ID={};".format(ID))
    myresult = my_cursor.fetchall()
    print(tabulate(myresult,headers=['ID','BookingNo','UserStatus','UserMail','UserName','UserContact','VehicleId','FromDate','ToDate','Days'],tablefmt='fancy_grid'))
    


def Book():
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database='Carrental')
    my_cursor=mydb.cursor()
    status=input('Enter your Booking Number-')
    my_cursor.execute("SELECT* FROM booking where BookingNo='{}';".format(status))
    myresult = my_cursor.fetchall()
    print(tabulate(myresult,headers=['ID','BookingNo','UserStatus','UserMail','UserName','UserContact','VehicleId','FromDate','ToDate','Days'],tablefmt='fancy_grid'))
  



def name():
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database='Carrental')
    my_cursor=mydb.cursor()
    name=input('Enter your name-')
    my_cursor.execute("SELECT* FROM booking where UserName='{}';".format(name))
    myresult = my_cursor.fetchall()
    print(tabulate(myresult,headers=['ID','BookingNo','UserStatus','UserMail','UserName','UserContact','VehicleId','FromDate','ToDate','Days'],tablefmt='fancy_grid'))

































