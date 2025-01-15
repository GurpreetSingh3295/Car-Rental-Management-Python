import mysql.connector
import VIP

def op():
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database='Carrental')
    my_cursor=mydb.cursor()

    
    #to get price per day access table
    my_cursor.execute('select * from autoshow;')
    myresult=my_cursor.fetchall()

    #to check get ststus and booking number and days
    result=VIP.Status()
    bk_no=result[1]
    status=result[0]
    no_days=result[2]
    vehicleid=result[3]
    
    #to get priceperday
    for record in myresult:
        if record[1]==vehicleid:
            priceperday=record[5]
    return(priceperday)

