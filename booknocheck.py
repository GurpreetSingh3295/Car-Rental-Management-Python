import mysql.connector
#to check id for adding record last value
#program for the file Car_Menu.py

def bookno():
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database='Carrental')
    my_cursor=mydb.cursor()
    my_cursor.execute("SELECT * FROM booking;")
    myresult = my_cursor.fetchall()
    for rec in myresult:
        bk=rec[1] 
    return(bk)




