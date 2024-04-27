# IMPORTING LIBRARIES

from datetime import datetime
import pytz
import requests


# IMPORTING FRONTS PAGES

import register_page as rgp
import initial_page as inp
import confirmation_page as cop


# LOGIN CONNECTION

def load_login(email, password):
    
    url = f'http://<Instance_IP>/frontlogin'

    credentials = {'email': email, 'password': password}

    response = requests.post(url, json=credentials)

    if response.status_code == 200:
        
        expiration = response.json()

        date_string = expiration
        date_format = "%a, %d %b %Y %H:%M:%S %Z"
        expiration = datetime.strptime(date_string, date_format)

        time_zone_brazil = pytz.timezone('America/Sao_Paulo')
        expiration = expiration.replace(tzinfo=pytz.utc).astimezone(time_zone_brazil)

    else:

        print("API ERROR:", response.status_code)

    now = datetime.utcnow()
    time_zone_brazil = pytz.timezone('America/Sao_Paulo')
    now_brazil = now.replace(tzinfo=pytz.utc).astimezone(time_zone_brazil)
        
    if now_brazil < expiration:
    
        inp.initial(expiration)


# CONFIRMATION CONNECTION

def load_confirmation(expiration, identity_confirm, id_confirm):

    now = datetime.utcnow()
    time_zone_brazil = pytz.timezone('America/Sao_Paulo')
    now_brazil = now.replace(tzinfo=pytz.utc).astimezone(time_zone_brazil)
    
    if now_brazil < expiration:

        cop.confirm_page (identity_confirm, id_confirm)


# REGISTER CONNECTION

def load_register(name, email, password):

    url = f'http://<Instance_IP>/frontregister'

    credentials = {'name': name, 'email': email, 'password': password}

    response = requests.post(url, json=credentials)

    if response.status_code == 200:
        
        register_process = response.json()

    else:

        print("API ERROR:", response.status_code)


# CANDIDACY CONNECTION

def load_initial(Name, Identity, Type_identity, Phone_number, Email_address, Driving_licence, Driving_licence_class, 
Educational_level, Course, Institution, Year_of_course_completion, English_language, Street, City, State, Postal_code, 
Country, Avaliable_for_change, Chemical_industry_years, Last_position, Performed_activities):

    url = f'http://<Instance_IP>/frontinitial'

    credentials = {'Name': Name, 'Identity': Identity, 'Type_identity': Type_identity, 'Phone_number': Phone_number, 'Email_address': Email_address, 'Driving_licence': Driving_licence, 'Driving_licence_class': Driving_licence_class, 
'Educational_level': Educational_level, 'Course': Course, 'Institution': Institution, 'Year_of_course_completion': Year_of_course_completion, 'English_language': English_language, 'Street': Street, 'City': City, 'State': State, 'Postal_code': Postal_code, 
'Country': Country, 'Avaliable_for_change': Avaliable_for_change, 'Chemical_industry_years': Chemical_industry_years, 'Last_position': Last_position, 'Performed_activities': Performed_activities}

    response = requests.post(url, json=credentials)

    if response.status_code == 200:
        
        confirmation = response.json()

        return confirmation

    else:

        print("API ERROR:", response.status_code)
