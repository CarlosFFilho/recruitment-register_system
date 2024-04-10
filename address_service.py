from flask import Flask
from sql import *


app_address = Flask(__name__)


# HOME PAGE

@app_address.route('/')

def __init__(self, Identity_person, Street, City, State, Postal_code, Country, Avaliable_for_change):
    
    self.Identity_person = Identity_person
    self.Street = Street
    self.City = City
    self.State = State
    self.Postal_code = Postal_code
    self.Country = Country
    self.Avaliable_for_change = Avaliable_for_change


# MECHANISM TO SAVE LOCATION INFORMATIONS

@app_address.route('/saveaddress')

def Save_Sql(Identity_person, Street, City, State, Postal_code, Country, Avaliable_for_change):
    
    concept3 = "Eligible" if State == "Alagoas" or Avaliable_for_change == "YES" else "No"
    values3 = ["DEFAULT, '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}'".format(Identity_person, Street, City, State, Postal_code, Country, Avaliable_for_change, concept3)]
    insert_data(values3, "address")


if __name__ == '__main__':
    
    app_address.run(debug=True)