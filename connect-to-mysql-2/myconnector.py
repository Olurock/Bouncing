import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hi"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE usage ('name' VARCHAR(255),'email' VARCHAR(255), 'age' INTEGER(10), 'id' INTEGER AUTO INCREMENT PRIMARY KEY)")
myc= "INSERT INTO user(username) VALUES ( %S )"
val = ('PETER', 'ADE')
mycursor.execute(myc,val)
mydb.commit()
#for I in mycursor:
#   print(I[0])
#mydb.commit()