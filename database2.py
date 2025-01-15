import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database='Carrental')
my_cursor=mydb.cursor()

#the car rental info table thingy
Booking="create table Booking(ID int(20) primary key,BookingNo int(50),UserMail varchar(100),UserName varchar(50),UserContact varchar(20),VehicleId int(10),FromDate varchar(10),ToDate varchar(10),Days int(100));"
my_cursor.execute(Booking)

#values and query for the main table

Booking_data=[(1,101,'ritmand@gmail.com','ritmandeep','+973 1818 1919',3,'2022-01-12','2022-01-20',3),(2,102,'faizan@gmail.com','faizan','+973 8712 1408',2 ,'2022-01-13','2022-01-21',4),(3,103,'adil@gmail.com','adil','+973 3236 9547',1,'2022-01-14','2022-01-22',10),(4,104,'abdullah@gmail.com','abdullah','+973 3236 9547',1,'2022-01-15','2022-01-23',12),(7,107,'suryansh@gmail.com','suryansh','+973 9367 5753 ',5,'2022-01-18','2022-01-26',1)]

for row in Booking_data:
    Booking_query="insert into Booking(ID,BookingNo,UserMail,UserName,UserContact,VehicleId,FromDate,ToDate,Days) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    my_cursor.execute(Booking_query,row)
    mydb.commit()

#table for the car catelogue
autoshow="create table autoshow(ID int(60) primary key,VehicleId int(100),Brand varchar(50),Model varchar(50),Year varchar(10),Priceperday varchar(100),Status varchar(15),Noofcars int(30));"
my_cursor.execute(autoshow)


#values and query for the catelogue table (the new one)

autoshow_data=[(1,1, 'Toyota','Glanza' , '2022', 10,'Available',5),(2,2, 'Mercedes-Benz', 'A-Class' , '2022' , 25, 'Available' , 5),(3,3, 'Lexus' , 'UX' , '2022' , 15, 'Available' , 5),(4,4, 'Audi' , 'S4' , '2022' , 15 , 'Available' , 5),(5,5, 'Nissan' , 'Altima' , '2022' , 10 , 'Available' , 5)]


for row in autoshow_data:
    autoshow_query="insert into autoshow(ID,VehicleId,Brand,Model,Year,Priceperday,Status,Noofcars) values(%s,%s,%s,%s, %s, %s, %s,%s);"
    my_cursor.execute(autoshow_query,row)
    mydb.commit()

#testimonial table

testimonial="create table testimonial(BookingNo int(60) primary key,Testimonial varchar(1000),PostingDate varchar(100));"

my_cursor.execute(testimonial)

#values and query for the testimonial table

testimonial_data=[(101,'fast and best price','2022-01-20'),(102,'EPIC','2022-01-21'),(103,'fast','2022-01-22'),(104,'best price','2022-01-23'),(105,'best service ','2022-01-24'),(106,'VIP actually feels like VIP','2022-01-25'),(107,'Im not even a VIP but this feels very noice','2022-01-26'),(108,'feels good','2022-01-27'),(109,'trusted','2022-01-28'),(110,'reliable','2022-01-29'),(111,'better than the other rental ive used','2022-01-30'),(112,'approved','2022-01-31'),(113,'Best rental','2022-02-01')]

for row in testimonial_data:
    testimonial_query="insert into testimonial(BookingNo,Testimonial ,PostingDate) values(%s, %s, %s);"
    my_cursor.execute(testimonial_query,row)

#billing table
billing="create table Billing(ID int(20) primary key,BookingNo int(50),UserStatus varchar(10),VehicleId int(20),No_of_days int(100),Total_Bill decimal(50,2),Currency varchar(10));"
my_cursor.execute(billing)
