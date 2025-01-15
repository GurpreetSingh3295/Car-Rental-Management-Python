import mysql.connector
from tabulate import tabulate


#manage booking
#cancel booking

def Cancel():
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database='Carrental')
    my_cursor=mydb.cursor()
    book=int(input('\t\t\tEnter booking number-'))
    try:
        query="SELECT VehicleId,BookingNo from booking where BookingNo={};".format(book)
        my_cursor.execute(query)
        myresult = my_cursor.fetchall()
        vid=myresult[0][0]

        Query='delete from booking where BookingNo={}'.format(book)
        my_cursor.execute(Query)
        mydb.commit()
        print('\n\t\t\t\t================ Booking Canceled =================\n')
   
  
        #updating the car back to avaliable, no of cars
        Query='update autoshow set Noofcars=Noofcars+1 where VehicleId={}'.format(vid)
        my_cursor.execute(Query)
        mydb.commit()
        #change done

    except:
        print('\t\t\t\n================= INVALID BOOKING NUMBER ==================\n')
        Cancel()




def Update_Days():
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database='Carrental')
    my_cursor=mydb.cursor()
    opt=input('Are you sure you want to change the rental period?(y/n)-')
    if opt in 'Yy':
        book=int(input('Enter booking number-'))
        fdate=input('Enter the date from rented(yyyy-mm-dd)-')
        tdate=input('Enter the date till rented(yyyy-mm-dd)-')
        days=int(tdate[8:])-int(fdate[8:])

        query1='update booking set FromDate={} where BookingNo={}'.format(fdate,book)
        my_cursor.execute(query1)
        mydb.commit()
        
        query2='update booking set ToDate={} where BookingNo={}'.format(tdate,book)
        my_cursor.execute(query2)
        mydb.commit()
        
        query3='update booking set Days={} where BookingNo={}'.format(days,book)
        my_cursor.execute(query3)
        mydb.commit()
        
    else:
        Update_Days()
    print('\n\t\t\t==================== UPDATION SUCCESSFULL ===========================\n')












    
