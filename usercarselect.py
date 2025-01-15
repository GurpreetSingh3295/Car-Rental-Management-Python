import mysql.connector
from tabulate import tabulate
#program to select car by user

def Car_select():
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database='Carrental')
    my_cursor=mydb.cursor()
    my_cursor.execute("SELECT* FROM autoshow")
    myresult = my_cursor.fetchall()
    print('\t\t\t\tWELCOME TO OUR SHOWROOM\n\t\tHERE IS A LIST OF VEHICLES YOU CAN CHOOSE FROM TO RENT:')
    print(tabulate(myresult,headers=['ID','VehicleId','Brand','Model','Year','Price_Per_Day','Status','Noofcars'],tablefmt='fancy_grid'))
    Vehicleid=int(input('\t\t\tENTER THE VEHICLE ID YOU WOULD LIKE TO CHOOSE-'))

    if True:
        for record in myresult:
            if record[1]==Vehicleid and record[6]=='Available' and record[7]>0:
                #print(record)
                #print(tabulate(record,headers=['ID','VehicleId','Brand','Model','Year','Price_Per_Day','Status','Noofcars'],tablefmt='fancy_grid'))
                opt=input('\t\t\t\tDO YOU WANT TO CONFIRM YOUR CAR? y/n')
                if opt in 'Yy':
                    print('\t\t\t\t================= CAR SELECTED ================')
                    return(Vehicleid)
                else:
                    Car_select()
        else:
            print('-------------------------TRY AGAIN! CAR IS NOT AVALIABLE RIGHT NOW----------------------')
            Car_select()
        #Car_select()
# deleted if-else cuz it wasnt working





