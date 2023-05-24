#install mysql
#pip install django
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python
#pip install django
#pip install mysqlclient
#django-admin startproject <projectName> (dcrm)
#cd <projectName>
#python manage.py startapp <name of app> (website)
#winpty python manage.py createsuperuser
#python manage.py runserver
import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Waldspurger22!'

	)
#Prepare cursor object

cursorObject = dataBase.cursor()f

#Create Database
cursorObject.execute("CREATE DATABASE elderco")

print('connector object created for python and mysql database communication \n cursor object created \n database created')