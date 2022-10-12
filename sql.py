import MySql.connector
import mysql as mysql

mydb = MySql.connector.connect(
    host = 'localhost',
    user = 'yourusername',
    password = 'yourpassword'
)




print(mydb)


