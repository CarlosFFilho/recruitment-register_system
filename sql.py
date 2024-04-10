# IMPORTING LIBRARIES

from flask import Flask
import MySQLdb

# CONNECTING TO THE DATABASE SERVER

app = Flask(__name__)

def db_connection():
    con = MySQLdb.connect(host= "sql10.freesqldatabase.com",
                            database= "sql10697831",
                            user= "sql10697831",
                            password= "RWvxcxPLjK",
                            port = 3306)
    return con


# DATABASE INSERTION MECHANISM

@app.route('/')
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

@app.route('/consult')
def consult_data(column, table, identity_confirm):

    con = db_connection()
    c = con.cursor()

    query2 = "SELECT " + column
    query2 = query2 + " FROM " + table
    query2 = query2 + " WHERE Identity = " + str(identity_confirm)

    c.execute(query2)
    
    return c.fetchall()

if __name__ == '__main__':
    app.run(debug=True)