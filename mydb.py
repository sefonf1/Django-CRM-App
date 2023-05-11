import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Lindawa97'


	)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE sefcompany")

print("Done.")