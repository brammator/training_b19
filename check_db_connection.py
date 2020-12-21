# -*- coding: utf-8 -*-
import mysql.connector

connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.exec
finally:
    connection.close()