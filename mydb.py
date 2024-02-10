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
#line 19 requires actual password which is redacted
import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'fake_password'

	)
#Prepare cursor object

cursorObject = dataBase.cursor()f

#Create Database
cursorObject.execute("CREATE DATABASE elderco")

print('connector object created for python and mysql database communication \n cursor object created \n database created')
