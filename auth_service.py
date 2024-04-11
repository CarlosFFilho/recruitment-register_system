from initial_page import *
from flask import Flask
from sql import *
import mysql.connector
import datetime
import pytz
import jwt


app_auth = Flask(__name__)


def conectar_bd():
    
    return mysql.connector.connect(
        host="host",
        user="user",
        password="password",
        database="database",
        port="port"
    )


# FUNCTION TO GENERATE TOKEN

@app_auth.route('/generatetoken')

def generate_token(payload):
    
    SECRET_KEY = "987654321"
    
    now = datetime.datetime.utcnow()
    time_zone_brazil = pytz.timezone('America/Sao_Paulo')
    now_brazil = now.replace(tzinfo=pytz.utc).astimezone(time_zone_brazil)
    expiration = now_brazil + datetime.timedelta(minutes=10)
    
    payload_info = {'Email_user': payload, 'exp': expiration}
    
    token = jwt.encode(payload_info, SECRET_KEY, algorithm='HS256')
    
    return token


# USER VERIFICATION FUNCTION

@app_auth.route('/verifyuser')

def verify_user(email, password):
    
    try:
        
        connection = conectar_bd()
        cursor = connection.cursor(dictionary=True)
        
        query = "SELECT * FROM users WHERE email_user = %s AND password_user = %s"
        
        cursor.execute(query, (email, password))
        user = cursor.fetchone()

        cursor.close()
        connection.close()

        return user


    except mysql.connector.Error as error:
        
        print("Error connecting to database:", error)
        
        return None
    

# USER AUTHENTICATION FUNCTION

@app_auth.route('/authenticateuser')

def authenticate_user(email, password):
    
    user = verify_user(email, password)
    
    print(user)
    
    user = user['Email_user']
    
    if user:
        
        token = generate_token(user)
        print("Token generated:", token)
        
        verify_token(token)
        
        return token
    
    
    else:
        
        print("Invalid credentials.")


# TOKEN VERIFICATION FUNCTION

@app_auth.route('/verifytoken')

def verify_token(token):
    
    try:
        
        SECRET_KEY = "987654321"
        
        payload_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])


        if 'exp' in payload_token:
            
            now = datetime.datetime.utcnow()
            time_zone_brazil = pytz.timezone('America/Sao_Paulo')
            now_brazil = now.replace(tzinfo=pytz.utc).astimezone(time_zone_brazil)

            expiration = datetime.datetime.fromtimestamp(payload_token['exp'])
            expiration = expiration.astimezone(time_zone_brazil)
            
            
            if now_brazil > expiration:
                
                return print("Expired Token 1")
            
            
            else:
                
                initial(expiration)
                
                return print("ACCESS RELEASED!")


    except jwt.ExpiredSignatureError:
        
        return print("Expired Token 2")
    
    
    except jwt.InvalidTokenError:
        
        return print("Invalid token")


# USER LOGIN FUNCTION

@app_auth.route('/logininfo')

def login_informations(email, password):
    
    email = email
    password = password
    
    authenticate_user(email, password)
    

# FUNCTION TO REGISTER NEW USER

@app_auth.route('/registerusers')

def register_users(name, email, password):
    
    new_user = ["DEFAULT, '{0}', '{1}', '{2}'".format(name, email, password)]
    insert_data(new_user, "users")


if __name__ == '__main__':
    
    app_auth.run(debug=True)
