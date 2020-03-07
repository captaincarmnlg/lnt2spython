import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)
mycursor = mydb.cursor()
createdb = "CREATE DATABASE {}"
mycursor.execute("SHOW DATABASES")
mycursor.execute(createdb.format("pyln"))