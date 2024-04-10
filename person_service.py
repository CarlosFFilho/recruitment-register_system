from flask import Flask
from sql import *


app_person = Flask(__name__)


# HOME PAGE

@app_person.route('/')

def __init__(self, Name, Identity, Type_identity, Phone_number, Email_address, Driving_licence, Driving_licence_class):
    
    self.Name = Name
    self.Identity = Identity
    self.Type_identity = Type_identity
    self.Phone_number = Phone_number
    self.Email_address = Email_address
    self.Driving_licence = Driving_licence
    self.Driving_licence_class = Driving_licence_class


# MECHANISM FOR SAVING PERSONAL INFORMATIONS

@app_person.route('/saveperson')

def Save_Sql(Name, Identity, Type_identity, Phone_number, Email_address, Driving_licence, Driving_licence_class):
    
    concept = "Eligible" if Driving_licence == "YES" and Driving_licence_class == "B" else "No"
    values1 = ["DEFAULT, '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}'".format(Name, Identity, Type_identity, Phone_number, Email_address, Driving_licence, Driving_licence_class, concept)]
    insert_data(values1, "person")


if __name__ == '__main__':
    
    app_person.run(debug=True)