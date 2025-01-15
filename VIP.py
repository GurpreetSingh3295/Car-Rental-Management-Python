import mysql.connector

#to check VIP or not
def Status():
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database='Carrental')
    my_cursor=mydb.cursor()
    query='select * from booking'
    my_cursor.execute(query)
    myresult=my_cursor.fetchall()

    bookingnumber=int(input('Enter booking number-'))
    for record in myresult:
        if record[1]==bookingnumber:
            status=record[2]
            days=record[9]
            vid=record[6]
            Id=record[0]
    return(status,bookingnumber,days,vid,Id)


