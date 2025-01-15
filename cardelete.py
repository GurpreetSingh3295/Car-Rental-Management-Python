import mysql.connector

def dell():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='Carrental')
    my_cursor=mydb.cursor()
    
    vid=int(input('\t\t\tEnter the vehicle id for deletion-'))
    my_cursor.execute('select * from autoshow where VehicleId={}'.format(vid))
    result=my_cursor.fetchall()

    print(tabulate(result,header=['ID','VehicleId','Model','Year','Priceperday','Status'],tablefmt='fancy_grid'))
    M=input('\t\t\tAre you sure u want to delete this car(y/n)-')
    if M in 'yY' :
        query='delete from autoshow where VehicleId={}'.format(vid)
        my_cursor.execute(query)
        mydb.commit()
    else:
        print('\t\t\t\tYou may try later-')
        dell()
    my_cursor.execute('select * from autoshow;')
    result=my_cursor.fetchall()
    print(tabulate(result,header=['ID','VehicleId','Model','Year','Priceperday','Status'],tablefmt='fancy_grid'))

