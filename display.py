import mysql.connector
from tabulate import tabulate

#for customers to view other reviews
def ViewFeedback():
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database='Carrental')
    my_cursor=mydb.cursor()
    my_cursor.execute("SELECT Testimonial, PostingDate FROM testimonial;")
    myresult = my_cursor.fetchall()
    print(tabulate(myresult,headers=['Testimonial','PostingDate'],tablefmt='fancy_grid'))
    