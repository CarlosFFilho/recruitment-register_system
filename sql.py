# IMPORTANDO BIBLIOTECAS

from flask import Flask
import MySQLdb

# CONECTANDO-SE COM O SERVIDOR DO BANCO DE DADOS

app = Flask(__name__)

def db_connection():
    con = MySQLdb.connect(host= "insert_host",
                            database= "insert_database",
                            user= "insert_user",
                            password= "insert_password",
                            port = "insert_port")
    return con

# MECANISMO DE INSERÇÃO AO BANCO DE DADOS

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

    return "Dados inseridos com sucesso"

# MECANISMO DE CONSULTA AO BANCO DE DADOS

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