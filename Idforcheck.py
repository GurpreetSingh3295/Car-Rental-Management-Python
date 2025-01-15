import mysql.connector
# for adding record to check last id
#program for the file Car_Menu.py

def Idch():
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database='Carrental')
    my_cursor=mydb.cursor()
    my_cursor.execute("SELECT * FROM booking;")
    myresult = my_cursor.fetchall()
    for rec in myresult:
        Id=rec[0] 
    return(Id)






