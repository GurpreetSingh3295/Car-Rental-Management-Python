import mysql.connector
import Idforcheck
import booknocheck
import usercarselect
import tkinter  as tk
from tkinter  import *
#program for the file Car_Menu.py
#booking

def Add():
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database='Carrental')
    my_cursor=mydb.cursor()
    name=input('Enter your Name-')
    Idd=Idforcheck.Idch()+1
    book=booknocheck.bookno()+1
    mail=input('Enter your Mail Id-')
    contact=input('Enter your contact number-')
    vehicleid=usercarselect.Car_select()
    fdate=input('Enter the date from rented(yyyy-mm-dd)-')
    tdate=input('Enter the date till rented(yyyy-mm-dd)-')
    days=int(tdate[8:])-int(fdate[8:])
    
    rec=(Idd,book,mail,name,contact,vehicleid,fdate,tdate,days)
    
    query='insert into booking(ID,BookingNo,UserMail,UserName,UserContact,VehicleId,FromDate,ToDate,Days) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);'

    my_cursor.execute(query,rec)
    mydb.commit()
    print('\t\t\t\t=================== Booking Done! =======================')
    print('\t\t\t\t\tYOUR BOOKING NUMBER IS-',book)
    
#to change status of car after booking

    Query='update autoshow set Noofcars=Noofcars-1 where VehicleId={}'.format(vehicleid)
    my_cursor.execute(Query)
    mydb.commit()

