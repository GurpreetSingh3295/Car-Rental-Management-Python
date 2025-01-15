import mysql.connector
import VIP
import priceperday 
from tabulate import tabulate

def Bill():
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
    Id=result[4] #id from booking


    #updating the car back to avaliable, no of cars
    Query='update autoshow set Noofcars=Noofcars+1 where VehicleId={}'.format(vehicleid)
    my_cursor.execute(Query)
    mydb.commit()
    #change done


    #to get priceperday
    price=priceperday.op()


    #to calculate vip discount
    
    if status=='VIP':
        Totalprice=(int(price)*no_days)/0.1
    else:
        Totalprice=int(price)*no_days

    print('Totalprice=',Totalprice,'$')

    Currency='$'
# to add values in billing table

    
    rec=(Id,bk_no,status,vehicleid,no_days,Totalprice,Currency)
    
    query='insert into billing(ID,BookingNo,UserStatus,VehicleId,No_of_days,Total_Bill,Currency) values(%s,%s,%s,%s,%s,%s,%s);'

    my_cursor.execute(query,rec)
    mydb.commit()
    print('Bill has been recorded')

    query='select * from billing where BookingNo={}'.format(bk_no)
    my_cursor.execute(query)
    myresult = my_cursor.fetchall()
    print(tabulate(myresult,headers=['ID','BookingNo','UserStatus','VehicleId','No_of_days','Total_Bill','Currency'],tablefmt='fancy_grid'))


'''
# to check fraud

def amt():
    amt=int(input('enter your payable amt'))
    if amt==Totalprice:
        print('!!!PAYMENT SUSCCESSFUL!!!')
    else:
        print('TRY AGAIN')
        amt()

'''




