# IMPORTING LIBRARIES

from flask import Flask, request, jsonify
import json


# CREATING API

app_control = Flask(__name__)


# IMPORTING MICROSERVICES

import auth_service as autserv
import insert_informations_service as ininfo
import db_service


# ROUTES

    ## CANDIDACY ROUTE

@app_control.route('/frontinitial', methods=['POST'])

def front__initial():
    
    data = request.get_json()

    Name = data.get('Name')
    Identity = data.get('Identity')
    Type_identity = data.get('Type_identity')
    Phone_number = data.get('Phone_number')
    Email_address = data.get('Email_address')
    Driving_licence = data.get('Driving_licence')
    Driving_licence_class = data.get('Driving_licence_class')
    Educational_level = data.get('Educational_level')
    Course = data.get('Course')
    Institution = data.get('Institution')
    Year_of_course_completion = data.get('Year_of_course_completion')
    English_language = data.get('English_language')
    Street = data.get('Street')
    City = data.get('City')
    State = data.get('State')
    Postal_code = data.get('Postal_code')
    Country = data.get('Country')
    Avaliable_for_change = data.get('Avaliable_for_change')
    Chemical_industry_years = data.get('Chemical_industry_years')
    Last_position = data.get('Last_position')
    Performed_activities = data.get('Performed_activities')

    confirmation = ininfo.Save_Sql(Name, Identity, Type_identity, Phone_number, Email_address, Driving_licence, Driving_licence_class, 
Educational_level, Course, Institution, Year_of_course_completion, English_language, Street, City, State, Postal_code, 
Country, Avaliable_for_change, Chemical_industry_years, Last_position, Performed_activities)
    
    return jsonify(confirmation)


    ## LOGIN ROUTE

@app_control.route('/frontlogin', methods=['POST'])

def front_login():

    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    expiration = autserv.login_informations(email, password)

    return jsonify(expiration)


    ## REGISTER ROUTE

@app_control.route('/frontregister', methods=['POST'])

def front_register():

    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    status = autserv.register_users(name, email, password)

    return jsonify(status)


# RUNNING API

if __name__ == '__main__':
    
    app_control.run(debug=True)