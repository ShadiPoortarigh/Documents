import pyodbc 
from pyodbc import *
server = '95.38.72.7,2560'
database = 'dashboard'
username = 'CRMERP' 
password = 'CRMERP320//14' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute('SELECT * FROM invoice')

for row in cursor:
    print(row)
