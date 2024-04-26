# IMPORTING LIBRARIES

import mysql.connector
import datetime
import pytz
import jwt


# IMPORTING DATABASE CONNECTOR

import db_service as dbs


# FUNCTION TO GENERATE TOKEN

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

def verify_user(email, password):
    
    try:
        
        connection = dbs.db_connection()
        cursor = connection.cursor(dictionary=True)
        
        query = "SELECT * FROM users WHERE Email = %s AND password = %s"
        
        cursor.execute(query, (email, password))
        user = cursor.fetchone()

        cursor.close()
        connection.close()

        return user

    except mysql.connector.Error as error:
        
        print("Error connecting to database:", error)
        
        return None
    

# USER AUTHENTICATION FUNCTION

def authenticate_user(email, password):
    
    user = verify_user(email, password)
    
    user = user['Email']
    
    if user:
        
        token = generate_token(user)
        print("Token generated:", token)
        
        expiration = verify_token(token)
        
        return expiration
    
    else:
        
        print("Invalid credentials.")


# TOKEN VERIFICATION FUNCTION

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
                
                return print("Expired Token")
            
            else:
                
                return expiration

    except jwt.ExpiredSignatureError:
        
        return print("Expired Token")
    
    except jwt.InvalidTokenError:
        
        return print("Invalid token")


# USER LOGIN FUNCTION

def login_informations(email, password): 
    
    email = email
    password = password
    
    expiration = authenticate_user(email, password)

    return expiration
    

# FUNCTION TO REGISTER NEW USER

def register_users(name, email, password):
    
    new_user = ["DEFAULT, '{0}', '{1}', '{2}'".format(name, email, password)]
    dbs.insert_data(new_user, "users")

    return ('REGISTER COMPLETE!')