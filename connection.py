import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


mydb = mysql.connector.connect(
                                host     = "109.238.191.44",
                                port     = "2561",
                                user     = "CRMERP",
                                password = "CRMERP320//14",
                                database = "VATANZARINDB"
                                )

mycursor = mydb.cursor()

mycursor.execute("show tables")
