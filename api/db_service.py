# IMPORTING LIBRARIES

import mysql.connector


# CONNECTING TO THE DATABASE SERVER

def db_connection():

    con = mysql.connector.connect(host= "host",
                            database= "database",
                            user= "user",
                            password= "password",
                            port = "port")
    return con


# DATABASE INSERTION MECHANISM

def insert_data(values, table):

    con = db_connection()
    c = con.cursor()

    query = "INSERT INTO " + table
    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values]) 
     
    c.execute(query)
    con.commit()
    
    c.close()
    con.close()

    return "Data entered successfully"


# DATABASE QUERY MECHANISM

def consult_data(column, table, identity_confirm):

    con = db_connection()
    c = con.cursor()

    query2 = "SELECT " + column
    query2 = query2 + " FROM " + table
    query2 = query2 + " WHERE Identity = " + str(identity_confirm)

    c.execute(query2)
    
    return c.fetchall()
