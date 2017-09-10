#! /usr/bin/python3

import psycopg2

connectionString = "dbname='postgres' user='postgres' password='postgres123' host='localhost' port='5432'"

def createTable():
    conn = psycopg2.connect(connectionString)
    cur = conn.cursor()
    cur.execute("CREATE TABLE if not EXISTS Store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insertItem(item, quantity, price):
    conn = psycopg2.connect(connectionString)
    cur = conn.cursor()
    # cur.execute("INSERT INTO Store VALUES('%s','%s','%s')" % (item, quantity, price))  --> sql injection prone
    cur.execute("INSERT INTO Store VALUES(%s,%s,%s)", (item, quantity, price))  #--> sql injection protected
    conn.commit()
    conn.close()

def updateItem(item, quantity, price):
    conn = psycopg2.connect(connectionString)
    cur = conn.cursor()
    cur.execute("UPDATE Store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))  # ? used to protect from sql injection
    conn.commit()
    conn.close()

def deleteItem(item):
    conn = psycopg2.connect(connectionString)
    cur = conn.cursor()
    cur.execute("DELETE FROM Store WHERE item=%s", (item,))  # ? used to protect from sql injection
    conn.commit()
    conn.close()

def viewTableData():
    conn = psycopg2.connect(connectionString)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Store")
    allRows = cur.fetchall()
    conn.close()
    return allRows

createTable()
insertItem("Bottle", 10, 50.5)
insertItem("Spoon", 5, 20.5)
updateItem("Bottle", 15, 45.0)
deleteItem('Bottle')

print(viewTableData())
