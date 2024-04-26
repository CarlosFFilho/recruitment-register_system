# IMPORTING DATABASE CONNECTOR

from db_service import *


# INSERT CANDIDACY DATA

def Save_Sql(Name, Identity, Type_identity, Phone_number, Email_address, Driving_licence, Driving_licence_class, 
Educational_level, Course, Institution, Year_of_course_completion, English_language, Street, City, State, Postal_code, 
Country, Avaliable_for_change, Chemical_industry_years, Last_position, Performed_activities):

    concept2 = "Eligible" if Educational_level != "Associates" and English_language == "YES" else "No"
    values2 = ["DEFAULT, '{0}', '{1}', '{2}', '{3}', {4}, '{5}', '{6}'".format(Identity, Educational_level, Course, Institution, Year_of_course_completion, English_language, concept2)]
    insert_data(values2, "education")

    concept3 = "Eligible" if State == "Alagoas" or Avaliable_for_change == "YES" else "No"
    values3 = ["DEFAULT, '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}'".format(Identity, Street, City, State, Postal_code, Country, Avaliable_for_change, concept3)]
    insert_data(values3, "address")

    Chemical_industry_years = float(Chemical_industry_years)
    concept4 = "Eligible" if Chemical_industry_years >= 3 else "No"
    values4 = ["DEFAULT, '{0}', {1}, '{2}', '{3}', '{4}'".format(Identity, Chemical_industry_years, Last_position, Performed_activities, concept4)]
    insert_data(values4, "professional_experience")

    concept = "Eligible" if Driving_licence == "YES" and Driving_licence_class == "B" else "No"
    values1 = ["DEFAULT, '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}'".format(Name, Identity, Type_identity, Phone_number, Email_address, Driving_licence, Driving_licence_class, concept)]
    insert_data(values1, "person")

    id_confirm = consult_data("id_person", "person", Identity)
        
    id_confirm = id_confirm[0][0]

    return Identity, id_confirm